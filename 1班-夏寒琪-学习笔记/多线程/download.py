import threading
import requests


def download_page(url, filename):
    try:
        response = requests.get(url)
        response.raise_for_status()  # 如果请求失败，抛出HTTPError异常
        with open(filename, 'w', encoding='UTF-8') as f:
            f.write(response.text)
        print(f"Downloaded {url} to {filename}")
    except requests.RequestException as e:
        print(f"Error occurred while downloading {url}: {e}")


def main():
    urls = ['http://www.baidu.com']
    filenames = ['baidu.html']

    # 确保URLs和文件名的数量相同
    assert len(urls) == len(filenames)

    threads = []
    # 若上面的urls是多个网址，则会进入循环，这里只写了一个网址
    for url, filename in zip(urls, filenames):
        t = threading.Thread(target=download_page, args=(url, filename))
        t.start()
        threads.append(t)

        # 等待所有线程完成
    for t in threads:
        t.join()


if __name__ == "__main__":
    main()
