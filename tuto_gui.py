from tkinter import *

# Window creation, root of the interface
window = Tk()
# Creation of a label (text line) that says Hello World ! and with as first parameter the previous window
label_field = Label(window,text="Hello World !")
label_field.config(text="Hello World !")
# Display of the label
label_field.pack()

# La commande var_case.get() permet d'obtenir l'état de la variable var_case

# Mise en place bouton
bouton_quitter = Button(window, text="Quitter", command=window.quit)
bouton_quitter.pack()

# Mise en place d'une ligne de saisi de texte
var_texte = StringVar()
ligne_texte = Entry(window, textvariable=var_texte, width=30)
ligne_texte.pack()

# Mise en place cases à cocher
var_case = IntVar()
case = Checkbutton(window, text="Ne plus poser cette question", variable=var_case)
case.pack()

# Mise en place bouton radio
var_choix = StringVar()

choix_rouge = Radiobutton(window, text="Rouge", variable=var_choix, value="rouge")
choix_vert = Radiobutton(window, text="Vert", variable=var_choix, value="vert")
choix_bleu = Radiobutton(window, text="Bleu", variable=var_choix, value="bleu")

choix_rouge.pack()
choix_vert.pack()
choix_bleu.pack()

# Mise en place liste
liste = Listbox(window)
liste.pack()
# Insérer un élément à la liste
liste.insert(END, "Pierre")
liste.insert(END, "Feuille")
liste.insert(END, "Ciseau")

# Fonctionnement Frame
cadre = Frame(window, width=768, height=576, borderwidth=1)
cadre.pack(fill=BOTH)

message = Label(cadre, text="Notre fenêtre")
message.pack(side="top", fill=X)
# Il existe aussi l'argument nomméfillqui permet au widget de remplir le widget parent,
# soit en largeur si la valeur est X, soit en hauteur si la valeur est Y,
# soit en largeur et hauteur si la valeur estBOTH.

# Running of the Tkinter loop that ends when we close the window
window.mainloop()

