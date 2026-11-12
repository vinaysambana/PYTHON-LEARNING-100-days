#Variables length arguments ---> we can capture any number of positional
#arguments,we use (*args),captures excess positional arguments and
#pack them into __________
'''
def sample(*a):
    """Usage of arbitrary arguments"""
    print(a)
    print(type(a))
sample()
sample(1,2)
sample('saketh','codegnan')
sample([12,3,4,5])

#In above case we used '*' to pack the values into a tuple
a,b,c = 2,4,-6
print(a,b,c)
a,*b,c = 2,4,5,6,65,12,-12
print(a)
print(c)
print(b) #in this case all values are stored into list
#a,*b,*c=2,4,5,6,65,12,-12#Multiple expressions are not allowed...
#print(a)
#print(b)
#print(c)

a,*b,c=(2,4,5),6,65,12,-12
print(a)
print(b)
print(c)

#Find the sum of given Values

def add(*a):
    """Usage of Variable length arguments"""
    #print(a)
    #print(type(a))
    result = 0
    print(a)
    for value in a:
        #if type(value) in (int,float):#membership operator
        if type(i) == int or type(i) == float: #comparision and logical operators
            result = result + value
            #print(result)
    return result
#print(add())
#print(add(1,3,4,5))#1+3+4+5 ---> 13
#print(add(12,3,4,5,6,-98,12))
#print(add(1,2,4,-2,'codegnan',2,12,'saketh'))
#what if we accept group of values
d = list(map(int,input().split()))
print(d)
print(add(*d))#we need to use * to unpack the values from the tuple

#we will use above usage of Variables length arguments for Ordering pizza

def order_pizza(size,*toppings):
    """Usage of *args"""
    print(f'Size of Pizza is : {size}')
    print(f'Toppings :{toppings}')
    for topping in toppings:
        print(f'Topping added : {topping}')
order_pizza("Large","Onions","Paneer","Capisicum","Olives","Mushroom")

#Keyword Variable length arguments : we can pass Any number of keyword arguments,
#Data is stored in dictionary,we use **kwargs...

def sample(**a):
    """Usage of **kwargs"""
    print(a)
    print(type(a))
sample()
sample(name = "Vinay",
       batch = "PFS-VSP-007",
       place = "Vizag",
       branch = "CSE",
       course = "PFS")
'''

def order_pizza(size,*toppings,**details):
    """Usage of *args"""
    print(f'Size of Pizza is : {size}')
   # print(f'Toppings :{toppings}')
    for topping in toppings:
        print(f'Topping added : {topping}')
    for key,value in details.items():
        print(f'Data is {key},result is {value}')
order_pizza( "Large",
            "Onions",
            "Paneer",
            "Capisicum",
            "Olives",
            "Mushroom",
            name = "Vinay",
            bill = 200,
            delivery = False,
            Tip = 50 )













































