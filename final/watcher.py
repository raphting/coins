from google.cloud import pubsub

#Connect to google pub/sub
ps = pubsub.Client()
topic = ps.topic("coins")
tidy = topic.subscription("work")

#Get notifications from workers
status = ps.topic("status")
subscription = status.subscription("solution")


print("WAITING FOR RESULT...")
while True:
	res = subscription.pull(return_immediately=False, max_messages=1000)
	if len(res) > 0:
		print("SOLUTION FOUND")
	for r in res:
		print(r[1].data)
		subscription.acknowledge(r[0])

