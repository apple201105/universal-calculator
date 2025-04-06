import pandas as pd
from datetime import datetime
from model import *
from view import *


def save_history():
    df = pd.DataFrame(history, columns=["Дата", "Имя", "Операция", "Параметры", "Результат"])
    df.to_excel("calculator_history.xlsx", index=False)
    print("История сохранена")


def simple_calculator(user_name):
    while True:
        op = display_calc_menu()

        if op == '0':
            break

        if op in ['+', '-', '*', '/', '**']:
            a, b = get_numbers()
            result = globals()[{'**': 'exponentiation'}.get(op, op)](a, b)
            show_result(a, b, op, result)
            history.append([datetime.now(), user_name, op, f"{a}, {b}", result])

        elif op == '√':
            a = get_single_number()
            result = root(a)
            show_result(a, None, '√', result)
            history.append([datetime.now(), user_name, '√', str(a), result])

        elif op == 'dep':
            amount, rate, years = get_deposit_params()
            total = calculate_deposit(amount, rate, years)
            show_deposit_result(amount, total)
            history.append([datetime.now(), user_name, 'Вклад',
                            f"{amount} руб, {rate}%, {years} лет", f"{total:.2f} руб"])

        else:
            show_message("Неверная операция")


def graph_calculator(user_name):
    while True:
        choice = display_graph_menu()
        if choice == '0':
            break

        x = np.linspace(-10, 10, 400)
        if choice == '1':
            k = float(input("Коэффициент k: "))
            y = linear_function(k, x)
            show_graph(f"y = {k}x", x, y, f"y = {k}x")

        elif choice == '2':
            k = float(input("Коэффициент k: "))
            x = x[x != 0]
            y = hyperbola(k, x)
            show_graph(f"y = {k}/x", x, y, f"y = {k}/x")

        elif choice == '3':
            a = float(input("a: "))
            b = float(input("b: "))
            c = float(input("c: "))
            y = quadratic(a, b, c, x)
            show_graph(f"y = {a}x² + {b}x + {c}", x, y, f"y = {a}x² + {b}x + {c}")

        elif choice == '4':
            a = float(input("a: "))
            b = float(input("b: "))
            c = float(input("c: "))
            d = float(input("d: "))
            y = cubic(a, b, c, d, x)
            show_graph(f"y = {a}x³ + {b}x² + {c}x + {d}", x, y, f"y = {a}x³ + {b}x² + {c}x + {d}")

        else:
            show_message("Неверный выбор")


def main():
    user_name = get_user_name()

    while True:
        choice = display_main_menu()

        if choice == '0':
            show_message(f"До свидания, {user_name}!")
            save_history()
            break

        elif choice == '1':
            simple_calculator(user_name)

        elif choice == '2':
            graph_calculator(user_name)

        else:
            show_message("Неверный выбор")


if __name__ == "__main__":
    main()
