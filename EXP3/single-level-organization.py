class Dir:
	def __init__(self,dirname):
		self.dirname = dirname
		self.filelist = []
	def create(self,file):
		if(file not in self.filelist):
			self.filelist.append(file)
			print(f"{file} CREATED IN {self.dirname}")
		else:
			print(f"{file} PRESENT")

	def remove(self,file):
		if(file in self.filelist):
			self.filelist.remove(file)
			print(f"{file} REMOVED FROM{self.dirname}")
		else:
			print("NO FILES")

	def __repr__(self):
		return(f"{dirname}")


dirname = input("Give a diretory name:")
d  = Dir(dirname)
print(f"Directory-> {d.dirname}\n")
while(1):

        print("1.Create\n2.Remove\n3.Display\n4.Exit")
        option= int(input("Choose option:"))
        if(option==1):
                 filename = input("Filename: ")
                 d.create(filename)
        elif(option==2):
                 filename = input("Filename: ")
                 d.remove(filename)
        elif(option==3):
                 print(f"\n\nDirectory is ->{d.dirname}")
                 for file in d.filelist:
                         print(f"{file}  ")
                 if(d.filelist==[]):
                         print("No files")
                 print()
        elif(option==4):
                 print("Bye")
                 exit(0)
        else:
                 print("Invalid Input")





