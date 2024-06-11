import threading
import time


def thread_job():
    print('T1 start\n')
    for i in range(10):
        time.sleep(0.1)  # 暂停0.1s
    print('T1 finish\n')


def T2_job():
    print('T2start\n')
    print('T2finish\n')


def main():
    added_thread = threading.Thread(target=thread_job, name='T1')
    thread2 = threading.Thread(target=T2_job(),name='T2')
    added_thread.start()
    thread2.start()
    added_thread.join()  # 加入主线程
    print('All done\n')


if __name__ == '__main__':
    main()