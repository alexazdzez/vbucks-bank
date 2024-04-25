from tkinter import *

def v_bucks():
    root = Tk()
    root.title("v-bucks")
    root.geometry("500x350")
    root.minsize(480, 360)
    root.iconbitmap("source/icon.ico")
    root.config(background='#3F3F3F')

    # créer frame
    frame_center = Frame(root, bg='#3F3F3F')

    # titre (texte)
    label_title = Label(frame_center, text="v-bucks", font=("Arial", 25), bg='#3F3F3F', fg='gray')
    label_title.pack(side=TOP)

    frame_center.pack(expand=YES)

    # menu
    menu_bar = Menu(root)

    file_menu = Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="Quitter", command=root.quit)

    menu_bar.add_cascade(label="Fichier", menu=file_menu)
    root.config(menu=menu_bar)

    root.mainloop()
