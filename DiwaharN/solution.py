start=int(input("Enter the starting value : "))
end=int(input("Enter the ending value : "))
l=[]
for i in range(start,end):
    if(i%7==0 and i%5!=0):
        l.append(str(i))

output=",".join(l) #Joining the list with comma-seperated join() fuction is used
print(output)
        

 
