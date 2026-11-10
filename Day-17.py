'''
Python ---> POP,OOP
POP ---> Procedure Oriented Programming ---> Functions

#Functions --->
Function ---> A Function is a Block of code(statements) which performs
a specific task.It is a reusable code ---> readbility,reusability and easy
to maintain...

#Types of Functions --->

User Defined Functions ---> def
Built-in FunctionsI---> Python by default(print,len,min,max,sorted,
str,list,bool,dict...)
Anonymous Function ---> Nameless Function ---> lambda(map,filter)
reduce Recursive Functions ---> Recursion ---> Factorial,Fibonacci Series ---> Decorators


Syntax :

def fname(parameters): Function header
    """Doc String (Description of function)"""
    statement(s)......#Body of Function
    ..................
    return value(s)
fname(args) #function call
'''
#Simple Function to understand the reusability
'''
#a = 20
#b = 1
#print(a+b)

def add(a,b):
    """This function returns the sum of given objects"""
    c = a+b
    #print(c)
    return c

print(add(24,25))
print(add(12,13))
print(add('code','gnan'))
print(add([1,2],[3,4,5]))


def add(a,b):
    """Sample Add function"""
    return f'Result is {a+b}'
c,d = map(int,input().split())
print(add(c,d))
print(add("code","gnan"))
g,h = 67,-45.5
e = add(g,h)#Assigning function to a variable 
print(e)
'''

#Functions are also Objects

def greeting():
    """Greetings to the User"""
    #return "Hey Guys Welcome to Codegnan"
    #return 24+256 #A function can have multiple values to return
    #but not multiple return statements
    return "Hey guys","Python","PFS-VSP-007"
    #return len (("Hey guys","Python","PFS-VSP-007"))

print(greeting())
print(greeting()*5)
print(type(greeting))#returns Function
print(type(greeting()))#returns Type of Function


























