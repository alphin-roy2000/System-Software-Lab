# block=[0]*100
# flag=1
# check=1
# while(flag==1):
# 	s = int(input("STARTING INDEX:"))
# 	l = int(input("LENGTH:"))
# 	for i in range(s,(s+l)):
# 		if(block[i]==0):
# 			block[i]=1
# 		else:
# 			print("Already allocated\n")
# 			check=0
# 	if(check==1):
# 		print("Allocated\n")
# 		n =  int(input("Do you want to continue? 1 or 0"))
# 		if(n==1):
# 			continue
# 		else:
# 			flag=0
# 			break
# 	else:
# 		break

list=[0]*100
c=11
for i in range(0,100):
  list[i]=0
print("Files allocation")
while(c!=0):
  count=0
  print("Enter starting block and length of files: ")
  st=int(input(""))
  len=int(input(""))
  for x in range(st,(st+len)):
    if(list[x]==0):
      count+=1
  if(len==count):
    for j in range(st,(st+len)):
      if(list[j]==0):  
        list[j]=1
        print(j,list[j])
    if(j!=(st+len-1)):
        print(" The file is allocated to disk")
  else:
    print(" The block is already allocated ")
  c=int(input("continue:"))