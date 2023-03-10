### Function
print('Function:')
def custom_pow(base:int, exp:int = 2, s:int = 0)-> int: #This will be the example of a function that makes the same as math.pow() and a sum of a value s, the equal represent the default value
    '''This is a docstring, this will be printed in case of help(cusom_pow) is used'''
    for x in range((exp-1)): #as for is a foreach we need a string summoned by range(n-1)
        base *= base
    return base + s # value that the function return

print(custom_pow(5)) # The default way to call the function
print(custom_pow(5,3)) # you can call the function in order of the arguments
print(custom_pow(5,3,2)) # it is not mandatory to set the values that have default values
print(custom_pow(5,s=3)) # you can also force which variable to set with the name of the variable and equal.
