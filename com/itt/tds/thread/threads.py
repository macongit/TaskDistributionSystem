
"""Threading Example in Python"""

# importing modules
from threading import Thread
from _thread import allocate_lock


class ThreadExample(Thread):

    """ThreadExample class inherits Thread module to
    make custom threads"""
    counter = 0
    lock = allocate_lock()

    def __init__(self):
        """ThreadExample object Initialization"""
        super().__init__(target=None, args=())

    def run(self):
        """Override the default Thread's run method"""
        ThreadExample.lock.acquire()  # acquiring lock over critical section
        ThreadExample.counter += 1
        f = open(__file__, "r")
        for line in f:
            print(line)
        print(ThreadExample.counter)
        ThreadExample.lock.release()  # releasing lock over critical section

threads = []
t1 = ThreadExample()
t2 = ThreadExample()
t3 = ThreadExample()

threads.append(t1)
threads.append(t2)
threads.append(t3)

t1.start()  # start the overridden run method of ThreadExample
t2.start()
t3.start()

for x in threads:
    """join method makes sure that main thread will
       wait to terminate all the threads"""
    x.join()
