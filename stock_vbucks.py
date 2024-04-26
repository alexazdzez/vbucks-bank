from tkinter import *
import save_vbucks


class Compte:
    def __init__(self, id):
        # root window
        self.mdp = id
        self.root = Tk()
        self.root.geometry("500x300")
        self.root.title('bank')
        self.frame_code = Frame(self.root)
        self.frame_v_bucks = Frame(self.root)

        # legende
        self.code_label = Label(self.frame_code, text="code")
        self.code_label.pack()

        self.number_v_bucks_label = Label(self.frame_v_bucks, text="nombre  v-bucks")
        self.number_v_bucks_label.pack()
        # code

        self.code = Entry(self.frame_code)
        self.code.pack()

        self.v_bucks = Entry(self.frame_v_bucks)
        self.v_bucks.pack()

        #boutons
        self.frame_buttons = Frame(self.root)
        self.button = Button(self.frame_buttons, text="ajouter", command=self.ajouter)
        self.button.pack(side=BOTTOM)
        self.button_save = Button(self.frame_buttons, text="enregistrer", command=self.save)
        self.button_save.pack(side=BOTTOM)
        self.button_read = Button(self.frame_buttons, text="lire", command=self.read)
        self.button_read.pack(side=BOTTOM)

        self.frame_buttons.pack(side=BOTTOM)
        self.frame_code.pack(side=LEFT)
        self.frame_v_bucks.pack(side=RIGHT)
        self.root.mainloop()

    def ajouter(self):
        label = Label(self.root, text="code: " + self.code.get() + " nombre de v-bucks: " + self.v_bucks.get())
        label.pack()

    def save(self):
        save_vbucks.add_vucks(self.mdp, self.code.get())

    def read(self):
        save_vbucks.read_vbucks(self.mdp)
