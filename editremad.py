l=[1,2,3,4,5]
print(l)
l.append(6)
print(l)
l.append(True)
print(l)


#Append fun takes only one arguement to add in list, if you use append list it added as 2d list
l.append([7,8,9])
print(l)
#Extend funtions is used to add many arguments to add in list

l.extend([7,8,9])
print(l)

l1=[1,2,3,4,5]
print(l1)
l1.append('Muni')
print(l1)
l1.extend('Muni')
print(l1)

#Insert
#Insert fun is used the add items at specified loaction which index you want in that index...

l2=[1,2,3,4,5,6]
print(l2)
l2.insert(1,100)
print(l2)

l2.insert(3,1000)
print(l2)

#Editing

l3=[1,2,3,4,5,6,7,8,9,10]
print(l3)

#Editing with index
l3[2]=200
l3[4]=400
print(l3)

#Editing with sicing
l3[1:4]=[1000,2000,3000,4000]
print(l3)