list=[0]*100
flag=1
while(True):
    check=0
    s = int(input("Enter starting index:"))
    if(list[s]==0):
    	list[s]=1
    	flag=int(input("do you want to continue? 1 or 0:"))
    	while(flag==1):
    		v = int(input("Enter next index :"))
    		if(list[v]==0):
    			list[v]=1
    			flag=int(input("Do you want to continue? 1 or 0 :"))
    			if(flag==1):
    				continue
    			else:
    				check =1
    				break
	    	else:
    			print("Already allocated")
    			flag=0
    else:
        print("Already allocated")
        break
    f1=int(input("Do you want to continue allocation"))
    if(f1==0):
        break
