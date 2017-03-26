import multiprocessing
import hashlib
import struct
from google.cloud import pubsub
import work_pb2

#subscribe to working tasks
ps = pubsub.Client()
topic = ps.topic("coins")
#wait 60 sec until requeuing message if not acknowledged
subscription = topic.subscription("work", ack_deadline=60)

#attach to status updates to notify controller
status = ps.topic("status")

#Prepare protobuf parser
msg = work_pb2.Compute()


def crack():
    while True:
        res = subscription.pull(return_immediately=False)
    	msg.ParseFromString(res[0][1].data)

        ZEROS = msg.zeros
        blob = msg.payload.encode('utf-8')

        start = msg.minnum
        end = msg.maxnum

	print("compute " + str(start) + " " + str(end))
        for n in range(start, end):
            nonce = n

            tohash = struct.pack('<Qs', nonce, blob)
            one = hashlib.sha256(tohash).digest()
            two = hashlib.sha256(one).hexdigest()

            #Note for testing: 8 zeros should be computationally quite hard
            if two[0:ZEROS] == ZEROS*"0":
		announce = str(n) + " : " + blob + " : " + two
		print(announce)
                ackid = status.publish(announce)
		print("Ack id: " + ackid)
                break

        subscription.acknowledge(res[0][0])


threads = []
cores = multiprocessing.cpu_count()
for i in range(cores):
    p = multiprocessing.Process(target=crack)
    p.start()
    threads.append(p)
