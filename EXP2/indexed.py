# list=[0]*100
# flag=1
# check=1
# while(flag==1):
# 	s = int(input("Enter the index block:"))
# 	if(list[s]==0):
# 		list[s]=1
# 		n= int(input("Enter no of blocks:"))
# 		for i in range(0,n):
# 			j=int(input("Give block number for the index block:"))
# 			if(list[j]==0):
# 				list[j]=1
# 			else:
# 				print("Already allocated")
# 				check=0
# 				flag=0
# 				break
# 		if(check==1):
# 			flag=int(input("Do you want to continue? 1 or 0 :"))
# 	else:
# 		print("Already allocated")
# 		break

f = [0]*50
index = [0]*50
count = 0
def two():
        count = 0
        for i in range(n):
            print("Enter the next index")
            index[i] = int(input())
            if(f[index[i]]==0):
                count+=1
        if(count==n):
            for i in range(n):
                f[index[i]]=1
            print("Allocated\nFile Indexed\n")
            for k in range(n):
                if(ind==index[k]):
                    print(ind,"already allocated")
                    continue
                print(ind,"->",index[k],":",f[index[k]])
        else:
            print("File in index is already allocated")
            print("Enter another file indexed")
            two()
while(1):
    ind = int(input("Enter the index block"))
    if(f[ind]==0):
        n = int(input("Enter the number of blocks needed"))
        two()
    else:
        print("Index block is allocated")
    print("Do you want to continue 1 or 0")
    c = int(input())
    if(c==0):
        exit()