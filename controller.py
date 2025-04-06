from datetime import datetime
from model import *
from view import *


def run_simple_calculator(user_name):
    while True:
        operation = display_calc_menu()

        if operation == '0':
            break
        if operation in ['+', '-', '*', '/', '**']:
            a, b = get_numbers()
            if operation == '+':
                result = add(a, b)
            elif operation == '-':
                result = subtract(a, b)
            elif operation == '*':
                result = multiply(a, b)
            elif operation == '/':
                result = divide(a, b)
            elif operation == '**':
                result = exponentiation(a, b)
            show_result(a, b, operation, result)
            add_to_history([get_time() ,user_name,operation,f"{a}, {b}",result])
        elif operation == 'root':
            a = get_single_number()
            result = root(a)
            show_result(a, None, '√', result)
            add_to_history([get_time() , user_name, '√',str(a),result])
        elif operation == 'dep':
            amount, rate, years = get_deposit_params()
            total = calculate_deposit(amount, rate, years)
            show_deposit_result(amount, total)
            add_to_history([ get_time(),user_name,'Вклад',f"{amount} руб, {rate}%, {years} лет", f"{total:.2f} руб"])
        else:
            show_message("Неверная операция")


def run_graph_calculator(user_name):
    while True:
        choice = display_graph_menu()
        if choice == '0':
            break
        x = np.linspace(-10, 10, 400)
        if choice == '1':
            k = float(input("Коэффициент k: "))
            y = linear_function(k, x)
            show_graph(f"y = {k}x", x, y, f"y = {k}x")
            add_to_history([ get_time() , user_name, "График: прямая",f"k = {k}","Построен график"])
        elif choice == '2':
            k = float(input("Коэффициент k: "))
            x = x[x != 0]
            y = hyperbola(k, x)
            show_graph(f"y = {k}/x", x, y, f"y = {k}/x")
            add_to_history([ get_time(), user_name,"График: гипербола", f"k = {k}","Построен график"])
        elif choice == '3':
            a = float(input("a: "))
            b = float(input("b: "))
            c = float(input("c: "))
            y = quadratic(a, b, c, x)
            show_graph(f"y = {a}x² + {b}x + {c}", x, y, f"y = {a}x² + {b}x + {c}")
            add_to_history([get_time() ,user_name,"График: парабола", f"a={a}, b={b}, c={c}","Построен график"])
        elif choice == '4':
            a = float(input("a: "))
            b = float(input("b: "))
            c = float(input("c: "))
            d = float(input("d: "))
            y = cubic(a, b, c, d, x)
            show_graph(f"y = {a}x³ + {b}x² + {c}x + {d}", x, y, f"y = {a}x³ + {b}x² + {c}x + {d}")
            add_to_history([get_time(),user_name, "График: кубическая",f"a={a}, b={b}, c={c}, d={d}", "Построен график"])
        else:
            show_message("Неверный выбор")


def run_calculator():
    user_name = get_user_name()

    while True:
        choice = display_main_menu()
        if choice == '0':
            filename = save_history_to_excel()
            show_message(f"До свидания, {user_name}! История сохранена в {filename}")
            break
        elif choice == '1':
            run_simple_calculator(user_name)
        elif choice == '2':
            run_graph_calculator(user_name)
        else:
            show_message("Неверный выбор")


if __name__ == "__main__":
    run_calculator()
