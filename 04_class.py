print('Class:')

class bike(object): # This is a class of a bike
    """docstring for bike"""
    def __init__(self, brand, wheels = 2, max_speed=60): # the same as a function you can use default values, but the first parameter should be always self.
        self.brand = brand # the values that were given above only exists on the __init__ that is where the class is summoned
        self.wheels = wheels # you can stores the values of the __init__ in the self class
        self.maximun_speed = max_speed # you can use different names, it is not mandatory to use the same
        self.max_mph = max_speed * 0.62 # also you can calculate, append do whatever you want and generate new variables.

    def turbo(self): # You could add functions inside a class and use the self arguments to give all the self.* and use them as you wish
        self.maximun_speed *= 2.0 # modifiying existing variables
        self.max_mph *= 2.0 # modifying existing variables
        return 'bike updated!'# modifying existing variables

    def evaluate(self,age): # you could ask for more arguments if you want
        return self.maximun_speed * age

Mybike = bike('oxford') # Here you are calling the __init__, please note that the self is 'invisible'
print(Mybike.brand) # you can access to variables of the class bike using dot '.'
print(Mybike.wheels) # Here is an example how to call all the variables
print(Mybike.maximun_speed)
print(Mybike.max_mph)
print(Mybike.turbo()) # invoke the function turbo from the class
print(Mybike.evaluate(25)) # invoke the function evaluate from the class
print(Mybike.turbo())
print(Mybike.evaluate(25)) #As you can see this function doesnt change the value of the attributes, but turbo does

