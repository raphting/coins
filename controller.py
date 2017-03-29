import os
from google.cloud import pubsub
import work_pb2

#Connect to google pub/sub
ps = pubsub.Client()
topic = ps.topic(os.environ['PUBSUB_WORK'])

#Serialize work instructions in protobuf
msg = work_pb2.Compute()
msg.payload = "example"
msg.zeros = 7

#Iterate over work packages and publish in pub/sub
#publish as batch job to avoid a few thousand API calls on the network
with topic.batch() as batch:
    for r in range(100000):
        msg.minnum = r * 10000000
        msg.maxnum = (r+1) * 10000000
        pubmsg = msg.SerializeToString()
        batch.publish(pubmsg)
	if r % 1000 == 0:
		batch.commit()

print("DONE FILLING QUEUE")
