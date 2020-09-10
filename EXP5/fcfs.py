
# class DiskScheduler:
# 	def __init__(self,scedulername):
# 		self.scedulername = scedulername
# 		self.head = None
# 		self.requests = []
# 	def __repr__(self):
# 		return(str(self.scedulername))

# def seektime(requests,head):
# 	time = abs(requests[0]-head)
# 	for i in range(len(requests)-1):
# 		time += abs((requests[i+1]-requests[i]))
# 	return (f" Seektime: {time}\n Average Time: {time/len(requests)}")


# scheduler = DiskScheduler("FCFS")
# print("Give Request Order")
# scheduler.requests += map(int,input().split(','))
# scheduler.head = int(input("Give initial header"))
# timeaxis = [i for i in range(len(scheduler.requests)+1)]
# requestaxis = [scheduler.head] + scheduler.requests
# time = seektime(scheduler.requests,scheduler.head)
# for i in range(len(requestaxis)-1):
# 	print(f"From {requestaxis[i]} to {requestaxis[i+1]}, seektime:{abs(requestaxis[i+1]-requestaxis[i])}")
# print()
# print(time)

def FCFS(hp,requests):
	time = 0
	n = len(requests)
	pos=hp
	for request in requests:
		temp=pos
		time += abs(request-pos)
		pos = request
		print("        ",pos,"  seeked with seek  time",abs(request-temp))


	avg_seek_time = time / n
	print("Total time:",time)
	return avg_seek_time

if __name__=='__main__':
	print("\n\n\n  **********     FCFS       *********\n\n\n")
	print("DISK SCHEDULING:")
	print("Provide number of I/O requests")
	n = int(input())
	print("Provide initial position of disc arm (total cylinders=200)")
	hp = int(input())
	while hp>200:
		print("!!! INVALID !!! try again")
		hp = int(input())	
	print("Provide positions to visit : max is 200")
	requests = []
	for i in range(n):
		req = int(input())
		requests.append(req)

	print(requests)

	print("Avg seek time for  fcfs was ",
		FCFS(hp,requests))