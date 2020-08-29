from advanced import multiply

# DRY - Don't Repeat Yourself


def test_multiply_char():
 assert multiply(56245, 58000) == 114245


def test_multiply_letter():
 return_value = multiply(2, 0.5)
 print(type(return_value))
 assert return_value == 1


def test_multiply_none():
 return_value = multiply(-4, 6)
 print(type(return_value))
 assert return_value == -24

def test_multiply_decimal():
 return_value = multiply(43, -0.65)
 print(type(return_value))
 assert return_value == -27.95

def test_multiply_string():
 return_value = multiply('36', 47)
 print(type(return_value))
 assert return_value == 1692

#//////////////////////////////////////////////

from advanced import divide

 # DRY - Don't Repeat Yourself

def test_divide_char():
 assert divide(56245, 58000) == 114245

def test_divide_letter():
 return_value = divide(4.5, 2)
 print(type(return_value))
 assert return_value == 2.25

def test_divide_none():
 return_value = divide(-8, 4)
 print(type(return_value))
 assert return_value == -2

def test_divide_decimal():
 return_value = divide(60, -0.5)
 print(type(return_value))
 assert return_value == -120

def test_divide_string():
 return_value = divide('58', 12)
 print(type(return_value))
 assert return_value == 4.83
