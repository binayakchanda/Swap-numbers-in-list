#create a empty list
list=[]

print("enter your length of list:")
n=int(input())

print("Enter the nos: ")
#reading the nos from user
for i in range(0,n):
    ele=int(input())
    list.append(ele)
print("BEFORE",list)

print("Enter the position to be swap:")
pos1=int(input())
pos2=int(input())

temp = list[pos1-1]
list[pos1-1] = list[pos2-1]
list[pos2-1] = temp

print("AFTER:",list)
