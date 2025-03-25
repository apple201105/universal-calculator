def display_menu():
    print("\n╔══════════════════════════════╗")
    print("║         КАЛЬКУЛЯТОР         ║")
    print("╠══════════════════════════════╣")
    print("║ + - сложение                 ║")
    print("║ - - вычитание                ║")
    print("║ * - умножение                ║")
    print("║ / - деление                  ║")
    print("║ 0 - выход                    ║")
    print("╚══════════════════════════════╝")
    choice = input("Выберите действие: ")
    return choice

def get_numbers():
    print("\n════════ Ввод чисел ════════")
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    return a, b

def show_result(a, b, operation, result):
    print("\n════════ Результат ════════")
    print(f" {a} {operation} {b} = {result}")
    print("═══════════════════════════")

def show_message(message):
    print(f"\n! {message} !")

def get_user_name():
    print("\n════════ Добро пожаловать! ════════")
    return input("Введите ваше имя: ")