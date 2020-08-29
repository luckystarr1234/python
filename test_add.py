
from add import add

# DRY - Don't Repeat Yourself


def test_add_char():
 assert add(56245, 58000) == 114245


def test_add_letter():
 return_value = add(451, 0.293)
 print(type(return_value))
 assert return_value == 451.293


def test_add_none():
 return_value = add(-4, 29)
 print(type(return_value))
 assert return_value == 25

def test_add_decimal():
 return_value = add(22, 0.65)
 print(type(return_value))
 assert return_value == 22.65

def test_add_string():
 return_value = add('36', 47)
 print(type(return_value))
 assert return_value == 83

#//////////////////////////////////////

from add import subtract

# DRY - Don't Repeat Yourself

def test_subtract_char():
 assert subtract(58245, 35486) == 22759


def test_subtract_letter():
 return_value = subtract(58.2, 29)
 print(type(return_value))
 assert return_value == 29.2


def test_subtract_none():
 return_value = subtract(78, -56)
 print(type(return_value))
 assert return_value == 134

def test_subtract_decimal():
 return_value = subtract(36, 0.23)
 print(type(return_value))
 assert return_value == 35.77

def test_subtract_string():
 return_value = subtract('583', 82)
 print(type(return_value))
 assert return_value == 501
