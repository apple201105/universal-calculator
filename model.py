def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Ошибка: деление на ноль"
    return a / b
def exponentiation(a,b):
    return a ** b
def root (a):
    if a < 0:
        print('Ошибка!Корень из отрицательного числа')
    else:
         return math.sqrt(a)
