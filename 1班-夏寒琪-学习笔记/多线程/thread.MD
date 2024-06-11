# 多线程学习
## 常用函数
``` python 
threading.active_count()  # 返回当前存货的线程对象的数量  
threading.current_thread()  # 返回当前对应调用者的Thread对象  
threading.enumerate()  # 返回当前所有存活的 Thread 对象的列表  
threading.get_ident()  # 返回当前线程的 “线程标识符”  
threading.get_native_id()  # 返回内核分配给当前线程的原生集成线程 ID
# 创建新线程格式
added_thread=threading.Thread(group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None)
"""
target 是用于 run() 方法调用的可调用对象，name 是线程名称
args 是用于调用目标函数的参数元组,kwargs 是用于调用目标函数的关键字参数字典
"""
start()  # 开始线程活动
join(timeout=None)  # 等待，直到线程终结。这会阻塞调用这个方法的线程，直到被调用 join() 的线程终结
```
## 锁
### 原始锁
原始锁是一个在锁定时不属于特定线程的同步基元组件，原始锁处于 "锁定" 或者 "非锁定" 两种状态之一。它被创建时为非锁定状态。它有两个基本方法， acquire() 和 release() 。当状态为**非锁定**时， acquire() 将状态改为 锁定 并立即返回。当状态是**锁定**时， acquire() 将阻塞直到其他线程调用 release() 将其改为非锁定状态，然后 acquire() 调用重置其为锁定状态并返回。 release() 只在锁定状态下调用， 它将状态改为非锁定并立即返回。
```pyhton
# 实现原始锁类
class threading.Lock():
  acquire(blocking=True, timeout=- 1)  # 可以阻塞或非阻塞地获得锁。在参数 blocking 被设置为 False 的情况下调用，将不会发生阻塞。如果调用时 blocking 设为 True 会阻塞
  release()  # 释放一个锁。这个方法可以在任何线程中调用，不单指获得锁的线程。
  locked()  #当锁被获取时，返回 True。
```
### 重入锁
重入锁是一个可以被同一个线程多次获取的同步基元组件。在内部，它在基元锁的锁定/非锁定状态上附加了 "所属线程" 和 "递归等级" 的概念。在锁定状态下，某些线程拥有锁 ； 在非锁定状态下， 没有线程拥有它。
```pyhton
# 实现重入锁类
class threading.RLock():
  acquire(blocking=True, timeout=- 1)  # 可以阻塞或非阻塞地获得锁。当无参数调用时： 如果这个线程已经拥有锁，递归级别增加一，并立即返回。否则，如果其他线程拥有该锁，则阻塞至该锁解锁。一旦锁被解锁(不属于任何线程)，则抢夺所有权，设置递归等级为一，并返回。如果多个线程被阻塞，等待锁被解锁，一次只有一个线程能抢到锁的所有权。在这种情况下，没有返回值
  release()  # 释放一个锁。释放锁，自减递归等级。如果减到零，则将锁重置为非锁定状态(不被任何线程拥有)，并且，如果其他线程正被阻塞着等待锁被解锁，则仅允许其中一个线程继续。如果自减后，递归等级仍然不是零，则锁保持锁定，仍由调用线程拥有。
```
