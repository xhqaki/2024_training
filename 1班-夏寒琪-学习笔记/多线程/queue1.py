import threading
from queue import Queue


def job(a, q):
    for i in range(len(a)):
        a[i] = a[i]**2
    q.put(a)


def multithreading():
    q = Queue()
    threads = []
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [8, 8, 8]]
    for i in range(4):
        t = threading.Thread(target=job, args=(data[i], q))
        t.start()
        threads.append(t)
    for thread in threads:
        thread.join()
    results = []
    for i in range(4):
        results.append(q.get())
    print(results)


if __name__ == '__main__':
    multithreading()