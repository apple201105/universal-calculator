def display_main_menu():
    print("\n╔══════════════════════════════╗")
    print("║       ГЛАВНОЕ МЕНЮ           ║")
    print("╠══════════════════════════════╣")
    print("║ 1 - Простой калькулятор      ║")
    print("║ 2 - Построение графиков      ║")
    print("║ 0 - Выход                    ║")
    print("╚══════════════════════════════╝")
    return input("Выберите действие: ")

def display_calc_menu():
    print("\n╔══════════════════════════════╗")
    print("║         КАЛЬКУЛЯТОР            ║")
    print("╠══════════════════════════════  ╣")
    print("║ + - сложение                   ║")
    print("║ - - вычитание                  ║")
    print("║ * - умножение                  ║")
    print("║ / - деление                    ║")
    print("║ ** - возведение а в степень b  ║")
    print("║ root - нахождение корня        ║")
    print("║ 0 - выход и сохранение в Excel ║")
    print("╚══════════════════════════════ ═╝")
    choice = input("Выберите действие: ")
    return choice

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

def get_numbers():
    print("\n════════ Ввод чисел ════════")
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    return a, b

def get_single_number():
    print("\n════════ Ввод числа ════════")
    a = float(input("Введите число: "))
    return a

def get_deposit_params():
    print("\n════════ Параметры вклада ════════")
    amount = float(input("Введите сумму вклада (руб): "))
    rate = float(input("Введите процентную ставку (% годовых): "))
    years = float(input("Введите срок вклада (лет): "))
    return amount, rate, years

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

def show_graph(title, x, y, label):
    import matplotlib.pyplot as plt
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label=label, color='blue')
    plt.title(title)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.legend()
    plt.show()
