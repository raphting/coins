import queue
import multiprocessing
import threading


pubsub = multiprocessing.JoinableQueue()

for i in range(1,55):
    pubsub.put(i)

def calc(item, no):
    item ** item ** 4
    print("Worker " + no + " result for " + str(item))

def unit(no):
    while True:
        try:
            item = pubsub.get(True, 10)
        except queue.Empty:
            print(str(no) + " queue empty")
            break
        calc(item, str(no))
        pubsub.task_done()

cores = multiprocessing.cpu_count()

threads = []
for i in range(cores):
    p = multiprocessing.Process(target=unit, args=(i,))
    p.start()
    threads.append(p)


pubsub.join()


