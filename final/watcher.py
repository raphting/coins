from google.cloud import pubsub

#Connect to google pub/sub
ps = pubsub.Client()
status = ps.topic("status")
solution = status.subscription("solution")

print("WAITING FOR RESULT...")
while True:
	res = solution.pull(return_immediately=False)
	print("SOLUTION FOUND")
	for r in res:
		print(r[1].data)
		solution.acknowledge(r[0])

