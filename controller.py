import pandas as pd
from datetime import datetime
from model import add,subtract,multiply,divide
from view import display_menu,get_numbers,show_result,show_message,get_user_name

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

            elif choice in ["+", "-", "*", "/"]:
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
                    result = exponentiation(a,b)
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

            else:
                show_message("Неверный выбор, попробуйте снова")


if __name__ == "__main__":
    calculator = CalculatorController()
    calculator.run()
