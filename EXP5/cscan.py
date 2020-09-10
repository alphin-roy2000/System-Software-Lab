

# class DiskScheduler:
# 	def __init__(self,scedulername):
# 		self.scedulername = scedulername
# 		self.head = None
# 		self.requests = []
# 	def __repr__(self):
# 		return(str(self.scedulername))

# def seek(requests,head):
# 	time = 0
# 	served = []
# 	start = requests.index(head)
# 	for i in range(start,len(requests)-1):
# 		st = abs((requests[i+1]-requests[i]))
# 		print(f"From {requests[i]} to {requests[i+1]}, seektime:{st}")
# 		served += [requests[i]]
# 		time += st
# 	served.append(requests[i+1])
# 	print(f"From {requests[i+1]} to 0, seektime:0")
# 	remaining = [i for i in requests if i not in served] +[0]
# 	remaining.sort()
# 	for i in range(len(remaining)-1):
# 		st = abs((remaining[i+1]-remaining[i]))
# 		print(f"From {remaining[i]} to {remaining[i+1]}, seektime:{st}")
# 		served += [remaining[i]]
# 		time += st
# 	served.append(remaining[i+1])
# 	return ((f" Seektime: {time}\n Average Time: {time/len(requests)}"),served)


	
# scheduler = DiskScheduler("C-SCAN")
# print("Give Request Order")
# scheduler.requests += map(int,input().split(','))
# scheduler.head = int(input("Give initial header"))
# timeaxis = [i for i in range(len(scheduler.requests)+2)]
# requestaxis = [scheduler.head] + scheduler.requests
# requestaxis.sort()
# time,served = seek(requestaxis,scheduler.head)
# print(time)
# '''
# These are implementations of different disk scheduling algorithms
# in python. They were written using a more algorithmic approach
# rather than using the various list functions that are available
# in python. 
 
# Usage: python DiskScheduler.py <initial cylinder position>
 
# i.e.
# python DiskScheduler.py 2150
# '''
# from heapq import *
# # hp is initial head position
# # and requests is the list of requests
# # no of cylinders is 200
# def FCFS(hp,requests):
# 	time = 0
# 	n = len(requests)
# 	pos=hp
# 	for request in requests:
# 		temp=pos
# 		time += abs(request-pos)
# 		pos = request
# 		print("        ",pos,"  seeked with seek  time",abs(request-temp))

# 	# calculate average seek time
# 	avg_seek_time = time / n
# 	return avg_seek_time

# # Shortest Seek Time First
# def SSTF(hp,reqs):
# 	requests = reqs.copy()
# 	time = 0
# 	position = hp
# 	n = len(requests)
# 	heap=[]
# 	while len(requests)>0:
# 		for r in requests:
# 			heappush(heap,(abs(position-r),r))
# 		x=heappop(heap)[1]
# 		time+=abs(position-x)
# 		position=x
# 		print("        ",x,"  seeked")
# 		requests.remove(x)
# 		heap=[]

# 	# calculate average seek time
# 	avg_seek_time = time/n
# 	return avg_seek_time

# def SCAN(hp,reqs):
# 	requests = reqs.copy()
# 	pos = hp
# 	time = 0
# 	end=200
# 	start=0
# 	#seek from curr_pos to end which is 200
# 	for i in range(pos,end+1):
# 		if i in requests:
# 			time+=abs(pos-i)
# 			pos=i
# 			print("        ",i,"  seeked")
# 			requests.remove(i)

# 	time+=abs(pos-end)
# 	pos=end
# 	#seek back to start
# 	for i in range(end,start-1,-1):
# 		if i in requests:
# 			time+=abs(pos-i)
# 			# print(time)
# 			pos=i
# 			print("        ",i,"  seeked")
# 			requests.remove(i)
# 	print(time)
# 	# calculate average seek time
# 	avg_seek_time = time/n
# 	print("Total time ",time)
# 	return avg_seek_time

# def C_SCAN(hp,reqs):
# 	requests = reqs.copy()
# 	pos = hp
# 	time = 0
# 	end=200
# 	start=0
# 	#seek from curr_pos to end which is 200
# 	for i in range(pos,end+1):
# 		if i in requests:
# 			time+=abs(pos-i)
# 			pos=i
# 			print("        ",i,"  seeked")
# 			requests.remove(i)
# 	time+=abs(pos-end)
# 	pos=end
# 	#seek to hp from start
# 	for i in range(start,hp+1):
# 		if i in requests:
# 			time+=abs(pos-i)
# 			pos=i
# 			print("        ",i,"  seeked")
# 			requests.remove(i)
	
# 	# calculate average seek time
# 	avg_seek_time = time/n
# 	print(time)
# 	return avg_seek_time

# def LOOK(hp,reqs):
# 	requests = reqs.copy()
# 	pos = hp
# 	time = 0
# 	end=max(requests)
# 	start=min(requests)
# 	#seek from curr_pos to end which is 200
# 	for i in range(pos,end+1):
# 		if i in requests:
# 			time+=abs(pos-i)
# 			pos=i
# 			print("        ",i,"  seeked")
# 			requests.remove(i)

# 	#seek back to start
# 	for i in range(end,start-1,-1):
# 		if i in requests:
# 			time+=abs(pos-i)
# 			pos=i
# 			print("        ",i,"  seeked")
# 			requests.remove(i)
# 	print(time)
# 	# calculate average seek time
# 	avg_seek_time = time/n
# 	return avg_seek_time

# def C_LOOK(hp,reqs):
# 	requests = reqs.copy()
# 	pos = hp
# 	time = 0
# 	end=max(requests)
# 	start=min(requests)
# 	#seek from curr_pos to max of list 
# 	for i in range(pos,end+1):
# 		if i in requests:
# 			time+=abs(pos-i)
# 			pos=i
# 			print("        ",i,"  seeked")
# 			requests.remove(i)

# 	time+=abs(pos-start)
# 	pos=start
# 	#seek to hp from start
# 	for i in range(start,hp+1):
# 		if i in requests:
# 			time+=abs(pos-i)
# 			pos=i
# 			print("        ",i,"  seeked")
# 			requests.remove(i)
	
# 	# calculate average seek time
# 	avg_seek_time = time/n
# 	return avg_seek_time

# if __name__=='__main__':
# 	print("DISK SCHEDULING:")
# 	print("Provide number of I/O requests")
# 	#n is the number of I/O requests
# 	n = int(input())
# 	print("Provide initial position of disc arm (total cylinders=200)")
# 	hp = int(input())
# 	while hp>200:
# 		print("!!! INVALID !!! try again")
# 		hp = int(input())	
# 	print("Provide positions to visit : max is 200")
# 	requests = []
# 	for i in range(n):
# 		req = int(input())
# 		requests.append(req)

# 	print(requests)

# 	#calling the functions
# 	print("  **********     FCFS       *********")
# 	print("Avg seek time for  fcfs was ",
# 		FCFS(hp,requests))
# 	print("  **********     SSTF       *********")
# 	print("Avg seek time for  sstf was ",
# 		SSTF(hp,requests))
# 	print("  **********     SCAN       *********")
# 	print("Avg seek time for  scan was ",
# 		SCAN(hp,requests))
# 	print("  **********     C-SCAN     *********")
# 	print("Avg seek time for  C-scan was ",
# 		C_SCAN(hp,requests))
# 	print("  **********     LOOK       *********")
# 	print("Avg seek time for  look was ",
# 		LOOK(hp,requests))
# 	print("  **********     C-LOOK     *********")
# 	print("Avg seek time for  C-look was ",
# 		C_LOOK(hp,requests))
# 	print("  **********     Thanks       *********")


def C_SCAN(hp,reqs):
	requests = reqs.copy()
	pos = hp
	time = 0
	end=200-1
	start=0
	for i in range(pos,end+1):
		if i in requests:
			time+=abs(pos-i)
			temp=pos
			pos=i
			print("        ",i,"  seeked with seek time",abs(temp-i))
			requests.remove(i)
	temp=pos
	time+=abs(pos-end)
	print("        ",end,"  seeked with seek time",abs(temp-end))
	pos=end

	for i in range(start,hp+1):
		if(pos==end):
			time+=abs(start-end)
			print("         0  seeked with seek time",abs(end-start))
			pos=start
		if i in requests:
			temp=pos
			time+=abs(pos-i)
			pos=i
			print("        ",i,"  seeked with seek time",abs(temp-i))
			requests.remove(i)
	

	avg_seek_time = time/n
	print("timetaken",time)
	return avg_seek_time

if __name__=='__main__':
	print("\n\n\n  **********     C-SCAN       *********\n\n\n")
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

	print("Avg seek time for  C-Scan was ",
		C_SCAN(hp,requests))