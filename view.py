def display_main_menu():
    print("\n╔═══════════════════════════════╗")
    print("║       ГЛАВНОЕ МЕНЮ             ║")
    print("╠════════════════════════════════╣")
    print("║ 1 - Простой калькулятор        ║")
    print("║ 2 - Построение графиков        ║")
    print("║ 0 - Выход и сохранение в Excel ║")
    print("╚════════════════════════════════╝")
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

def show_deposit_result(amount, total):
    print(f"\nИтоговая сумма: {total:.2f}")
    print(f"Доход: {total - amount:.2f}")
    input("Нажмите Enter...")

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
    plt.figure(figsize=(10, 7))
    ax = plt.gca()

    
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')

  
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)

    
    ax.spines['left'].set_linewidth(2.5)
    ax.spines['bottom'].set_linewidth(2.5)
    ax.spines['left'].set_color('#FF4500')  # Оранжево-красный
    ax.spines['bottom'].set_color('#FF4500')

    
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.tick_params(axis='both', which='major', width=2, colors='#FF4500', size=6)


    plt.plot(x, y, label=label, color='#1E90FF', linewidth=2.5)  # Синий dodger

  
    ax.plot(1, 0, ">", transform=ax.get_yaxis_transform(), clip_on=False, color='#FF4500')
    ax.plot(0, 1, "^", transform=ax.get_xaxis_transform(), clip_on=False, color='#FF4500')

    
    ax.set_xlabel('Ось X', fontsize=12, color='#FF4500', loc='right')
    ax.set_ylabel('Ось Y', fontsize=12, color='#FF4500', loc='top')

   
    plt.title(title, fontsize=14, pad=20)
    plt.grid(True, linestyle='--', alpha=0.6, color='gray')

 
    plt.legend(framealpha=1, frameon=True, edgecolor='black')

   
    plt.margins(0.1)

    plt.tight_layout()
    plt.show()

