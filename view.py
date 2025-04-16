import matplotlib.pyplot as plt
import numpy as np


def display_main_menu():
    print("\n╔══════════════════════════════╗")
    print("║       ГЛАВНОЕ МЕНЮ           ║")
    print("╠══════════════════════════════╣")
    print("║ 1 - Простой калькулятор      ║")
    print("║ 2 - Построение графиков      ║")
    print("║ 3 - Конвертер единиц         ║")
    print("║ 0 - Выход                    ║")
    print("╚══════════════════════════════╝")
    return input("Выберите действие: ")

def display_calc_menu():
    print("\n╔══════════════════════════════╗")
    print("║       КАЛЬКУЛЯТОР           ║")
    print("╠══════════════════════════════╣")
    print("║ + - сложение                 ║")
    print("║ - - вычитание                ║")
    print("║ * - умножение                ║")
    print("║ / - деление                  ║")
    print("║ ** - возведение в степень    ║")
    print("║ root - квадратный корень     ║")
    print("║ dep - расчет вклада          ║")
    print("║ 0 - назад                    ║")
    print("╚══════════════════════════════╝")
    return input("Выберите действие: ")


def display_graph_menu():
    print("\n╔══════════════════════════════╗")
    print("║    ВЫБЕРИТЕ ТИП ГРАФИКА      ║")
    print("╠══════════════════════════════╣")
    print("║ 1 - Прямая пропорциональность║")
    print("║ 2 - Гипербола                ║")
    print("║ 3 - Квадратная парабола      ║")
    print("║ 4 - Кубическая парабола      ║")
    print("║ 0 - Назад                    ║")
    print("╚══════════════════════════════╝")
    return input("Выберите тип графика: ")


def display_converter_menu():
    print("\n╔══════════════════════════════╗")
    print("║    КОНВЕРТЕР ЕДИНИЦ         ║")
    print("╠══════════════════════════════╣")
    print("║ 1 - Длина                    ║")
    print("║ 2 - Площадь                  ║")
    print("║ 3 - Объем                    ║")
    print("║ 4 - Время                    ║")
    print("║ 0 - Назад                    ║")
    print("╚══════════════════════════════╝")
    return input("Выберите тип конвертации: ")

def display_distance_units():
    print("\nДоступные единицы длины:")
    print("mm - миллиметры, cm - сантиметры")
    print("m - метры, km - километры")
    print("in - дюймы, ft - футы")
    print("yd - ярды, mi - мили")

def display_area_units():
    print("\nДоступные единицы площади:")
    print("mm² - квадратные миллиметры")
    print("cm² - квадратные сантиметры")
    print("m² - квадратные метры")
    print("km² - квадратные километры")
    print("ha - гектары")
    print("in² - квадратные дюймы")
    print("ft² - квадратные футы")
    print("ac - акры")

def display_volume_units():
    print("\nДоступные единицы объема:")
    print("ml - миллилитры")
    print("l - литры")
    print("m³ - кубические метры")
    print("cm³ - кубические сантиметры")
    print("in³ - кубические дюймы")
    print("ft³ - кубические футы")
    print("gal - галлоны")

def display_time_units():
    print("\nДоступные единицы времени:")
    print("ms - миллисекунды")
    print("s - секунды")
    print("min - минуты")
    print("h - часы")
    print("d - дни")
    print("wk - недели")

def get_conversion_input():
    value = float(input("Введите значение: "))
    from_unit = input("Из какой единицы: ").strip()
    to_unit = input("В какую единицу: ").strip()
    return value, from_unit, to_unit

def show_conversion_result(value, from_unit, converted_value, to_unit):
    print(f"\n{value} {from_unit} = {converted_value:.6f} {to_unit}")
    input("Нажмите Enter...")

def get_numbers():
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    return a, b


def get_single_number():
    return float(input("Введите число: "))


def get_deposit_params():
    amount = float(input("Сумма вклада: "))
    rate = float(input("Процентная ставка (%): "))
    years = float(input("Срок (лет): "))
    return amount, rate, years


def show_result(a, b, op, result):
    print(f"\n{a} {op} {b} = {result}" if b is not None else f"\n√{a} = {result}")
    input("Нажмите Enter...")


def show_deposit_result(amount, total):
    print(f"\nИтоговая сумма: {total:.2f}")
    print(f"Доход: {total - amount:.2f}")
    input("Нажмите Enter...")


def show_graph(title, x, y, label):
    plt.figure(figsize=(10, 6))
    ax = plt.gca()

    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.plot(1, 0, ">", transform=ax.get_yaxis_transform(), clip_on=False, color='darkred')
    ax.plot(0, 1, "^", transform=ax.get_xaxis_transform(), clip_on=False, color='darkred')
    ax.spines['left'].set_linewidth(1)
    ax.spines['bottom'].set_linewidth(1)
    ax.spines['left'].set_color('darkred')
    ax.spines['bottom'].set_color('darkred')
    
    ax.plot(x, y, 'b-', linewidth=2, label=label)

    ax.set_title(title, pad=20)
    ax.set_xlabel('X', loc='right', color='darkred')
    ax.set_ylabel('Y', loc='top', color='darkred')
    ax.grid(True, linestyle='--', alpha=0.7)
    ax.legend()

    plt.tight_layout()
    plt.show()


def show_message(msg):
    print(f"\n! {msg} !")


def get_user_name():
    return input("Введите ваше имя: ")
