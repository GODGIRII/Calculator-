import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Basic Calculator")
root.resizable(False, False)

# Input field
entry = tk.Entry(root, width=16, font=("Arial", 24), borderwidth=2, relief="ridge", justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Function to handle button press
def on_button_click(char):
    if char == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(0, str(result))
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(0, "Error")
    else:
        entry.insert(tk.END, char)

# Button layout (text, row, column)
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

# Create buttons and place them on the grid
for (text, row, col) in buttons:
    button = tk.Button(root, text=text, width=4, height=2, font=("Arial", 18),
                       command=lambda char=text: on_button_click(char))
    button.grid(row=row, column=col, padx=5, pady=5)

# Clear button
clear_btn = tk.Button(root, text="C", width=18, height=2, font=("Arial", 18),
                      command=lambda: entry.delete(0, tk.END))
clear_btn.grid(row=5, column=0, columnspan=4, padx=5, pady=5)

# Start the app
root.mainloop()

