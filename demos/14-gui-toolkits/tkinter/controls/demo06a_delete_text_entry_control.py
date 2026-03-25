import tkinter as tk


def clear_text_input():
    txt.delete(0, tk.END)


main_window = tk.Tk()
main_window.title("Demo Delete Text from Entry Control")
main_window.geometry("400x240")

txt = tk.Entry(main_window, width=30)
txt.pack()

btn_read = tk.Button(
    main_window, height=1, width=10, text="Clear", command=clear_text_input
)
btn_read.pack()

main_window.mainloop()
