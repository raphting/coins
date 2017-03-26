import work_pb2

msg = work_pb2.Compute()

msg.payload = "jojo"
msg.minnum = 1000
msg.maxnum = 2000
msg.zeros = 5

st = msg.SerializeToString()


n = work_pb2.Compute()
n.ParseFromString(st)
print(n.payload)
