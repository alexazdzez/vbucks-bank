from tkinter import *
import webbrowser

import connection
import inscription


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

# titre (texte)
label_title = Label(frame_center, text="Banque", font=("Arial", 25), bg='#3F3F3F', fg='gray')
label_title_two = Label(frame_center, text="v-bucks", font=("Arial", 20), bg='#3F3F3F', fg='gray')
label_title.pack(side=TOP)
label_title_two.pack(side=TOP)

# textes
label_subtitle = Label(frame_bottom, text="®Tcharlex Inc.", font=("Courrier", 15), bg='#3F3F3F', fg='gray')
label_subtitle.pack(side=BOTTOM)

# boutons
yt_button = Button(frame_bottom, text="youtube", font=("Courrier", 15), bg='gray', fg='#3F3F3F',
                   command=open_zertou_frais_chanel)
yt_button.pack(pady=25)

# ajouter frames
frame_bottom.pack(side=BOTTOM)
frame_center.pack(expand=YES)
text_variable = StringVar()

# Create an Entry widget associated with the textvariable
entry = Entry(root, textvariable=text_variable)
entry.pack()


def retrieve_text():
    # Retrieve the text from the textvariable
    entered_text = text_variable.get()
    lened_text = len(entered_text)
    if lened_text >= 6:
        print("Entered text:", entered_text)
    else:
        print("trop petit")


# Create a button to trigger text retrieval
button = Button(root, text="Retrieve Text", command=retrieve_text)
button.pack()

# menu
menu_bar = Menu(root)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Explore", command=rick_roll)
file_menu.add_command(label="Quitter", command=root.quit)

compte_menu = Menu(menu_bar, tearoff=0)
compte_menu.add_command(label="se connecter", command=connection.connecter)
compte_menu.add_command(label="s'inscrire", command=inscription.inscrire)

menu_bar.add_cascade(label="Fichier", menu=file_menu)
menu_bar.add_cascade(label="compte", menu=compte_menu)
root.config(menu=menu_bar)

root.mainloop()
