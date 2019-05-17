import tkinter

from selector import *


#---------------------------------------------------Création Launcher--------------------------------------------------#
# Création de la fenêtre
launcher = tkinter.Tk()
launcher.title('Launcher')
launcher.geometry('500x600')
launcher.resizable(width=False, height=False)

image = tkinter.PhotoImage(file='bgrd.png', master=launcher)
canvas = tkinter.Canvas(launcher, width=500, height=600)
canvas.pack()
canvas.create_image((500 // 2, 700 // 2), image=image)

#Charge la police d'écriture
font10 = "-family {DejaVu Sans} -size 25"

#Bouton jouer
boutonJ = tkinter.Button(canvas, text='JOUER', command=lambda: run(), bg="#1a1a1a", fg="white")
boutonJ.place(relx=0.34, rely=0.45, height=75, width=170)
boutonJ.configure(font=font10)

#Bouton éditeur
boutone = tkinter.Button(canvas, text='EDITEUR', bg="#1a1a1a", fg="#747d8c")
boutone.place(relx=0.34, rely=0.60, height=75, width=170)
boutone.configure(font=font10)

#Bouton quitter
boutonq = tkinter.Button(canvas, text='QUITTER', command=lambda: launcher.destroy(), bg="#1a1a1a", fg="white")
boutonq.place(relx=0.34, rely=0.75, height=75, width=170)
boutonq.configure(font=font10)

# Permet de lancer le selecteur de niveau
def run():
    launcher.destroy()
    l1 = selector ()


# Permet de détécter quand la souris passe et quitte un bouton .
def enterj(event):
    boutonJ.configure(bg="#2ed573")

def enterq(event):
    boutonq.configure(bg="#e74c3c")

def leave(event):
    boutonJ.configure(bg="#1a1a1a")
    boutonq.configure(bg="#1a1a1a")





# Ajoutte au bouton les evenement qui pemettent de savoir quand on passe la souris dessus
boutonJ.bind("<Enter>", enterj)
boutonJ.bind("<Leave>", leave)
boutonq.bind("<Enter>", enterq)
boutonq.bind("<Leave>", leave)


launcher.mainloop()

