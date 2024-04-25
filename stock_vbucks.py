from tkinter import *

def v_bucks():

    # root window
    root = Tk()
    root.geometry("500x300")
    root.title('Login')

    # configure the grid
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=3)

    # username
    code_label = Label(root, text="code")
    code_label.grid(column=0, row=0, sticky=W, padx=5, pady=5)

    number_v_bucks_label = Label(root, text="nombre v-bucks")
    number_v_bucks_label.grid(column=1, row=0, sticky=E, padx=5, pady=5)

    # password
    code_1_label = Label(root, text="1111111")
    code_1_label.grid(column=0, row=1, sticky=W, padx=5, pady=5)

    v_bucks_1 = Label(root, text="1000")
    v_bucks_1.grid(column=1, row=1, sticky=E, padx=5, pady=5)

    root.mainloop()