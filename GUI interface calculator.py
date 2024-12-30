import tkinter as tk
from tkinter import messagebox
def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + value)

def evaluate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        messagebox.showerror("Error", "Invalid Input")

def clear():
    entry.delete(0, tk.END)


window = tk.Tk()
window.title("Calculator")

# Entry widget for the display
entry = tk.Entry(window, width=30, borderwidth=5, font=("Arial", 16), justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

# Create buttons and add them to the window
for text, row, col in buttons:
    if text == "=":
        button = tk.Button(window, text=text, width=10, height=2, font=("Arial", 14),
                           command=evaluate)
    elif text == "C":
        button = tk.Button(window, text=text, width=10, height=2, font=("Arial", 14),
                           command=clear)
    else:
        button = tk.Button(window, text=text, width=10, height=2, font=("Arial", 14),
                           command=lambda t=text: button_click(t))
    button.grid(row=row, column=col, padx=5, pady=5)

# Run the application
window.mainloop()




