list=[0]*100
flag=1
check=1
while(flag==1):
	s = int(input("Enter the index block:"))
	if(list[s]==0):
		list[s]=1
		n= int(input("Enter no of blocks:"))
		for i in range(0,n):
			j=int(input("Give block number for the index block:"))
			if(list[j]==0):
				list[j]=1
			else:
				print("Already allocated")
				check=0
				flag=0
				break
		if(check==1):
			flag=int(input("Do you want to continue? 1 or 0 :"))
	else:
		print("Already allocated")
		break
