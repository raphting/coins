import os
from google.cloud import pubsub

#Connect to google pub/sub
ps = pubsub.Client()
status = ps.topic(os.environ['PUBSUB_STATUS'])
solution = status.subscription(os.environ['PUBSUB_SOLUTION'])

print("WAITING FOR RESULT...")
while True:
	res = solution.pull(return_immediately=False)
	print("SOLUTION FOUND")
	for r in res:
		print(r[1].data)
		solution.acknowledge([r[0]])

