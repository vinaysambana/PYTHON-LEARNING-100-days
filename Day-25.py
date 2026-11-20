#Multiplication table pattern:-

data = [i*j for i in range(1,11) for j in range(1,11)]
#print(data)
'''
for table in data:
    print(table,end = " ")
print(*data)

#get th etable pattern in vertical order
data = [i*j for i in range(1,11) for j in range(1,11)]
for i in range(0, 25, 5):
    print(data[i:i+5])

#Nested Comprehension with if condition
#Syntax:[expression for i in iterable1 for j in iterable2 if condition]
#possible pairs without matching values

data = [(i,j) for i in range(1,4) for j in range(1,4) if i!=j]
print(data)

f = [i*j for i in range(1,4) for j in range(1,4) if i!=j]
print(f)
print(*f)
'''
#Nested Comprehension with if-else Usage
#[true_vlue if conditon else false_value
#for item1 in iterable1 for item2 in iterable2]

week_1 = [15,20,21,22,18,19]
week_2 = [23,19,25,18,19,25]

result_1 = ["Improved" if x<y else "Lagged" for x in week_1 for y in week_2]
print(result_1)

result_2 = ["Improved" if x>y else "Lagged" for x in week_1 for y in week_2]
print(result_2)

#Make sure to check the braces and closures
#In the above case if we replace [] braces with () ---> we don't get tuple

#Generators
result = ("Improved" if x<y else "Lagged" for x in week_1 for y in week_2)
print(result)

#Generators ---> It is a Special Function,which produces one value at a time
#we use yield keyword
'''
def fname():
    """doc string"""
    return value(s)...
    ..................
fname()


def fname():
    """Doc string"""
    yield value1
    yield value2
    yield value3
    ............
fname()


def func():
    """Normal Function"""
    return[1,2,3,4,5]
    #return "Saketh" # A function can have return with multiple values
#print(func())
data = func()
for i in data:
    print(i)

def func():
    """Generator Function"""
    yield 1
    yield 2
    yield 3
#print(func())
b = func()
print(next(b))
print(next(b))
print(next(b))
#print(next(b))


def display():
    """Subjects Covered"""
    yield ["Python",45 Days,'Paperbased Exams']
    yield ["Aptitude",65 Days,'Weekly Exams']
    yield ["SoftSkills",60 Days,"Activities"]
    yield ["Frontend",45 Days,"Projects"]
    yield ["FASTAPI",45 Days,"Integration"]
print(display())
g = display()
print(next(g))
print(f'Subject alloted is {next(g)}')
print(f'Subject alloted is {next(g)}')
print(f'Subject alloted is {next(g)}')

week_1 = [20,14]
week_2 = [15,20]
result = ("Improved" if x<y else "Lagged" for x in week_1 for y in week_2)
#print(result)#it returns a generator
g = result
print(next(g))
print(next(g))#next() function will fetch the value from generator
print(*result)
'''
#Exception Handling ---> It is the mechanism in python to respond to
#Runtime Errors or Exceptions
#Exception is an event that occurs during the execution of a program
#which disrupts its normal flow...

#TypeError,ValueError,IndexError,AttributeError,KeyError,ZeroDivisionError.


#We will be using try,except and finally...
'''
Syntax:
try:    #you write code which may cause an error
    #code that raise an exception
except ExceptionType:    #it handles the error if it occurs
    #code to handle the exception
'''

#Basic Exception handling
a,b = 5,0
try:
    result = a/b
    print(f'Answer is {result}')
except Exception as e:
    print(f'Error is {e}')

















    



















































    
















































