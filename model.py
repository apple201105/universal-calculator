import math
import numpy as np
from datetime import datetime


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
def calculate_deposit(amount, rate, years):
     return amount * (1 + rate / 100) ** years


def linear_function(k, x):
    return k * x

def hyperbola(k, x):
    return k / x

def quadratic(a, b, c, x):
    return a * x**2 + b * x + c

def cubic(a, b, c, d, x):
    return a * x**3 + b * x**2 + c * x + d

history = []

def add_to_history(record):
    history.append(record)

def save_history_to_excel(filename="calculator_history.xlsx"):
    import pandas as pd
    df = pd.DataFrame(history,
                     columns=["Дата", "Имя", "Операция", "Параметры", "Результат"])
    df.to_excel(filename, index=False)
    return filename
def get_time():
    return datetime.now().strftime("%H:%M %d.%m.%Y")
