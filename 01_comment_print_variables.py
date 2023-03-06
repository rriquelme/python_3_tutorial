# Section 1: Comments and Print
# A single line comment in python is indicated by a # at the beginning
''' This 
is 
a 
multiline
comment '''
# A print function prints the code to the console, useful to learn and to debug
print('This is a print') # a comment can also be added after a funcion declaration or variable declaration.
print('you can print multiple things separated by a comma','like this and python will add a space in between')

# Section 2: Variables
var_1 = 5   # This is a int variable
var_2 = 'a' # There is a str variable, no need to invoke int or str as other languages.
var_3 = 1.  # Theis is a float variable
print('Hello World!') # This is regular print
print('Hello','World!') # To append in a print on 2.X version a, is used and it adds a space between
print('Hello',end=" ") # The comma could be at the end
print('World!') # and the result will be the same
print('var_1', var_1) # It could be really helpful to print variables
print('var_2', var_2) # It doesnt care if it is a int str or float etc
print('var_3', var_3) # It doesnt care if it is a int str or float etc
print('var_1 is a ',type(var_1)) # Use 'type' to check which type of variable like int
print('var_2 is a ',type(var_2)) # or str
print('var_3 is a ',type(var_3)) # or float

# List

print('List:')
L = [2, 5, 8, 'x', 'y'] # This is a list 
print(L) # An easy way to print it is with print.
print(L[0]) # The first element starts with 0
print(L[-1]) # The last element is -1
print(L[0:3]) # This will select the elements 0, 1 and 2 (Warning!: not the 3)
print(L[2:4]) # This will select element 2 and 3 
print(L[:-2]) # All elements except the last two
print(L[-2:]) # from the element [-2] until the end
L.append('z') #This is the Way to append elements to a list
print(L) # View the list with the last element appended.

# List Methods:
#append: add an element
print(L.append('Hello')
print(L.append(['Hello','world'])
#insert : index and what to insert
print(L.insert(2,'inserted')
#extend
#del
#remove
#pop
#reverse
#copy

# Dictionary, Tuples
print('Dictionary:')
D = {'k1': 123, 'k2': 456, 1:'v3'} # This is a Dictionary syntax key:value
print(D) # This is how to print a dictionary
print(D['k1']) # This is how to print a value with a given key
print(D.get('k1'))
#pop, popitem, del, clear, copy, sorted(keys), update

print ('Tuple:')
a, b = 1, 5 # The values can be assigned to each element separated with commas
print ('a',a) # value of a
print ('b',b) # value of b
# count index sorted
