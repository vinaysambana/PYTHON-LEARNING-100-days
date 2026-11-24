'''
Modules ---> User Defined Modules ---> Create,Accessing...
A Module is a Python File(.py) Consists of Object,Variables,Function
we use import keyword....
'''

def greet(name):
    """User defined function"""
    return f'Hello{name}...Welcome to Codegnan'
print(greet("Saketh"))

names = {'Students':['Vinay','Deepak','Lokesh'],
         'age':[25,22,24]}
print(__name__)

def display():
    """Generator Function"""
    yield "Python"
    yield "SQL"


if __name__ == "__main__":
    print(greet("Saketh"))
































