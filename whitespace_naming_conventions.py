# By Kami Bigdely
# PEP8 - whitespaces and variable names.
class Pizza:
    def __init__(self, my_bread_type, cheese_type, meat_type, pizza_toppings,size):
        self.bread_type = my_bread_type
        self.cheese_type = cheese_type
        self.meat_type = meat_type
        self.toppings = pizza_toppings
        self.size = size
    @classmethod
    def create_chicago_pizza(cls, size):
        bread = 'deep-dish bread'
        cheese = 'mozzarella cheese'
        meatType = 'Italian sausage'
        toppings = ['green bell pepper','mushroom', 'chunky tomato sauce', 'onion']
        return cls (bread, cheese, meatType, toppings, size)    
    @classmethod
    def createCalifornia_pizza(ct, meat_Type, size):
        bread = 'thin crust'
        CHEESE = 'feta cheese'
        toppings = [ 'garlic', 'spinach', 'broccoli', 'olives', 'red onion', 'red bell pepper' ]
        return ct(bread, CHEESE, meat_Type, toppings, size) 
    def printInfo(self):
        print('bread type is: ', obj.bread_type)
        print('cheese type is: ', obj.cheese_type)
        print('meat type is: ', obj.meatType)
        print('Toppings are: ', end='')
        print(', '.join(map(str, obj.toppings)))

    
myPizza = Pizza.createCalifornia_pizza('chicken', 'large')
myPizza.printInfo()