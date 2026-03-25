import tkinter as tk

main_window = tk.Tk()


def handle_click_left(event):
    print("Left button was clicked!")


def handle_click_right(event):
    print("Right button was clicked!")


btn = tk.Button(main_window, text="Click Me")
btn.grid(column=0, row=1)
btn.bind("<Button-1>", handle_click_left)
btn.bind("<Button-3>", handle_click_right)

main_window.mainloop()
