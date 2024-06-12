import redis
conn = redis.Redis(host='127.0.0.1',port=6379,db=0)  # 注意要redis启动时才能连接成功
print(conn)
testdata='test123456'
conn.set('Test',testdata)
testd=conn.get('Test')
print(testd)

# 增
conn.set('name','xhq')
# 查
print(conn.get("name"))
# 批量设置值
conn.mset ({"key1":"1","key2":"2","key3":"3"})
print(conn.mget("key1","key2"))
# 删
conn.delete("key1")
print(conn.get("key1"))
