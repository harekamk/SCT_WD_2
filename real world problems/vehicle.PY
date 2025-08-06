#1st data=total no of vehicles(2-wheeler and 4-wheeler)=v and 2nd data=total no of wheels=w. find out how many TW and FW are present
v=int(input("Total no of vehicles:"))
w=int(input("Total no of wheels:"))
if (w&1)==1 or w<2 or w<=v:
    print("Invalid input")
else:
    x=((4*v)-w)//2
    print("Tw={0} FW={1}".format(x,v-x))