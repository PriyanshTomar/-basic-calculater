import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Basic Calculator")
        self.geometry("300x400")

        self.current_number = ''
        self.previous_number = ''
        self.operator = ''

        self.display = tk.Entry(self, font=("Arial", 24), bd=10, insertwidth=2, width=14, borderwidth=4)
        self.display.grid(row=0, column=0, columnspan=4)

        buttons = [
            'C', '←', '/', '*',
            '7', '8', '9', '-',
            '4', '5', '6', '+',
            '1', '2', '3', '=',
            '0', '.'
        ]

        row = 1
        col = 0
        for button in buttons:
            if button == '0':
                tk.Button(self, text=button, padx=20, pady=20, font=("Arial", 18), command=lambda b=button: self.append_number(b)).grid(row=row, column=col, columnspan=2)
                col += 2
            else:
                tk.Button(self, text=button, padx=20, pady=20, font=("Arial", 18), command=lambda b=button: self.on_button_click(b)).grid(row=row, column=col)
                col += 1
            if col > 3:
                col = 0
                row += 1

    def on_button_click(self, button):
        if button == 'C':
            self.clear_all()
        elif button == '←':
            self.backspace()
        elif button in ['+', '-', '*', '/']:
            self.set_operator(button)
        elif button == '=':
            self.calculate_result()
        else:
            self.append_number(button)

    def clear_all(self):
        self.current_number = ''
        self.previous_number = ''
        self.operator = ''
        self.display.delete(0, tk.END)

    def backspace(self):
        self.current_number = self.current_number[:-1]
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.current_number)

    def set_operator(self, op):
        if self.current_number == '':
            return
        if self.previous_number != '':
            self.calculate_result()
        self.operator = op
        self.previous_number = self.current_number
        self.current_number = ''
        self.display.delete(0, tk.END)

    def calculate_result(self):
        if self.previous_number == '' or self.current_number == '' or self.operator == '':
            return

        num1 = float(self.previous_number)
        num2 = float(self.current_number)

        if self.operator == '/' and num2 == 0:
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, 'Error')
            self.clear_all()
            return

        result = 0
        if self.operator == '+':
            result = num1 + num2
        elif self.operator == '-':
            result = num1 - num2
        elif self.operator == '*':
            result = num1 * num2
        elif self.operator == '/':
            result = num1 / num2

        self.display.delete(0, tk.END)
        self.display.insert(tk.END, str(result))
        self.current_number = str(result)
        self.previous_number = ''
        self.operator = ''

    def append_number(self, num):
        if num == '.' and '.' in self.current_number:
            return
        self.current_number += num
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.current_number)

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
