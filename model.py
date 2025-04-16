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



def convert_distance(value, from_unit, to_unit):
    units = {
        'mm': 0.001,
        'cm': 0.01,
        'm': 1,
        'km': 1000,
        'in': 0.0254,
        'ft': 0.3048,
        'yd': 0.9144,
        'mi': 1609.34
    }
    return value * units[from_unit] / units[to_unit]

def convert_area(value, from_unit, to_unit):
    units = {
        'mm²': 1e-6,
        'cm²': 1e-4,
        'm²': 1,
        'km²': 1e6,
        'ha': 1e4,
        'in²': 0.00064516,
        'ft²': 0.092903,
        'ac': 4046.86
    }
    return value * units[from_unit] / units[to_unit]

def convert_volume(value, from_unit, to_unit):
    units = {
        'ml': 1e-6,
        'l': 0.001,
        'm³': 1,
        'cm³': 1e-6,
        'in³': 1.63871e-5,
        'ft³': 0.0283168,
        'gal': 0.00378541
    }
    return value * units[from_unit] / units[to_unit]

def convert_time(value, from_unit, to_unit):
    units = {
        'ms': 0.001,
        's': 1,
        'min': 60,
        'h': 3600,
        'd': 86400,
        'wk': 604800
    }
    return value * units[from_unit] / units[to_unit]
