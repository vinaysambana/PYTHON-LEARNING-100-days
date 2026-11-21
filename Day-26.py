'''
#Basic Exception handling
a,b = 5,0
try:
    result = a/b
    print(f'Answer is {result}')
except Exception as e:
    print(f'Error is {e}')

#a,b = map(int,input("Enter the values:").split())
#print(a,b)
try:
    a,b = map(int,input("Enter the values:").split())
    print(a,b)
    result = a/b
    print(f'Answer is {result}')
except Exception as e :
    print(f'Error is {e}')

#Multiple Except Blocks
try:
    a,b = map(int,input("Enter the values:").split())
    #print(a,b)
    result = a/b
    print(f'Answer is {result}')
except ValueError:
    print("Values should be only 2 and only integers")
except ZeroDivisionError:
    print("Cannot divide by Zero")
except NameError:
    print("Sariga Chusi Rayuu Bey")

try:
    subjects = ['Python',45,'AI',30]
    #print(subjects[5])
    subjects.apend("SQL")
    print(subjects)
except Exception as e: #this can be written if u want exception to take care
    print(e)
except IndexError:
    print("Make sure to check the length")
except NameError:
    print("Check the spelling")
except AttributeError:
    print("Check the method properly")
finally:
    print("Anyways this will be printed....")


#Catching Multiple Exceptions Together
try:
    value = int(input("Enter a value:"))
    #result = 10/vlue check this case
    f = 10/value
    print(f)
except (ValueError,ZeroDivisionError,NameError) as e:
    print(f'An Error Occured : {e}')


#Raising Exceptions
#You can raise exceptions intentionaly using raise keyword
value = 15
if value < 0:
    raise ValueError("Value cannot be Negative")
else:
    print("Done")


Custom Error Messages:
try:
    raise Exception("Custom Error Message")
except Exception as e:
    print(e)

try:
    value = -15
    if value < 0 or value in [1,20]:
        raise Exception("Value is negative")
except Exception as e:
    print(e)
'''
def fn(a,b):
    """Testing"""
    return a*b
print(fn(50,20))


















    

    



















    
    





































