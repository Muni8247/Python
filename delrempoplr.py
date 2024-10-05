#Delete
l=[1,2,3,4,5,6,7,8,9,10]

#Index
print(l)
del l[1]
print(l)
del l[6]
print(l)

#Slicing
l=[1,2,3,4,5,6,7,8,9,10]
del l[0:4]
print(l)
del l[-3:-1]
print(l)

#Remove
#While using remove fun we can give a specified num which you want to delete insted of giving index num
l1=[1,2,3,4,5,6,7,8,9,10]
print(l1)

l1.remove(2)
print(l1)
l1.remove(6)
print(l1)
#Pop
l2=[1,2,3,4,5,6,7,8,9,10]

#Clear
l3=[1,2,3,4,5,6,7,8,9,10]


#Pop
#Uisng the pop function is used the delete the last item in the list...
l4=[1,2,3,4,5,6,7,8,9,10]
#Using pop() function
l4.pop()
print(l4)

#pop() using index
l4.pop(2)
print(l4)

l4.pop(-1)
print(l4)


#Clear()
#Using clear function to delete the entire list give the empty list...

l4.clear()
print(l4)