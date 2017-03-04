import multiprocessing
import hashlib
import struct


pubsub = multiprocessing.JoinableQueue()
kill = multiprocessing.JoinableQueue()

def crack():
    blob = "123".encode('utf-8')

    while True:
        start = 0
        end = 0
        try:
            start_stop = pubsub.get(True, 10)
            ss = start_stop.split(",")
            start = int(ss[0])
            end = int(ss[1])
            print("Start with " + str(start), str(end))
        except queue.Empty:
            return

        for n in range(start, end):
            nonce = n

            tohash = struct.pack('<Ls', nonce, blob)
            one = hashlib.sha256(tohash).digest()
            two = hashlib.sha256(one).hexdigest()

            #8 zeros should be computationally quite hard
            if two[0:7] == "0000000":
                print(nonce, two)
                kill.put(True)
                break



for r in range(100000):
    pubsub.put(str(r * 10000000) + "," + str((r+1) * 10000000))

threads = []
cores = multiprocessing.cpu_count()
for i in range(cores):
    p = multiprocessing.Process(target=crack)
    p.start()
    threads.append(p)

kill.get(True)

for t in threads:
    t.terminate()

print("Done.")


