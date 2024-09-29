
###   (1)Find the length of the string without using len() function

n=input("Enter the name: ")

count=0
for i in n:
    count+=1
print("The length of a name is: ",count)


#   (2)Extrct the username from given Gmail
m=input("Enter the Gmail: ")

pos=m.index('@')

print(m[0:pos])

# (3)Count the frquency of particular char in a string
o=input("Enter the sentence: ")
feq=input("Which word you want to search: ")

count=0

for i in o:
    if i==feq:
        count+=1
print("Frequency of char is",count)


# (4)Write a programme to remove a particlar char from a string

p=input("Enter the name: ")
rem=input("Enter the char you which you want to remove: ")

res=' '
for i in p:
    if i != rem:
        res=res+i
print(res)


#  (5) rite a programm to check whether given string is Palindrome or not
q=input("Enter the word: ")

flag=True

for i in range(0,len(q)//2):
    if q[i] != q[len(q) -i -1]:
        flag=False
        print("Not a palindrome")
        break
if flag:
    print("Palindrome!!!")###
    


#  (6)Write a programm to count the num of words in string without using split() fun!!!
s=input("Enter the sentence: ")

l=[]
temp=" "
for i in s:
    if i !=' ':
        temp=temp+i
    else:
        l.append(temp)
        temp=' '
    
l.append(temp)
print(l)
