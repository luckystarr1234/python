from advanced import multiply

# DRY - Don't Repeat Yourself
import pytest


from add import add

# DRY - Don't Repeat Yourself
# Annotation

@pytest.mark.parametrize("a, b, expected", [
    (1, 1, 1),
    (462, 543, 250866),
    (-4, 6, -24),
    (None, None, None),
    (None, 46, 46),
    (70, None, 70),
    (2.4, 5.8, 13.92),
    (5j + 6, 8j + 9, 40j**2 + 93j + 54 ),
    (2**3, 9**2 ,648 )
])
def test_multiply(a, b, expected):
    assert multiply(a, b) == expected


#//////////////////////////////////////////////

from advanced import divide

 # DRY - Don't Repeat Yourself

def test_divide_char():
 assert divide(56245, 58000) == 114245

def test_divide_letter():
 return_value = divide(4, 2)
 print(type(return_value))
 assert return_value == 2

def test_divide_none():
 return_value = divide(8, 4)
 print(type(return_value))
 assert return_value == -2

def test_divide_decimal():
 return_value = divide(60, 5)
 print(type(return_value))
 assert return_value == 12

def test_divide_string():
 return_value = divide(72, 12)
 print(type(return_value))
 assert return_value == 6
