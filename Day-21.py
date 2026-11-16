'''
#Pass by Refrence ---> When mutable objects (Lists,Sets,Dict) are passed into
#the function,changes inside the function affect the original object...

def update(items):
    """We will assume items as list"""
    items.append("Laptop")
cart = ["Mobile","Watch"]
update(cart)
#print(update(cart))#returns None
print(cart)#Original list changes
#print(update("saketh"))#raises Attribute Error

#Dictionary Usage : ---> Updating profile
def update(profile):
    """Usage of Dictionary"""
    profile['branch'] = "Vizag"
students = {'names':['Sanjay','Akash']}
pfs_students = {'batches':['PFS-VSP-007','PFS-VSP-006'],
                'subjects':['Python','MYSQL','Aptitude']}
update(students)
print(students)
update(pfs_students)
print(pfs_students)

#Pass by Value ---> Original data will not change,Immutable objects
#Pass by Object Refrence ---> Original data will change,Mutable objects


#Built-in functions ---> Functions which are inbuilt in Python
#print(),len(),min(),max(),sorted(),int(),float(),bool(),complex(),str(),
#list(),tuple(),set()dict(),input(),eval(),help()...

#Print(dir())
#print(dir(__builtins__))#returns list of built-in functions and errors
#print(help(print))
#print(help(len))

#abs(),chr(),ord()
print(abs(-34))#returns the absolute value of a numbers
print(chr(67))
print(ord('@'))#returns the ASCII Value
data = [24,56,78,0]
print(any(data))#any() ---> compares bool(x) for any valuer ---> True
print(all(data))#all() ---> needs all values to be present
#print(all(None))
print(any([None]))
print(any([None]))
print(all([None]))
print(bin(6))#returns binary object

print(help(enumerate))

data = ["Akash","Ajay","Sanjay"]
c = dict(enumerate(data))#by defult it creates a counter object
print(c)

d = dict(enumerate(data,1))
print(d)
'''
#Zip ---> it combines multiple collections into a string collection
data = ["Sanjay","Akash","Vijay","Ajay","Bharath"]
marks = [25,20,23,21,18]
f = dict(zip(data,marks))#zip checks for length matching
print(f)






















