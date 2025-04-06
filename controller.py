import pandas as pd
from datetime import datetime
from model import add, subtract, multiply, divide,exponentiation, root,calculate_deposit
from view import display_menu, get_numbers, show_result, show_message, get_user_name, get_single_number,get_deposit_params


class CalculatorController:
    def __init__(self):
        self.user_name = get_user_name()
        self.history = []

    def save_to_excel(self):
        df = pd.DataFrame(self.history, columns=["Дата", "Имя", "Операция", "Число1", "Число2", "Результат"])
        df.to_excel("calculator_history.xlsx", index=False)
        print(f"\nИстория операций сохранена в calculator_history.xlsx")

    def run(self):
        while True:
            choice = display_menu()

            if choice == "0":
                show_message(f"До свидания, {self.user_name}!")
                self.save_to_excel()
                break

            elif choice in ["+", "-", "*", "/","**"]:
                a, b = get_numbers()

                if choice == "+":
                    result = add(a, b)
                    operation = "+"
                elif choice == "-":
                    result = subtract(a, b)
                    operation = "-"
                elif choice == "*":
                    result = multiply(a, b)
                    operation = "*"
                elif choice == "/":
                    result = divide(a, b)
                    operation = "/"
                elif choice == "**":
                    result = exponentiation(a, b)
                    operation = "**"
                show_result(a, b, operation, result)

                self.history.append([
                    datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    self.user_name,
                    operation,
                    a,
                    b,
                    result
                ])
            elif choice == 'root':
                a = get_single_number()
                result = root(a)
                operation = "root"
                show_result(a, None, operation, result)
                self.history.append([
                    datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    self.user_name,
                    operation,
                    a,
                    None,
                    result
                ])
            elif choice.upper() == 'B':
                amount, rate, years = get_deposit_params()
                total_amount = calculate_deposit(amount, rate, years)
                income = total_amount - amount

                print("\n════════ Результат расчета вклада ════════")
                print(f"Сумма вклада: {amount:.2f} руб")
                print(f"Процентная ставка: {rate:.2f}%")
                print(f"Срок вклада: {years} лет")
                print(f"Итоговая сумма: {total_amount:.2f} руб")
                print(f"Доход: {income:.2f} руб")
                print("══════════════════════════════════════════")
                input("Нажмите Enter для продолжения...")

                self.history.append([
                    datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    self.user_name,
                    "Вклад",
                    f"Сумма: {amount} руб",
                    f"Ставка: {rate}%, Срок: {years} лет",
                    f"Итого: {total_amount:.2f} руб"
                ])



            else:
                show_message("Неверный выбор, попробуйте снова")


if __name__ == "__main__":
    calculator = CalculatorController()
    calculator.run()
