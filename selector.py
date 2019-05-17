import tkinter
from level1 import *
from level2 import *

# Permet de lancer les niveaux choisit
def niveau1(self):
    self.select.destroy()
    l1 = level1()
def niveau2(self):
    self.select.destroy()
    l2 = level2()

class selector:

    # Constructeur par défaut > Création de la fenêtre
    def __init__(self):

        # Constructeur de la fenêtre principale
        self.select = tkinter.Tk()
        self.select.title('Niveaux')
        self.select.geometry('500x600')
        self.select.configure(background='#1a1a1a')
        self.select.resizable(width=False, height=False)

        # Déclaration des boutons & positionement de jouer et quitter

        self.boutonq = tkinter.Button(self.select, text='Quitter', command=self.select.destroy, bg="#e74c3c", fg="white")
        self.boutonq.place(relx=0.35, rely=0.80, height=50, width=140)

        self.Canevas = tkinter.Canvas(self.select, width=420, height=480, bg="#1a1a1a")
        self.Canevas.pack(side=tkinter.TOP, padx=10, pady=50)
        self.font10 = "-family {DejaVu Sans} -size 20"

        self.txtniv= tkinter.Label(self.select, text="Niveaux", bg="#1a1a1a", fg='white')
        self.txtniv.configure(font=self.font10)
        self.txtniv.place(relx=0.34, rely=0.02, height=25, width=150)

        # Configuration de la taille des lignes et colonnes de la grille
        self.Canevas.rowconfigure(1, minsize=75, weight=5)
        self.Canevas.columnconfigure(1, minsize=75, weight=5)
        self.Canevas.rowconfigure(2, minsize=75, weight=5)
        self.Canevas.columnconfigure(2, minsize=75, weight=5)
        self.Canevas.rowconfigure(3, minsize=75, weight=5)
        self.Canevas.columnconfigure(3, minsize=75, weight=5)
        self.Canevas.rowconfigure(4, minsize=75, weight=5)
        self.Canevas.columnconfigure(4, minsize=75, weight=5)
        self.Canevas.rowconfigure(5, minsize=75, weight=5)
        self.Canevas.columnconfigure(5, minsize=75, weight=5)

        # Déclaration et positionement sur la grilel des boutons ( certe un peu long)
        self.b1 = tkinter.Button(self.Canevas, text="1", bg='white', command=lambda: niveau1(self), font=self.font10)
        self.b1.grid(row=1, column=1, sticky='nesw')
        self.b2 = tkinter.Button(self.Canevas,text="2", bg='white', command=lambda: niveau2(self), font=self.font10)
        self.b2.grid(row=1, column=2, sticky='nesw')

        def enterb1(event):
            self.b1.configure(bg="#2ed573", fg="white")

        def leaveb1(event):
            self.b1.configure(bg="white", fg="black")

        def enterb2(event):
            self.b2.configure(bg="#2ed573", fg="white")

        def leaveb2(event):
            self.b2.configure(bg="white", fg="black")


        # Ajout au bouton les event qui permette de savoir quand on passe la souris dessus
        self.b1.bind("<Enter>", enterb1)
        self.b1.bind("<Leave>", leaveb1)
        self.b2.bind("<Enter>", enterb2)
        self.b2.bind("<Leave>", leaveb2)

        self.select.mainloop()


