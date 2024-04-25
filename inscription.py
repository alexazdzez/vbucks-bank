import string
from tkinter import *


def retrieve_text(text_variable):
    # Retrieve the text from the textvariable
    entered_text = text_variable.get()
    print("Entered text:", entered_text)
def inscrire():
    root = Tk()
    root.title("inscription")
    root.geometry("500x500")
    root.minsize(480, 360)
    root.config(background='#3F3F3F')
    frame = Frame(root, bg='#3F3F3F')

    text_variable = StringVar()

    # Create an Entry widget associated with the textvariable
    entry = Entry(root, textvariable=text_variable)
    entry.pack()


    # Create a button to trigger text retrieval
    button = Button(root, text="Retrieve Text", command=lambda: retrieve_text(text_variable))
    button.pack()
    frame.pack(expand=YES)

    root.mainloop()
