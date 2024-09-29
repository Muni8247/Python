name="KatigariNagaMuniReddy"
print(len(name))

print("*"*20)
print(max(name))

print("*"*20)
print(min(name))

print("*"*20)
print(sorted(name))

print("*"*20)
print(sorted("KatigariNagaMuniReddy",reverse=True))


#Capitalized

n1="katigari naga muni reddy"
n2="Katigari Naga Muni Reddy"
print(n1.title())
print("*"*25)
print(n2.capitalize())
print("*"*25)
print(n1.lower())
print("*"*25)
print(n2.upper())

print("*"*25)



#Count
a="nagamunireddy"
print(a.count("a"))

#Find
print("*"*25)
print(a.find("a"))

print(a.find("i"))

print(a.find("w"))

#Index
print("*"*25)
print(a.index("i"))

print(a.index("m"))

print("*"*25)
#StartsWith
print(a.endswith("y"))

print(" ")
print("*"*25)
#Format
a="Muni"
b="Reddy"

print("My name is {0} and my caste is {1} caste".format(a,b))

#isalnum
print(" ")
print("*"*25)
b="Muni123"
c="1234567"
print(b.isalnum())

#Isalpha
print(" ")
print("*"*25)
print(b.isalpha())

#Isdigit
print(" ")
print("*"*25)
print(b.isdigit())
print("*"*25)
print(c.isdigit())

#Split
print(" ")
print("Split","*"*25)
d="Hi my name is Naga Muni reddy"
print(d.split())


print(d.split("a"))

#Replace
print(" ")
print("Replace","*"*25)
e="Hi my name is name is Naga Muni Reddy"
print(e.replace("Muni","Swarna"))