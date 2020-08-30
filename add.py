def add(a, b):

    type1 = type(a)
    type2 = type(b)

    if a is None:
        return b

    if b is None:
        return a

    if type1 is not int:
        raise TypeError('First input parameter must be an int. Instead it is '+str(type1))

    if type2 is not int:
        raise TypeError('Second input parameter must be an int. Instead it is '+str(type2))

    return a + b


def subtract(a, b):
    type1 = type(a)
    type2 = type(b)

    if a is None:
        return b

    if b is None:
        return a

    if type1 is not int:
        raise TypeError('First input parameter must be an int. Instead it is ' + str(type1))

    if type2 is not int:
        raise TypeError('Second input parameter must be an int. Instead it is ' + str(type2))

    return a - b