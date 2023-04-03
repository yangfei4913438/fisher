import threading
import time

from werkzeug.local import LocalStack

my_stack = LocalStack()
my_stack.push(1)
print('in main thread after push, value is:', my_stack.top)


def worker():
    print('in new thread before push, value is:', my_stack.top)
    my_stack.push(2)
    print('in new thread after push, value is:', my_stack.top)


new_t = threading.Thread(target=worker, name='threaded_01')
new_t.start()

time.sleep(1)

print('finally, in main thread value is:', my_stack.top)

tt = {'name': '张三'}

res = getattr(tt, 'name', 'sss')

print(res)
