import tkinter as tk

# Create a Tkinter window
window = tk.Tk()
window.title("Getting Textvariable from Entry")

# Create a textvariable
text_variable = StringVar()

# Create an Entry widget associated with the textvariable
entry = tk.Entry(window, textvariable=text_variable)
entry.pack()


def retrieve_text():
    # Retrieve the text from the textvariable
    entered_text = text_variable.get()
    print("Entered text:", entered_text)


# Create a button to trigger text retrieval
button = tk.Button(window, text="Retrieve Text", command=retrieve_text)
button.pack()

# Run the Tkinter event loop
window.mainloop()
