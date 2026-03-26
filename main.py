import tkinter as tk
from tkinter import messagebox

class Calculator(tk.Tk):
    def __init__(self, master):
        super().__init__()
        
        self.title("Simple Calculator")

        self.entry = tk.Entry(master, width=16, font=('Arial', 16), borderwidth=2, relief='ridge')
        self.entry.grid(row=0, column=0, columnspan=4)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        for i, button in enumerate(buttons):
            tk.Button(master, text=button, width=5, height=2, font=('Arial', 14),
                      command=lambda b=button: self.on_button_click(b)).grid(row=(i//4)+1, column=i%4)

    def on_button_click(self, char):
        if char == '=':
            try:
                result = eval(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                messagebox.showerror("Error", "Invalid expression")
                self.entry.delete(0, tk.END)
        else:
            self.entry.insert(tk.END, char)



if __name__ == "__main__":
    app = Calculator(None)
    app.mainloop()
    
# i will change full entire code in future but for now this is the code for very very simple calculator.