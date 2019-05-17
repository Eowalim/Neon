import tkinter
from level2 import *

# Déclaration des variables mémoire. (pour pouvoir les utilisés plus bas )
# quand clicke = 2 > il fait un check pour voir si il peut colorer la case
# memcol1 et memco2 = variables  memoire des couleurs du bouton 1 et 2
# memnl1 et memn2 = variables   memoire des noms du bouton 1 et 2

click = 0
memcol1 = ""
memcol2 = ""

memn1 = ""
memn2 = ""

# Tableau de la grille valide
grille_valid = [
    ["blue", "blue", "blue", "blue", "blue"],
    ["yellow", "yellow", "yellow", "yellow", "blue"],
    ["green", "green", "green", "yellow", "blue"],
    ["green", "red", "red", "red", "blue"],
    ["green", "green", "green", "green", "blue"]
]

# Tableau de la grille non valide
grille = [
    ["blue", "white", "white", "white", "white"],
    ["yellow", "white", "white", "white", "white"],
    ["white", "white", "green", "yellow", "white"],
    ["white", "red", "white", "red", "white"],
    ["white", "white", "white", "green", "blue"]
]

# Classe level2
class level2:

     # Constructeur par défaut > Création de la fenêtre
    def __init__(self):

        # Constructeur de la fenêtre principale
        self.game = tkinter.Tk()
        self.game.title('Neon')
        self.game.geometry('500x600')
        self.game.configure(background='#1a1a1a')
        self.game.resizable(width=False, height=False)

        # Déclaration des boutons & positionement de jouer et quitter

        self.boutonq = tkinter.Button(self.game, text='Quitter', command=self.game.destroy, bg="#e74c3c", fg="white")
        self.boutonq.place(relx=0.37, rely=0.93, height=30, width=120)

        self.Canevas = tkinter.Canvas(self.game, width=420, height=480)
        self.Canevas.pack(side=tkinter.TOP, padx=10, pady=50)
        self.font10 = "-family {DejaVu Sans} -size 20"

        self.txtniv = tkinter.Label(self.game, text="Niveau 2", bg="#1a1a1a", fg='white')
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
        self.b1 = tkinter.Button(self.Canevas, bg='blue', command=lambda: self.couleur(self.b1, "b1"))
        self.b1.grid(row=1, column=1, sticky='nesw')
        self.b2 = tkinter.Button(self.Canevas, bg='white', command=lambda: self.couleur(self.b2, "b2"))
        self.b2.grid(row=1, column=2, sticky='nesw')
        self.b3 = tkinter.Button(self.Canevas, bg='white', command=lambda: self.couleur(self.b3, "b3"))
        self.b3.grid(row=1, column=3, sticky='nesw')
        self.b4 = tkinter.Button(self.Canevas, bg="white", command=lambda: self.couleur(self.b4, "b4"))
        self.b4.grid(row=1, column=4, sticky='nesw')
        self.b5 = tkinter.Button(self.Canevas, bg='white', command=lambda: self.couleur(self.b5, "b5"))
        self.b5.grid(row=1, column=5, sticky='nesw')
        self.b6 = tkinter.Button(self.Canevas, bg='yellow', command=lambda: self.couleur(self.b6, "b6"))
        self.b6.grid(row=2, column=1, sticky='nesw')
        self.b7 = tkinter.Button(self.Canevas, bg='white', command=lambda: self.couleur(self.b7, "b7"))
        self.b7.grid(row=2, column=2, sticky='nesw')
        self.b8 = tkinter.Button(self.Canevas, bg='white', command=lambda: self.couleur(self.b8, "b8"))
        self.b8.grid(row=2, column=3, sticky='nesw')
        self.b9 = tkinter.Button(self.Canevas, bg='white', command=lambda: self.couleur(self.b9, "b9"))
        self.b9.grid(row=2, column=4, sticky='nesw')
        self.b10 = tkinter.Button(self.Canevas, bg='white', command=lambda: self.couleur(self.b10, "b10"))
        self.b10.grid(row=2, column=5, sticky='nesw')
        self.b11 = tkinter.Button(self.Canevas, bg='white', command=lambda: self.couleur(self.b11, "b11"))
        self.b11.grid(row=3, column=1, sticky='nesw')
        self.b12 = tkinter.Button(self.Canevas, bg='white', command=lambda: self.couleur(self.b12, "b12"))
        self.b12.grid(row=3, column=2, sticky='nesw')
        self.b13 = tkinter.Button(self.Canevas, bg='green', command=lambda: self.couleur(self.b13, "b13"))
        self.b13.grid(row=3, column=3, sticky='nesw')
        self.b14 = tkinter.Button(self.Canevas, bg='yellow', command=lambda: self.couleur(self.b14, "b14"))
        self.b14.grid(row=3, column=4, sticky='nesw')
        self.b15 = tkinter.Button(self.Canevas, bg='white', command=lambda: self.couleur(self.b15, "b15"))
        self.b15.grid(row=3, column=5, sticky='nesw')
        self.b16 = tkinter.Button(self.Canevas, bg='white', command=lambda: self.couleur(self.b16, "b16"))
        self.b16.grid(row=4, column=1, sticky='nesw')
        self.b17 = tkinter.Button(self.Canevas, bg='red', command=lambda: self.couleur(self.b17, "b17"))
        self.b17.grid(row=4, column=2, sticky='nesw')
        self.b18 = tkinter.Button(self.Canevas, bg='white', command=lambda: self.couleur(self.b18, "b18"))
        self.b18.grid(row=4, column=3, sticky='nesw')
        self.b19 = tkinter.Button(self.Canevas, bg='red', command=lambda: self.couleur(self.b19, "b19"))
        self.b19.grid(row=4, column=4, sticky='nesw')
        self.b20 = tkinter.Button(self.Canevas, bg='white', command=lambda: self.couleur(self.b20, "b20"))
        self.b20.grid(row=4, column=5, sticky='nesw')
        self.b21 = tkinter.Button(self.Canevas, bg='white', command=lambda: self.couleur(self.b21, "b21"))
        self.b21.grid(row=5, column=1, sticky='nesw')
        self.b22 = tkinter.Button(self.Canevas, bg='white', command=lambda: self.couleur(self.b22, "b22"))
        self.b22.grid(row=5, column=2, sticky='nesw')
        self.b23 = tkinter.Button(self.Canevas, bg='white', command=lambda: self.couleur(self.b23, "b23"))
        self.b23.grid(row=5, column=3, sticky='nesw')
        self.b24 = tkinter.Button(self.Canevas, bg='green', command=lambda: self.couleur(self.b24, "b24"))
        self.b24.grid(row=5, column=4, sticky='nesw')
        self.b25 = tkinter.Button(self.Canevas, bg='blue', command=lambda: self.couleur(self.b25, "b25"))
        self.b25.grid(row=5, column=5, sticky='nesw')
        self.boutonj = tkinter.Button(self.game, text='Vérifier la grille', command=lambda: self.win(), bg="#27ae60",
                                      fg="white")
        self.boutonj.place(relx=0.37, rely=0.87, height=30, width=120)

        self.game.mainloop()

    # ------------------Méthodes & Fonctions ------------------#

    def couleur(self, btn, nb):
        global click, memn1, memn2, memcol1, memcol2  # permet de modifier ces variables dans la méthode
        # Pour le premier bouton cliqué
        if click == 0:
            # Recupération du nom de la variable puis conversion et mise en mémoire
            nombtn = nb
            memn1 = nombtn

            # Recupération de la couleur puis conversion et mise en mémoire
            c1 = self.getCouleur(btn)
            col1 = self.convert_color(c1)
            memcol1 = col1

            click += 1

            verif = "Numéro du clique : {} \nNuméro du bouton : {} \nCouleur : {} ".format(click, nb, memcol1)
            print(verif)


        # Pour le premier bouton cliqué
        elif click == 1:
            # Recup nom de la variable + mis dans la mémoire
            nombtn2 = nb
            memn2 = nombtn2

            # Recup de la couleur puis on la convertit et on la met dans la mémoire
            c2 = self.getCouleur(btn)
            col2 = self.convert_color(c2)
            memcol2 = col2

            click += 1
            verif = "\nNuméro du clique : {} \nNuméro du bouton : {} \nCouleur : {} ".format(click, nb, memcol2)
            print(verif)

        # Après le clique sur les deux boutons on test pour savoir si on peut les peindre + remise à 0 du compteur de click pour pourvoir recliqué sur 2 bouton et ainsi de suite
        if click == 2:
            verif = "\nClick : {}, je doit faire un test ".format(click)
            print(verif)
            self.check_paint(memn1, memn2, memcol1, memcol2)
            click = 0

    # Recup la couleur du bouton cliqué dans le format ( X, X, X) et la retourne
    def getCouleur(self, btn):
        couleur = btn.winfo_rgb(btn["bg"])
        return couleur

    # Permet de convertir une couleur (X, X, X) en nom de couleur
    def convert_color(self, colortoconvert):
        color = colortoconvert
        if color == (0, 32896, 0):
            color = "green"
        elif color == (65535, 0, 0):
            color = "red"
        elif color == (65535, 65535, 0):
            color = "yellow"
        elif color == (0, 0, 65535):
            color = "blue"
        elif color == (65535, 65535, 65535):
            color = "white"

        return color

    # Méthode pour savoir si on peut peinde les variable " n = sont les noms des bouton "" et " c= les couleurs" / " " 1 = premeir bouton cliqué " et " 2 : deuxieme boutons cliqué"
    def check_paint(self, case1, case2, color1, color2):
        # Check si on veut peindre une case existante colorée et si c'est de la même couleur.
        if (case1 == "b1"
            or case1 == "b6"
            or case1 == "b13"
            or case1 == "b14"
            or case1 == "b17"
            or case1 == "b19"
            or case1 == "b24"
            or case1 == "b25") and (case2 == "b1"
            or case2 == "b6"
            or case2 == "b13"
            or case2 == "b15"
            or case2 == "b17"
            or case2 == "b19"
            or case2 == "b24"
            or case2 == "b25"):
            print("On ne peut pas coloré la case ")
            if color1 == color2:
                print("On ne peut pas coloré la case ")
        else:
            print("On peut coloré la case ")
            self.paint(case2,color1)  # apelle de la méthode paint pour colrée la deuxieme case avec la couleur du premier bouton

    # Permet de peindre la case + remplace dans le tableau de la grille non valide
    def paint(self, case, color):
        global grille
        if case == "b2":
            self.b2.configure(bg=color)
            grille[0][1] = color
        elif case == "b3":
            self.b3.configure(bg=color)
            grille[0][2] = color
        elif case == "b4":
            self.b4.configure(bg=color)
            grille[0][3] = color
        elif case == "b5":
            self.b5.configure(bg=color)
            grille[0][4] = color
        elif case == "b7":
            self.b7.configure(bg=color)
            grille[1][1] = color
        elif case == "b8":
            self.b8.configure(bg=color)
            grille[1][2] = color
        elif case == "b9":
            self.b9.configure(bg=color)
            grille[1][3] = color
        elif case == "b10":
            self.b10.configure(bg=color)
            grille[1][4] = color
        elif case == "b11":
            self.b11.configure(bg=color)
            grille[2][0] = color
        elif case == "b12":
            self.b12.configure(bg=color)
            grille[2][1] = color
        elif case == "b15":
            self.b15.configure(bg=color)
            grille[2][4] = color
        elif case == "b16":
            self.b16.configure(bg=color)
            grille[3][0] = color
        elif case == "b18":
            self.b18.configure(bg=color)
            grille[3][2] = color
        elif case == "b20":
            self.b20.configure(bg=color)
            grille[3][4] = color
        elif case == "b21":
            self.b21.configure(bg=color)
            grille[4][0] = color
        elif case == "b22":
            self.b22.configure(bg=color)
            grille[4][1] = color
        elif case == "b23":
            self.b23.configure(bg=color)
            grille[4][2] = color


    # Vérifie si les 2 grilles correspondent
    def win(self):
        # OUI : Affiche gagné
        if grille_valid == grille:
            self.font10 = "-family {DejaVu Sans} -size 20"
            self.txtgagner = tkinter.Label(self.game, text="Gagné", bg="#1a1a1a", fg='green')
            self.txtgagner.configure(font=self.font10)
            self.txtgagner.place(relx=0.32, rely=0.73, height=30, width=170)

            self.boutonj.destroy()
            self.boutonreco = tkinter.Button(self.game, text='Niveau suivant', command=lambda: self.suivant(),bg="#f39c12", fg="white")
            self.boutonreco.place(relx=0.37, rely=0.87, height=30, width=120)

        # NON: Affiche perdu + bouton recommencer apparait
        else:

            self.font10 = "-family {DejaVu Sans} -size 20"
            self.perdu = tkinter.Label(self.game, text="Perdu", bg="#1a1a1a", fg='red')
            self.perdu.configure(font=self.font10)
            self.perdu.place(relx=0.32, rely=0.73, height=30, width=170)
            self.boutonj.destroy()
            self.boutonr = tkinter.Button(self.game, text='Recommencer', command=lambda: self.recommencer(),bg="#f39c12", fg="white")
            self.boutonr.place(relx=0.37, rely=0.87, height=30, width=120)

    # Ferme la fenêtre actuelle et en ouvre une nouvelle
    def recommencer(self):
        self.game.destroy()
        self.__init__()

    # Ferme la fenêtre actuelle et ouvre le niveau 2
    def suivant(self):
        self.game.destroy()
        l2 = level2()



