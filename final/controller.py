from google.cloud import pubsub
import work_pb2

#Connect to google pub/sub
ps = pubsub.Client()
topic = ps.topic("coins")
tidy = topic.subscription("tidy")

#Get notifications from workers
status = ps.topic("status")
subscription = status.subscription("solution")

#Serialize work instructions in protobuf
msg = work_pb2.Compute()
msg.payload = "jojo"
msg.zeros = 5

#Iterate over work packages and publish in pub/sub
#publish as batch job to avoid a few thousand API calls on the network
with topic.batch() as batch:
    for r in range(100000):
        msg.minnum = r * 10000000
        msg.maxnum = (r+1) * 10000000
        pubmsg = msg.SerializeToString()
        batch.publish(pubmsg)

res = subscription.pull(return_immediately=False)
print("SOLUTION FOUND")
print(res[0][1].data)


#Tidy up queue
res = tidy.pull(return_immediately=True, max_messages=100000)
for r in res:
    tidy.acknowledge(r[0])
