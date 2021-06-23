# Loops in Python and conditional:
# Loops: 
# For loop:
print('For:') # The syntax for a For is very important, in python elements are not arranged by { } like in other languages, always remember after : use 4 spaces '    '
L = [2, 5, 8, 'x', 'y'] # Same as above
for x in L: # For in python is like a foreach (for each element)
    print(x) # so in a list the value of x get assigned each value of the list L
D = {'k1': 123, 'k2': 456, 1:'v3'} # same as above
for x in D: # In case it is a dictionary,
    print(x,D[x]) # x is the value of each key and to access each element you should use D[key]

# While loop:
print('While:')
while True: #this is a while statement,
    print('True') # the loop sintax is very important the : at the end of the while and then 4 spaces at the begining of the line, same as for
    break # This breaks the loop

# Conditional:
print('If:')
v1 = 5
if 3 >= v1 > 1: #This is a if, it should have a true condition value to execute the next step
    print('3 >= v1 > 1')
elif 5>=v1 >3: # elif in python is as else if in other languages, it should match the true condition AND the previous if was False
    print('5>=v1 >3')
else: # else, if no other option, this will be the case.
    print('not any condition above')
