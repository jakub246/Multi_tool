import math


def get_expr(symbol):
    list_of_operation = [
        {'expr': '+', 'type': 2, 'prec': 1, 'func': add},
        {'expr': '-', 'type': 2, 'prec': 1, 'func': subtraction},

        {'expr': '*', 'type': 2, 'prec': 2, 'func': multiplication},
        {'expr': '/', 'type': 2, 'prec': 2, 'func': division},

        {'expr': '**', 'type': 2, 'prec': 5, 'func': pow},
        {'expr': 'sqrt', 'type': 1, 'prec': 5, 'func': sqrt},

        {'expr': 'sin', 'type': 1, 'prec': 10, 'func': sin},
        {'expr': 'cos', 'type': 1, 'prec': 10, 'func': cos},

        {'expr': 'pi', 'type': 0, 'prec': 20, 'func': pi},
        {'expr': 'e', 'type': 0, 'prec': 20, 'func': e},
    ]

    for elem in list_of_operation:
        if elem['expr'] == symbol:
            return elem
    return None


def add(a, b):
    return a+b


def subtraction(a, b):
    return a-b


def multiplication(a, b):
    return a*b


def division(a, b):
    return a/b


def sin(a):
    return math.sin(a)


def cos(a):
    return math.cos(a)


def pi():
    return 3.14159265359


def e():
    return 2.71828182846


def sqrt(a):
    return math.sqrt(a)


def pow(a, b):
    return a**b
