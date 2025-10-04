from customtkinter import CTk, CTkFrame, CTkLabel, CTkEntry, CTkButton, CTkScrollableFrame
import requests
from tkinter import messagebox

API_URL_ADD = "https://mvivibe.fr:5003/giftcards/add"
API_URL_LIST = "https://mvivibe.fr:5003/giftcards/{}"

class CompteApp(CTk):
    def __init__(self, user_id):
        super().__init__()
        self.user_id = user_id
        self.title("V-Bucks Bank")
        self.geometry("600x500")
        self.configure(fg_color="#0F0F0F")
        self.iconbitmap("source/icon.ico")

        CTkLabel(self, text="Gestion des V-Bucks", font=("Arial", 24, "bold"), text_color="#FFFFFF").pack(pady=10)


        frame_add = CTkFrame(self, fg_color="#1A1A1A", corner_radius=15)
        frame_add.pack(padx=20, pady=10, fill="x")

        CTkLabel(frame_add, text="Code V-Bucks", text_color="#FFFFFF").grid(row=0, column=0, sticky="w", pady=5)
        self.entry_code = CTkEntry(frame_add, width=300, placeholder_text="Entrez le code",
                                   fg_color="#0F0F0F", text_color="#FFFFFF", border_color="#555555")
        self.entry_code.grid(row=0, column=1, padx=10, pady=5)

        CTkLabel(frame_add, text="Nom / Description", text_color="#FFFFFF").grid(row=1, column=0, sticky="w", pady=5)
        self.entry_name = CTkEntry(frame_add, width=300, placeholder_text="Nom ou description",
                                   fg_color="#0F0F0F", text_color="#FFFFFF", border_color="#555555")
        self.entry_name.grid(row=1, column=1, padx=10, pady=5)

        CTkButton(frame_add, text="Ajouter", command=self.add_vbucks,
                  fg_color="#333333", hover_color="#444444", text_color="#FFFFFF").grid(row=2, column=0, columnspan=2, pady=10)


        self.frame_list = CTkScrollableFrame(self, fg_color="#1A1A1A", corner_radius=15)
        self.frame_list.pack(padx=20, pady=10, fill="both", expand=True)

        CTkButton(self, text="Actualiser la liste", command=self.refresh_list,
                  fg_color="#333333", hover_color="#444444", text_color="#FFFFFF").pack(pady=10)

        self.refresh_list()

    def add_vbucks(self):
        code = self.entry_code.get().strip()
        name = self.entry_name.get().strip()
        if not code:
            messagebox.showwarning("Erreur", "Le code ne peut pas être vide")
            return

        data = {"user_id": self.user_id, "code": code, "name": name}
        try:
            response = requests.post(API_URL_ADD, json=data)
            if response.status_code == 201:
                messagebox.showinfo("Succès", "Code ajouté !")
                self.entry_code.delete(0, "end")
                self.entry_name.delete(0, "end")
                self.refresh_list()
            else:
                messagebox.showerror("Erreur", response.json().get("error", "Erreur inconnue"))
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Erreur réseau", str(e))

    def refresh_list(self):

        for widget in self.frame_list.winfo_children():
            widget.destroy()

        try:
            response = requests.get(API_URL_LIST.format(self.user_id))
            if response.status_code == 200:
                cards = response.json()
                if not cards:
                    CTkLabel(self.frame_list, text="Aucun code enregistré.", text_color="#FFFFFF").pack(pady=5)
                    return
                for c in cards:
                    CTkLabel(self.frame_list, text=f"{c['code']} - {c['name']}", text_color="#FFFFFF",
                             anchor="w").pack(fill="x", padx=10, pady=2)
            else:
                CTkLabel(self.frame_list, text="Impossible de récupérer la liste.", text_color="#FF5555").pack()
        except requests.exceptions.RequestException as e:
            CTkLabel(self.frame_list, text=f"Erreur réseau : {e}", text_color="#FF5555").pack()