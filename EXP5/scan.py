# class DiskScheduler:
# 	def __init__(self,schedulername):
# 		self.schedulername = schedulername
# 		self.head = None
# 		self.requests = []
# 	def __repr__(self):
# 		return(str(self.schedulername))

# def seek(requests,head):
# 	time = 0
# 	served = []
# 	start = requests.index(head)
# 	for i in range(start,len(requests)-1):
# 		st = abs((requests[i+1]-requests[i]))
# 		print(f"From {requests[i]} to {requests[i+1]}, seektime:{st}")
# 		served += [requests[i]]
# 		time += st
# 	remaining = [i for i in requests if i not in served]
# 	remaining.sort(reverse=True)
# 	for i in range(len(remaining)-1):
# 		st = abs((remaining[i+1]-remaining[i]))
# 		print(f"From {remaining[i]} to {remaining[i+1]}, seektime:{st}")
# 		served += [remaining[i]]
# 		time += st
# 	served.append(remaining[i+1])
# 	return ((f" Seektime: {time}\n Average Time: {time/len(requests)}"),served)



# scheduler = DiskScheduler("SCAN")
# print("Give Request Order")
# scheduler.requests += map(int,input().split(','))
# scheduler.head = int(input("Give initial header"))
# timeaxis = [i for i in range(len(scheduler.requests)+1)]
# requestaxis = [scheduler.head] + scheduler.requests
# requestaxis.sort()
# time,served = seek(requestaxis,scheduler.head)
# print(time)

def SCAN(hp,reqs,num):
	requests = reqs.copy()
	pos = hp
	time = 0
	end=200-1
	start=0
	flag=True
	for i in range(pos,end+1):
		if i in requests:
			temp=pos
			time+=abs(pos-i)
			pos=i
			num=num-1
			print("        ",i,"  seeked with seek time ",abs(temp-i))
			requests.remove(i)
	if(num!=0):
	    time+=abs(pos-end)
	    print("        ",end,"  seeked with seek time ",abs(pos-end))
	    pos=end
	    for i in range(end,start-1,-1):
		    if i in requests:
			    temp=pos
			    time+=abs(pos-i)
			    pos=i
			    print("        ",i,"  seeked with seek time:",abs(temp-i))
			    requests.remove(i)
	print(time)
	avg_seek_time = time/n
	print("Total time ",time)
	return avg_seek_time

if __name__=='__main__':
	print("\n\n\n  **********     SCAN      *********\n\n\n")
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

	print("Avg seek time for  scan was ",
		SCAN(hp,requests,n))