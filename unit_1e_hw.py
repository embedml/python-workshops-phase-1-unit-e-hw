
'''
In this file you will fill in each function.

Only edit where it says it is okay to edit. Altering the rest 
of the code may result in false failures. If you have trouble please
reach out to your instructor. :)
'''

'''

For Unit 1D you will practice what you learned below:

- Functions 
    - Creating a function
    - Returning a value (including void)
    - Creating parameters for function
    - Default arguments
    - Multiple returns
'''

#### Create a Function Below! ####
'''
Create a function called useless_function(), have it return None

Hint: Syntax to create a function:

def <function_name>():
    return <some value>

'''

##################################

#### Create a Function Below ####
'''
Create a function called integer_return_5() that returns the integer 5

'''

##################################

#### Create a Function Below ####
'''
Create a function called string_return_I_am_a_string() that returns the string "I am a string!"

'''

##################################

#### Create a Function Below ####
'''
Create a function called add_one(), that takes in a parameter x, adds 1 then returns the value

'''

##################################


#### Create a Function Below ####
'''
Create a function called add_x_y(), that takes in a parameter x, and a parameter y, adds x and y then returns that value

'''

##################################


#### Create a Function Below ####
'''
Create a function called slope_intercept_function(), that takes in parameters, m, x and b. Where:

:param m: (float) The slope to scale the the list x
:param x: (list) The list of values we want to scale and shift based on m and b
:param b: (float) The intercept to shift the values of x

Have the function scale each value of x then add b and store the result back into x.

Have the function return x

Hint: Use a for loop to iterate through the list and indexing to store it back into x
'''


##################################



#### Create a Function Below ####
'''
Create a function called multi_return(), that takes in parameters, x and y

:param x: (int) Integer passed in, scaled by 5 and returned
:param y: (int) Integer passed in, incremented by 2 and returned

Have the function scale the of x by 5 and add 2 to y. 

Have the function return x and y in that order. 

'''

##################################


#### Create a Function Below ####
'''
Create a function called default_args(), that takes in a list x, and a parameter pre_pend


:param x: (list) List we want to prepend onto
:param pre_pend = 5: (int) Integer we would like to prepend to the list x
:return x: (list) List after prepend

Have the default value for pre_pend be 5. Have the function prepend the value pre_pend to the list x.

Return the list x.

Hint: Look up some methods you can use with a list to help you!
'''

##################################

#### Create a Function Below ####
'''Create a function called is_fair_price() that takes in a floats called price and fair_price

:param price: (float) price of an item
:param fair_price: (float) fair price used to compare the variable price
:return isFair: (boolean) holds if the value if fair (True) or not fair (False)

The function should store the value True into a variable called isFair if `price` is less than 
or equal to `fair_price`, otherwise store False into  `isFair`. Then return `isFair`

'''

##################################

#### Create a Function Below ####
'''
Create a function called buy_items() that takes in two dictionaries, one dictionary called 'goods' and another dictionary
called 'shopping_list'. 

Each dictionary will have keys of type string and values of type float. 

:param goods: (dict str:float) A dictionary with items as keys that can be purchased for the value
:param shopping_list: (dict str:float) A dictionary that holds items a person may want and values at the price they think is fair for that item
:return goods_to_buy: (list) A list of the names of items that are at or less of the fair price of that item

This function should check to see if each item in `shopping_list' exists in `goods`, if it does exist then the item price in `goods` should be checked, 
if the item price in `goods` is less than or equal to the price in `shopping_list` that item (just the string) should be added to the list `goods_to_buy`. 
If the item price is more than the fair price, then skip that item. If an item cannot be found in 'goods' that is present in 'shopping_list' it should be skipped.

At the end return the list 'goods_to_buy`, which should be in the order of `shopping_list`

Hint: Use the previous function to reduce the number of lines of code you need. 
Hint Hint: You can create more functions to make this easier to read/understand
'''

##################################


