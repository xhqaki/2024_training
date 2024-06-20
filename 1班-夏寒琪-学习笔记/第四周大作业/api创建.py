from pathlib import Path
from fastapi import FastAPI, Query
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from starlette.responses import FileResponse
from starlette.requests import Request

# 用declarative_base() 创建一个基类，这个基类是所有 ORM 映射类的基类。
Base = declarative_base()


# 定义名为DataInfo的SQLAlchemy模型类，和我创建的data_info表进行交互
class DataInfo(Base):
    __tablename__ = 'data_info'
    id = Column(Integer, primary_key=True)
    image_path = Column(String)
    label_camera_std_path = Column(String)
    label_lidar_std_path = Column(String)
    label_camera = Column(String)
    calib_camera_intrinsic = Column(String)
    calib_lidar_to_camera = Column(String)
    label_lidar = Column(String)


# 设置连接我的mysql数据库
DATABASE_URL = "mysql+pymysql://root:123456@localhost/test"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 我的图片存储image的子目录下
IMAGES_DIR = Path(__file__).parent / "image"

app = FastAPI()

# 使用FastAPI定义一个GET请求的路由，用于下载图片文件。
@app.get("/download/{filename:path}")
async def download_image(filename: str, request: Request):
    # 构造图片文件的完整路径
    image_path = IMAGES_DIR / filename

    # 检查文件是否存在
    if not image_path.exists() or not image_path.is_file():
        return {"message": "File not found"}, 404

        # 发送文件作为HTTP响应
    return FileResponse(image_path, media_type="image/jpg", filename=filename)  # 图片是JPG格式


# 使用FastAPI定义一个GET请求的路由，用于获取下载图片的http地址。
@app.get("/get_image_path/{filename:path}")
async def get_image_path(filename: str, request: Request):
    # 构造图片文件的下载URL
    image_url = request.url_for("download_image", filename=filename)

    # 返回图片的下载URL
    return {"image_path": str(image_url)}


# 使用FastAPI定义一个GET请求的路由，用于查询与给定图片路径关联的数据。
@app.get("/query_data/")
async def query_data(image_path: str = Query(..., description="Image path to query")):
    session = SessionLocal()
    try:
        data = session.query(DataInfo).filter(DataInfo.image_path == image_path).first()
        if data:
            # 返回关联的 lidar/*.json的json数据、返回关联的calib/*/*.json数据，这里还返回了图片的存储路径
            result = {
                "label_camera": data.label_camera,
                "calib_camera_intrinsic": data.calib_camera_intrinsic,
                "calib_lidar_to_camera": data.calib_lidar_to_camera,
                "label_lidar": data.label_lidar,
                "image_path": data.image_path
            }
            return result
        else:
            return {"error": "Data not found"}
    finally:
        session.close()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
