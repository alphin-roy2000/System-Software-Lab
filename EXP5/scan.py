class Scheduler:
	def __init__(self,name):
		self.name = name
		self.head = None
		self.requests = []
	def __repr__(self):
		return(str(self.name))

def seek(requests,head):
	time = 0
	served = []
	start = requests.index(head)
	for i in range(start,len(requests)-1):
		st = abs((requests[i+1]-requests[i]))
		print(f"From {requests[i]} to {requests[i+1]}, seektime:{st}")
		served += [requests[i]]
		time += st
	remaining = [i for i in requests if i not in served]
	remaining.sort(reverse=True)
	for i in range(len(remaining)-1):
		st = abs((remaining[i+1]-remaining[i]))
		print(f"From {remaining[i]} to {remaining[i+1]}, seektime:{st}")
		served += [remaining[i]]
		time += st
	served.append(remaining[i+1])
	return ((f" Seektime: {time}\n Average Time: {time/len(requests)}"),served)



scheduler = Scheduler("SCAN")
print("Enter the order of requests separated by comma:")
scheduler.requests += map(int,input().split(','))
scheduler.head = int(input("Current position of head: "))
timeaxis = [i for i in range(len(scheduler.requests)+1)]
requestaxis = [scheduler.head] + scheduler.requests
requestaxis.sort()
time,served = seek(requestaxis,scheduler.head)
print(time)