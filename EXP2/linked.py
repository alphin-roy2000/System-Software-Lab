
# pages = [0]*50
# while(1):
#     print("Enter starting block of file")
#     start = int(input())
#     print("Enter the length of file")
#     length = int(input())
#     k = length +start
#     j= start
#     if(pages[start]==0):
#         while(j<k):
#             if (pages[j]==0):
#                 pages[j]=1
#                 print(j,' -> ',pages[j])
#             else:
#                 print('Block',j,'is already allocated\n')
#                 k+=1
#             j+=1
#     else:
#         print("Starting block is already allocated\n")
#     print("Do you want to continue?\nEnter 1 for yes, 0 for no")
#     ch = int(input())
#     if(ch==0):
#         exit()
list=[0]*100
y=1
s=0

ind = int(input("Enter starting index:"))
if(list[ind]==0):
	list[ind]=1
	y=int(input("Do you want to continue 1 to 0"))
	while(y==1):
		val = int(input("Enter next index :"))
		if(list[val]==0):
			list[val]=1
			y=int(input("Do you want to continue 1 or 0 :"))
			if(y==1):
				continue
			else:
				s=1
				break
		else:
			print("Already allocated ")
			y=0
			break
	if(s==1):
		print("Successfully allocated")