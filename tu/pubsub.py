from google.cloud import pubsub

ps = pubsub.Client()

topic = ps.topic("coins")
subscription = topic.subscription("work")

res = subscription.pull(return_immediately=True)

print("Pulled: "+ str(len(res)))

if res:
	print(res[0][1].data)
	subscription.acknowledge(res[0][0])
