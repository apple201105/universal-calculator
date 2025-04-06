import matplotlib as plt
import pandas as pd
from datetime import datetime
from model import *
from view import *


def run_calculator():
    user_name = get_user_name()

    while True:
        choice = display_main_menu()

        if choice == "0":
            show_message(f"До свидания, {user_name}!")
            save_history_to_excel("calculator_history.xlsx")
            break

        elif choice == "1":
            run_simple_calculator(user_name)

        elif choice == "2":
            run_graph_calculator(user_name)

        else:
            show_message("Неверный выбор, попробуйте снова")


def run_simple_calculator(user_name):
    while True:
        operation = display_calc_menu()

        if operation == "0":
            break

        elif operation in ["+", "-", "*", "/", "**"]:
            a, b = get_numbers()

            if operation == "+":
                result = add(a, b)
            elif operation == "-":
                result = subtract(a, b)
            elif operation == "*":
                result = multiply(a, b)
            elif operation == "/":
                result = divide(a, b)
            elif operation == "**":
                result = exponentiation(a, b)

            show_result(a, b, operation, result)
            add_to_history([
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                user_name,
                operation,
                f"{a}, {b}",
                result
            ])

        elif operation == "root":
            a = get_single_number()
            result = root(a)
            show_result(a, None, "root", result)
            add_to_history([
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                user_name,
                "root",
                str(a),
                result
            ])

        else:
            show_message("Неверный выбор, попробуйте снова")


def run_graph_calculator(user_name):
    while True:
        choice = display_graph_menu()

        if choice == "0":
            break

        x = np.linspace(-10, 10, 400)

        if choice == "1":
            k = float(input("Введите коэффициент k для y = kx: "))
            y = linear_function(k, x)
            show_graph(f"Прямая пропорциональность y = {k}x", x, y, f"y = {k}x")
            add_to_history([
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                user_name,
                "График: прямая",
                f"k = {k}",
                "Построен график"
            ])

        elif choice == "2":
            k = float(input("Введите коэффициент k для y = k/x: "))
            x = np.linspace(-10, 10, 400)
            x = x[x != 0]  # Исключаем 0, чтобы избежать деления на 0
            y = hyperbola(k, x)
            show_graph(f"Гипербола y = {k}/x", x, y, f"y = {k}/x")
            add_to_history([
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                user_name,
                "График: гипербола",
                f"k = {k}",
                "Построен график"
            ])

        elif choice == "3":
            a = float(input("Введите коэффициент a: "))
            b = float(input("Введите коэффициент b: "))
            c = float(input("Введите коэффициент c: "))
            y = quadratic(a, b, c, x)
            show_graph(f"Квадратная парабола y = {a}x² + {b}x + {c}", x, y,
                       f"y = {a}x² + {b}x + {c}")
            add_to_history([
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                user_name,
                "График: парабола",
                f"a = {a}, b = {b}, c = {c}",
                "Построен график"
            ])

        elif choice == "4":
            a = float(input("Введите коэффициент a: "))
            b = float(input("Введите коэффициент b: "))
            c = float(input("Введите коэффициент c: "))
            d = float(input("Введите коэффициент d: "))
            y = cubic(a, b, c, d, x)
            show_graph(f"Кубическая парабола y = {a}x³ + {b}x² + {c}x + {d}",
                       x, y, f"y = {a}x³ + {b}x² + {c}x + {d}")
            add_to_history([
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                user_name,
                "График: кубическая",
                f"a = {a}, b = {b}, c = {c}, d = {d}",
                "Построен график"
            ])

        else:
            show_message("Неверный выбор, попробуйте снова")


if __name__ == "__main__":
    run_calculator()
