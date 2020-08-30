
list=[]
for i in range (0 ,100):
                list.append(0)
c=1
while(c):
       st = int(input('Enter the starting block: '))
       len = int(input('Enter the length: '))
       for j in range (st,st+len):
         if(list[j]==0):
               list[j]=1
               print(j,"->",list[j])
              
         else:
             print('Block already allocated')
             break
             
       c=int(input("Do you want to continue 1 or 0: "))
       
if(c==0):
      print('  ')

