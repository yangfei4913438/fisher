import threading
import time

from werkzeug.local import Local

my_obj = Local()
my_obj.val = 1


def worker():
    my_obj.val = 2
    print('in new thread val is:', my_obj.val)


new_t = threading.Thread(target=worker, name='threaded_01')
new_t.start()

time.sleep(1)

print('in main thread val is:', my_obj.val)
