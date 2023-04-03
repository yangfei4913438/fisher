import threading

# 当前的线程，也就是主线程
mt = threading.current_thread()
# 打印线程的名称
print(mt.name)  # MainThread


# 创建一个新的任务
def worker():
    print('i am a new thread...')
    wt = threading.current_thread()
    # 打印线程的名称
    print('my name is', wt.name)  # worker_thread_01


# 定义新的线程
new_t = threading.Thread(target=worker, name='worker_thread_01')
# 启动新的线程
new_t.start()

# 定义新的线程
new_t2 = threading.Thread(target=worker, name='worker_thread_02')
# 启动新的线程
new_t2.start()
