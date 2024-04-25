from tkinter import *
import webbrowser


def open_zertou_frais_chanel():
    webbrowser.open_new("https://www.youtube.com/channel/UCFLeKci8Um3O9ZNcchvSW3A")


def rick_roll():
    webbrowser.open_new("https://www.youtube.com/watch?v=dQw4w9WgXcQ")


                                                                        # base de la fenetre
root = Tk()
root.title("v-bucks bank")
root.geometry("1080x720")
root.minsize(480, 360)
root.iconbitmap("source/icon.ico")
root.config(background='#3F3F3F')

                                                                        # créer frame
frame_center = Frame(root, bg='#3F3F3F')
frame_bottom = Frame(root, bg='#3F3F3F')
frame_inscription = Frame(root, bg='#3F3F3F')

                                                                        # titre (texte)
label_title = Label(frame_center, text="Banque", font=("Arial", 25), bg='#3F3F3F', fg='gray')
label_title_two = Label(frame_center, text="v-bucks", font=("Arial", 20), bg='#3F3F3F', fg='gray')
label_title.pack(side=TOP)
label_title_two.pack(side=TOP)

                                                                        # textes (centre)
label_subtitle = Label(frame_bottom, text="®zertou, mpxp Inc.", font=("Courrier", 15), bg='#3F3F3F', fg='gray')
label_subtitle.pack(side=BOTTOM)

                                                                        # boutons (centre)
yt_button = Button(frame_bottom, text="youtube", font=("Courrier", 15), bg='gray', fg='#3F3F3F', command=open_zertou_frais_chanel)
yt_button.pack(pady=25)


                                                                        # var pour inscri
id_var = StringVar()
mdp_var = StringVar()

                                                                        # entry
label_inscri = Label(frame_inscription, text="pour s'inscrire", font=("Arial", 20), bg='#3F3F3F', fg='gray')
label_inscri.pack(side=TOP)
id = Entry(frame_inscription, textvariable=id_var)
id.pack()
mdp = Entry(frame_inscription, textvariable=mdp_var)
mdp.pack()

                                                                        # bouton enregister (logique)
def retrieve_text():
    # Retrieve the text from the textvariable
    id_text = id_var.get()
    mdp_text = mdp_var.get()
    lened_id = len(id_text)
    lened_mdp = len(mdp_text)
    if lened_mdp >= 6:
        print("id :", id_text)
        print("mdp :", mdp_text)
    else:
        print("mot de passe trop court")


                                                                        # bouton enregister
button = Button(frame_inscription, text="s'inscrire", command=retrieve_text)
button.pack()

                                                                        # pack frames
frame_bottom.pack(side=BOTTOM)
frame_inscription.pack(side=LEFT)
frame_center.pack(expand=YES)

                                                                        # menu
menu_bar = Menu(root)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Explore", command=rick_roll)
file_menu.add_command(label="Quitter", command=root.quit)

menu_bar.add_cascade(label="Fichier", menu=file_menu)
root.config(menu=menu_bar)

root.mainloop()
