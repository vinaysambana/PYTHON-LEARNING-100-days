'''
#Map() ---> Transformation
#Filter() ---> Selection
#Reduce() ---> Aggregation (import from functools)

reduce()---> It Reduces an iterable into a single value...
It repeatedly applies a function to combine elements....

we can use it from functools
syntax ---> reduce(function,iterable)
'''
import functools
from functools import reduce
'''
#Sum of numbers from a iterable
numbers = [1,5,2,3,4]
result = reduce(lambda a,b:a+b,numbers)
print(result)


#Largest Number from a collection
data = list(map(int,input().split()))
print(data)
result = reduce(lambda a,b:a if a>b else b,data)
print(result)
print(max(data))

#Return the Longest word in a group of strings

words = ['Python','Developer','SQL','Programming']
longest = reduce(lambda a,b : a if len(a) > len(b) else b,words)
print(f'Longest Word : {longest}')


#List Comprehensions ---> In Python,It is a Precise way to Create Lists

#Syntax ---> [expression for item in iterable]
#iterable ---> list,set,dict or range()

#Native Approach:
lst = []
for i in range(10):
    #print(i)
    lst.append(i)
print(lst)

#Optimized Approach:

lst = [i for i in range(10)]
print(lst)

#Squares of 1-10 numbers in a list
squares = [i**2 for i in range(1,11)]
print(squares)

#Get the Even Numbers of 1-10 Numbers in a list
even_numbers = [i for i in range(1,11) if i%2 == 0]
print(even_numbers)
                
even_numbers = [int(i%2 == 0) for i in range(1,11)]
print(even_numbers)

#Update scores of each person with 10 marks
scores = [25,45,50,60,55]
f_scores = [i+10 for i in scores]
print(f_scores)
m_scores = list(map(lambda i : i+10,scores))
print(m_scores)

names = ['saketh','codegnan','vizag']
#result = ['SAKETH','CODEGNAN','VIZAG']
result = [i.upper() for i in names]
print(result)

result = list(map(lambda i:i.upper(),names))
print(result)

#List Comprehension with if-else usage
#[true_value if condition else false_value for item in iterable]

data = [12,4,5,6,8,9]
result = ["Even" if i%2==0 else "Odd" for i in data]
print(result)

result = [i**2 if i%2==0 else i**3 for i in data]
print(result)
'''
#Nested List Comprehension ---> One Inside Another
#[expression for i in iterable 1 for j in iterable 2]

colours = ['Red','Blue','White']
sizes = ['S','M','L','XL']
dress = [(colour,size) for colour in colours for size in sizes]
print(dress)

d = [(i,j) for i in range(1,5) for j in range(1,5)]
print(d)
print(*d)

d = [(i*j) for i in range(1,5) for j in range(1,5)]
print(d)
























