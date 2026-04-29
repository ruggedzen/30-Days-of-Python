import math

#comment

"""big 
comment"""

list = [1,2,3,4,5] #using square brackets can be changed and allows duplicates
tuple = (1,2,3,4,5) #using parenthesis. Like a list but cannot be changed
set = {1,2,3,4,5} #using curly braces. Order does not matter and does not allow duplicates
dict = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five"} #using curly braces

type(tuple) #to check the type of a variable

"""
Excersise 1
"""
print(type(10) )
print(type(9.8))
print(type(3.14))
print(type(4 - 4j))
print(type(['Asabeneh', 'Python', 'Finland']))
print(type('Rugged'))
print(type('Zen'))
print(type('Place'))

"""
Excersise 2
"""
#Create this file

"""
Exercise 3
"""
point1 = (2, 3)
point2 = (10, 8)

euclidean_distance = math.dist(point1, point2)
print (euclidean_distance)