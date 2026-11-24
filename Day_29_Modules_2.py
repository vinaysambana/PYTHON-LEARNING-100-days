'''
Modules ---> User Defined Modules ---> Create,Accessing...
Built-in Modules ---> math,os,sys,time.....
A Module is a Python File(.py) Consists of Object,Variables,Function
we use import keyword....

import Day_29_Modules
print(dir(Day_29_Modules)) #use dir to get list of all available methods and attributes
print(type(Day_29_Modules.greet))
print(Day_29_Modules.greet("Saketh"))
print(type(Day_29_Modules.names))
print(Day_29_Modules.names.items())


print(Day_29_Modules.__doc__)#returns docstring (description of module)
print(__doc__)#returns current file docstring


Day_29_Modules.names.update({"Place":"Vizag",
                             "Subjects":['Python','Aptitude','SQL']})

print(Day_29_Modules.names)
print(len(Day_29_Modules.names))


#Accessing Methods/Attributes using from keyword
from Day_29_Modules import greet
print(greet("Codegnan"))

#print(names) #this is not possible as we didn't import it

from Day_29_Modules import greet,names # we can import multiple attributes
print(names)

#Aliasing module names
import Day_29_Modules as Ms
print(Ms.greet("Vijay"))
print(Ms.names.keys())
'''

#To Access all methods/attributes we use '*'
from Day_29_Modules import * #this is only reccommened for user/simple modules
print(names)
print(greet("Saketh"))
f = display()
print(next(f))


















