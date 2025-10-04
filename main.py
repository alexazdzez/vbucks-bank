from customtkinter import CTk, CTkFrame, CTkLabel, CTkEntry, CTkButton
from tkinter import StringVar, Menu, Canvas
import stock
import webbrowser

class InscriptionFrame(CTkFrame):
    def __init__(self, master, switch_callback, **kwargs):
        super().__init__(master, fg_color="#0A0A0A", corner_radius=25, **kwargs)
        self.id_var = StringVar()
        self.mdp_var = StringVar()

        CTkLabel(self, text="Inscription", font=("Arial", 28, "bold"), text_color="#FFFFFF").pack(pady=(30,20))
        CTkLabel(self, text="Identifiant", font=("Arial", 18), text_color="#AAAAAA").pack(pady=(5,5))
        CTkEntry(self, textvariable=self.id_var, placeholder_text="email@gmail.com",
                 fg_color="#0F0F0F", text_color="#FFFFFF", border_color="#555555", corner_radius=12,
                 width=400).pack(pady=5)

        CTkLabel(self, text="Mot de passe", font=("Arial", 18), text_color="#AAAAAA").pack(pady=(15,5))
        CTkEntry(self, textvariable=self.mdp_var, show="*", placeholder_text="••••••••",
                 fg_color="#0F0F0F", text_color="#FFFFFF", border_color="#555555", corner_radius=12,
                 width=400).pack(pady=5)

        CTkButton(self, text="S'inscrire", command=self.inscrire,
                  fg_color="#222222", hover_color="#333333", text_color="#FFFFFF", width=200).pack(pady=20)

        CTkButton(self, text="Déjà un compte ? Se connecter", command=switch_callback,
                  fg_color="#111111", hover_color="#222222", text_color="#AAAAAA").pack(pady=10)

    def inscrire(self):
        if len(self.mdp_var.get()) >= 6:
            stock.add(self.id_var.get(), self.mdp_var.get())
        else:
            print("Mot de passe trop court")

class ConnexionFrame(CTkFrame):
    def __init__(self, master, switch_callback, **kwargs):
        super().__init__(master, fg_color="#0A0A0A", corner_radius=25, **kwargs)
        self.id_var = StringVar()
        self.mdp_var = StringVar()

        CTkLabel(self, text="Connexion", font=("Arial", 28, "bold"), text_color="#FFFFFF").pack(pady=(30,20))
        CTkLabel(self, text="Identifiant", font=("Arial", 18), text_color="#AAAAAA").pack(pady=(5,5))
        CTkEntry(self, textvariable=self.id_var, placeholder_text="email@gmail.com",
                 fg_color="#0F0F0F", text_color="#FFFFFF", border_color="#555555", corner_radius=12,
                 width=400).pack(pady=5)

        CTkLabel(self, text="Mot de passe", font=("Arial", 18), text_color="#AAAAAA").pack(pady=(15,5))
        CTkEntry(self, textvariable=self.mdp_var, show="*", placeholder_text="••••••••",
                 fg_color="#0F0F0F", text_color="#FFFFFF", border_color="#555555", corner_radius=12,
                 width=400).pack(pady=5)

        CTkButton(self, text="Se connecter", command=self.connecter,
                  fg_color="#222222", hover_color="#333333", text_color="#FFFFFF", width=200).pack(pady=20)

        CTkButton(self, text="Pas de compte ? S'inscrire", command=switch_callback,
                  fg_color="#111111", hover_color="#222222", text_color="#AAAAAA").pack(pady=10)

    def connecter(self):
        stock.connect(self.id_var.get(), self.mdp_var.get())

class App(CTk):
    def __init__(self):
        super().__init__()
        self.title("v-bucks bank")
        self.geometry("1080x720")
        self.minsize(800, 600)
        self.configure(fg_color="#0F0F0F")
        self.iconbitmap("source/icon.ico")


        frame_top = CTkFrame(master=self, height=140, fg_color="#1A1A1A", corner_radius=15)
        frame_top.pack(fill="x", side="top", padx=20, pady=20)
        CTkLabel(frame_top, text="Banque v-bucks", font=("Arial", 36, "bold"), text_color="#FFFFFF").pack(expand=True)


        self.canvas = Canvas(self, width=600, height=500, bg="#050505", highlightthickness=0)
        self.canvas.pack(pady=10, expand=True)

        self.inscription_frame = InscriptionFrame(self.canvas, self.show_connexion, width=600, height=500)
        self.connexion_frame = ConnexionFrame(self.canvas, self.show_inscription, width=600, height=500)

        self.current_window = self.canvas.create_window(300, 250, window=self.inscription_frame)


        frame_bottom = CTkFrame(master=self, height=80, fg_color="#1A1A1A", corner_radius=15)
        frame_bottom.pack(fill="x", side="bottom", padx=20, pady=(0,20))
        CTkLabel(frame_bottom, text="® Mvivibe Inc.", font=("Arial", 16), text_color="#AAAAAA").pack(side="left", padx=20)
        CTkButton(frame_bottom, text="Notre Site", command=lambda: webbrowser.open_new("https://mvivibe.fr"),
                  fg_color="#333333", hover_color="#444444", text_color="#FFFFFF").pack(side="right", padx=20)


        menu_bar = Menu(self)
        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Explore", command=lambda: webbrowser.open_new("https://www.youtube.com/watch?v=dQw4w9WgXcQ"))
        file_menu.add_command(label="Quitter", command=self.quit)
        menu_bar.add_cascade(label="Fichier", menu=file_menu)
        self.config(menu=menu_bar)

    def show_connexion(self):
        self.animate_flip(self.inscription_frame, self.connexion_frame)

    def show_inscription(self):
        self.animate_flip(self.connexion_frame, self.inscription_frame)

    def animate_flip(self, frame_out, frame_in, steps=10, delay=30):

        def shrink(i):
            if i <= steps:
                scale = max(1 - i / steps, 0.01)  # <-- jamais 0
                self.canvas.scale(self.current_window, 300, 250, scale, 1)
                self.after(delay, lambda: shrink(i + 1))
            else:
                self.canvas.delete(self.current_window)
                self.current_window = self.canvas.create_window(300, 250, window=frame_in)
                expand(0)

        def expand(i):
            if i <= steps:
                scale = max(i / steps, 0.01)  # <-- jamais 0
                self.canvas.scale(self.current_window, 300, 250, scale, 1)
                self.after(delay, lambda: expand(i + 1))

        shrink(0)


if __name__ == "__main__":
    app = App()
    app.mainloop()