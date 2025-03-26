def display_menu():
    print("\n╔══════════════════════════════╗")
    print("║         КАЛЬКУЛЯТОР          ║")
    print("╠══════════════════════════════╣")
    print("║ + - сложение                 ║")
    print("║ - - вычитание                ║")
    print("║ * - умножение                ║")
    print("║ / - деление                  ║")
    print("║ 0 - выход и сохранение в Excel║")
    print("╚══════════════════════════════╝")
    choice = input("Выберите действие: ")
    return choice

def get_numbers():
    print("\n════════ Ввод чисел ════════")
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    return a, b
def get_single_number():
    print("\n════════ Ввод числа ════════")
    a = float(input("Введите число: "))
    return a
def show_result(a, b, operation, result):
    print("\n════════ Результат ════════")
    if operation == "root":
        print(f" √{a} = {result}")
    else:
         print(f" {a} {operation} {b} = {result}")
              
    print("═══════════════════════════")
    input("Нажмите клавишу Enter для возврата в меню")
def show_message(message):
    print(f"\n! {message} !")

def get_user_name():
    print("\n════════ Добро пожаловать! ════════")
    return input("Введите ваше имя: ")
