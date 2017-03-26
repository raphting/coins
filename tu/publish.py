from google.cloud import pubsub

ps = pubsub.Client()
topic = ps.topic("coins")

mydata = "Hallo ich bins hier"

data = mydata.encode('utf-8')

msgid = topic.publish(data)
