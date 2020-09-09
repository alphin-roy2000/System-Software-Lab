
class Scheduler:
	def __init__(self,name):
		self.name = name
		self.head = None
		self.requests = []
	def __repr__(self):
		return(str(self.name))

def seektime(requests,head):
	time = abs(requests[0]-head)
	for i in range(len(requests)-1):
		time += abs((requests[i+1]-requests[i]))
	return (f" Seektime: {time}\n Average Time: {time/len(requests)}")


scheduler = Scheduler("FCFS")
print("Enter the order of requests separated by comma:")
scheduler.requests += map(int,input().split(','))
scheduler.head = int(input("Current position of head: "))
timeaxis = [i for i in range(len(scheduler.requests)+1)]
requestaxis = [scheduler.head] + scheduler.requests
time = seektime(scheduler.requests,scheduler.head)
for i in range(len(requestaxis)-1):
	print(f"From {requestaxis[i]} to {requestaxis[i+1]}, seektime:{abs(requestaxis[i+1]-requestaxis[i])}")
print()
print(time)