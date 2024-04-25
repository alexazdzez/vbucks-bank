from tkinter import *


def valider(id, mdp):
    print("test")


def connecter():
    root = Tk()
    root.title("connection")
    root.geometry("500x500")
    root.minsize(480, 360)
    root.config(background='#3F3F3F')
    frame = Frame(root, bg='#3F3F3F')

    id = StringVar()
    mdp = StringVar()

    champ_id = Entry(frame, textvariable=id)
    champ_id.pack()

    champ_mdp = Entry(frame, textvariable=mdp)
    champ_mdp.pack()

    yt_button = Button(frame, text="valider", font=("Courrier", 15), bg='gray', fg='#3F3F3F', command=lambda: valider(id, mdp))
    yt_button.pack(pady=25)
    frame.pack(expand=YES)

    root.mainloop()
