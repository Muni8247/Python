'''#Len() Min() Max() Soretd()

l=[1,2,3,4,5,6,7,8,9,10]
print(len(l))

print(" ")
print("*************MIN***************")
print(min(l))
print(" ")
print("************MAX**************")
print(max(l))
print(" ")
print("********SORTED***********")
print(sorted(l,reverse=True))'''

#Count()
#Count fun is used to count the num of times repeated...
l=[1,2,3,4,4,5,6,7,8,9,10]
print(l.count(4))
print(l.count(1))


# Index()
print(" ")
print("*********INDEX***********")
print(l.index(1))
print(l.index(10))
print(l.index(5))

#Reverse
print(" ")
print("******REVERSE*************")
l.reverse()
print(l)