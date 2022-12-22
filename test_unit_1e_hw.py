'''
!!! DO NOT EDIT THIS FILE !!!
'''
import random
from unit_1e_hw import *

def test_useless_function():
    assert useless_function() == None, f"Should return `{None}`, your function returned `{useless_function()}`"

def test_integer_return_5():
    assert integer_return_5() == 5, f"Should return `{5}`, your function returned `{integer_return_5()}`"

def test_string_return_I_am_a_string():
    assert string_return_I_am_a_string() == "I am a string!", f'Should return: "I am a string!", your function returned: {string_return_I_am_a_string()}'

def test_add_one():
    x = random.random()
    assert add_one(x=x) == x + 1, f"Should return `{x + 1}`, your function returned `{add_one()}`"


def test_add_x_y():
    x = random.randrange(-999, 999)
    y = random.randrange(-999, 999)
    assert add_x_y(x, y) == x + y, f"When x is {x}, and y is {y}, correct answer is {x+y}, but \
    your function returned {add_x_y(x=x, y=y)}"

def test_slope_intercept_function():
    m = random.randrange(-999, 999)
    x = [random.randrange(-999, 999), random.randrange(-999, 999), random.randrange(-999, 999), random.randrange(-999, 999), random.randrange(-999, 999)]
    b = random.randrange(-999, 999)
    y = slope_intercept_function(m=m, x=x.copy(), b=b) 
    for index, num in enumerate(y):
        assert num ==  m * x[index] + b, f"Expected: {m * x[index] + b} but your function returned: {slope_intercept_function(m, x, b)[index]}"

def test_multi_return():
    x = random.randrange(-999, 999)
    y = random.randrange(-999, 999)
    assert len(multi_return(x, y)) == 2, f"multi_return must return 2 values, your function returned {len(multi_return(x, y))} values"
    x_out, y_out = multi_return(x=x, y=y)
    assert x_out == x * 5, f"The scaled x value should be: {x * 5}, but your scaled x value was {x_out}"
    assert y_out == y + 2, f"The incremented y value should be: {y + 2}, but your incremented y value was {y_out}"


def test_default_args():
    x_before_prepend = [5, 6, 7, 8, 9]
    assert default_args(x_before_prepend, 4) == [4, 5, 6, 7, 8, 9], f"Passed in {x_before_prepend} and 4, list returned should be {[4, 5, 6, 7, 8, 9]}, but your function returned {default_args(x_before_prepend, 4)}"
    assert default_args([7, 3, 2, 4, 1]) == [5, 7, 3, 2, 4, 1], f"Passed in just {[7, 3, 2, 4, 1]} with no prepend value (resorting to default), list returned should be {[5, 7, 3, 2, 4, 1]}, but got {default_args([5, 7, 3, 2, 4, 1])}"

def test_is_fair_price():
    high_value = random.randint(50, 99)
    low_value = random.randint(0, 49)
    assert is_fair_price(price=high_value, fair_price=low_value) == False
    assert is_fair_price(price=low_value, fair_price=high_value) == True
    high_value = random.randint(50, 99)
    low_value = random.randint(0, 49)
    assert is_fair_price(high_value, low_value) == False
    assert is_fair_price(low_value, high_value) == True
    assert is_fair_price(0, 0) == True
    assert is_fair_price(10, 10) == True

def test_buy_items():
    value_1 = random.randint(200, 1000)/100
    value_2 = random.randint(300, 1000)/100
    value_3 = random.randint(325, 1000)/100
    value_4 = random.randint(250, 1000)/100
    value_5 = random.randint(200, 1000)/100
    value_6 = random.randint(400, 1000)/100


    dict_1 = {
        "cheese" : value_1,
        "milk" : value_2,
        "batteries" : value_3,
        "apples" : value_4,
        "chicken" : value_5,
        "coffee" : value_6,
    }

    dict_2 = {
        "milk" : value_2 + 1,
        "coffee" : value_6 -2
    }

    dict_3 = {
        "butter": 2,
        "chicken" : value_5 + 1,
        "batteries" : value_3,
        "juice" : 5
    }

    l = buy_items(dict_1, dict_2)
    assert l == [list(dict_1.keys())[1]], f"Your list had {l}, which is incorrect"
    l = buy_items(dict_1, dict_3)
    assert l == [list(dict_1.keys())[4], list(dict_1.keys())[2]], f"Your list had {l}, which is incorrect"
    