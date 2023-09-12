import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Kalkulator")
        self.root.resizable(False, False)

        self.entry = tk.Entry(self.root, width=30)
        self.entry.pack()

        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack()

        self.buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '+'
        ]

        self.create_buttons()

        self.calc_button = tk.Button(self.root, text="Oblicz", width=30, command=self.calculate)
        self.calc_button.pack()

        self.result_label = tk.Label(self.root, text="Wynik: ")
        self.result_label.pack()

    def create_buttons(self):
        row = 0
        col = 0

        for button in self.buttons:
            tk.Button(self.button_frame, text=button, width=5, command=lambda button=button: self.entry.insert(tk.END, button)).grid(row=row, column=col)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def calculate(self):
        try:
            expression = self.entry.get()
            result = eval(expression)
            self.result_label.config(text="Wynik: " + str(result))
        except Exception as e:
            self.result_label.config(text="Błąd: " + str(e))

root = tk.Tk()
calculator = Calculator(root)
root.mainloop()
