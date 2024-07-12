import tkinter as tk
from tkinter import messagebox
import math

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(screen.get())
            screen.delete(0, tk.END)
            screen.insert(tk.END, str(result))
        except Exception as e:
            messagebox.showerror("Error", "Invalid Input")
    elif text == "C":
        screen.delete(0, tk.END)
    elif text == "√":
        try:
            result = math.sqrt(float(screen.get()))
            screen.delete(0, tk.END)
            screen.insert(tk.END, str(result))
        except Exception as e:
            messagebox.showerror("Error", "Invalid Input")
    elif text == "^":
        screen.insert(tk.END, "**")
    else:
        screen.insert(tk.END, text)

root = tk.Tk()
root.title("Scientific Calculator")

screen = tk.Entry(root, font="lucida 20 bold")
screen.pack(fill=tk.BOTH, ipadx=8)

button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    "7", "8", "9", "/", "C",
    "4", "5", "6", "*", "(",
    "1", "2", "3", "-", ")",
    "0", ".", "=", "+", "^",
    "sin", "cos", "tan", "√", "log"
]

row = 0
col = 0

for button in buttons:
    btn = tk.Button(button_frame, text=button, font="lucida 15 bold")
    btn.grid(row=row, column=col, padx=10, pady=10)
    btn.bind("<Button-1>", click)
    col += 1
    if col == 5:
        row += 1
        col = 0

root.mainloop()
