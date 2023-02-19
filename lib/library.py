
from tkinter import *
import os
import webbrowser

from tkinter import filedialog

savedFile={1:""}

class editeurText:

    #Constructeur
    def __init__(self, fenPrincipal, zoneText):
        self.fenPrincipal=fenPrincipal
        self.zoneText=zoneText


    #creation de la fenetre
    def creaFenetre(self):
        self.fenPrincipal=Tk()
        self.fenPrincipal.title("Epsilon editor")

        #Calcul permettant de placer la fenetre au centre de l'ecran
        largeurEcran=self.fenPrincipal.winfo_screenwidth()
        hauteurEcran=self.fenPrincipal.winfo_screenheight()

        largeurfen=800
        hauteurfen=600

        posX=(largeurEcran//2)-(largeurfen//2)
        posY=(hauteurEcran//2)-(hauteurfen//2)

        geo="{}x{}+{}+{}".format(largeurfen,hauteurfen,posX,posY)

        self.fenPrincipal.geometry(geo)

    #creation d'une zone de texte
    def creaZoneText(self):
        self.zoneText=Text(self.fenPrincipal,undo=True,font=("Arial", 12))
        self.zoneText.pack(side=LEFT,expand=True , fill='both')

    #Generer la fenetre
    def genererFen(self):

        # Création de la barre de défilement
        scrollbar = Scrollbar(self.fenPrincipal)
        scrollbar.pack(side=RIGHT, fill=Y)

        # Association de la barre de défilement à la zone de texte
        scrollbar.config(command=self.zoneText.yview)
        self.zoneText.config(yscrollcommand=scrollbar.set)
        self.fenPrincipal.mainloop()

    # ----------ACTIONS DU MENU FICHIER--------
    def nouveau(self):
        os.popen("python main.py")

    def ouvrir(self):

        #selection du fichier dans la boite de dialogue
        file=filedialog.askopenfilename(initialdir="/",title="Selectionner un fichier",filetypes=(("Text File","*.txt"),("All files","*.*")))

        #ouverture du fichier avec les droit de lecture
        f=open(file,'r')
        r=f.read()
        f.close()

        #insertion du contenu du fichier dans la zone de texte
        self.zoneText.insert("1.0",r)

    def enregistrer_sous(self):
        fichier=filedialog.asksaveasfilename(defaultextension=".*",initialdir="/",title="Enregistrer sous", filetypes=(("Text File","*.txt"),("Python file","*.py"),("Excel file","*.xls"),("html file","*.html"),("css file","*.css"),("All files","*.*")))
        savedFile[1]=fichier
        f=open(fichier,'w')

        #Ajout du fichier dans la zone de texte au niveau de la ligne 1 position 0 jusqu'à la fin
        s=self.zoneText.get("1.0",END)
        f.write(s)
        f.close()

    def enregistrer(self):

        if(savedFile[1]==""):
            self.enregistrer_sous()
        else:
            f=open(savedFile[1],'w')
            s=self.zoneText.get("1.0",END)
            f.write(s)
            f.close()

    def quitter(self):
        self.fenPrincipal.quit()

    #------------------ACTION MENU EDITION----------------
    def copier(self):
        #vider le presse papier existant
        self.zoneText.clipboard_clear()
        self.zoneText.clipboard_append(self.zoneText.selection_get())

    def coller(self):
        self.zoneText.insert(INSERT,self.zoneText.clipboard_get())

    def couper(self):
        self.copier()
        self.zoneText.delete('sel.first','sel.last')

    def annuler(self):
        self.zoneText.edit_undo()

    def retablir(self):
        self.zoneText.edit_redo()


    #-------------ACTION MENU AFFICHAGE-----------------------

    def zoom_avant(self):
        facteur_zoom = 2
        taille_actuelle = self.zoneText["font"].split(" ")[-1]
        nouvelle_taille = int(taille_actuelle) + facteur_zoom
        self.zoneText.config(font=("Arial", nouvelle_taille))

    def zoom_arriere(self):
        facteur_zoom = 2
        taille_actuelle = self.zoneText["font"].split(" ")[-1]
        nouvelle_taille = int(taille_actuelle) - facteur_zoom
        if nouvelle_taille > 0:
            self.zoneText.config(font=("Arial", nouvelle_taille))

    # -------------ACTION MENU AIDE-----------------------

    def aide(self):
        webbrowser.open_new_tab("https://www.google.com")


    #------------------creation d'un menu------------------------
    def creaMenu(self):

        #creation du menu
        barreDemenu=Menu(self.fenPrincipal)

        #creation onglet fichier
        ongletFichier=Menu(barreDemenu,tearoff=False)

        barreDemenu.add_cascade(label="Fichier", menu=ongletFichier)
        ongletFichier.add_command(label="Nouveau",command=self.nouveau)
        ongletFichier.add_command(label="Ouvrir", command=self.ouvrir)
        ongletFichier.add_command(label="Enregistrer", command=self.enregistrer)
        ongletFichier.add_command(label="Enregistrer sous", command=self.enregistrer_sous)
        ongletFichier.add_command(label="Quitter", command=self.quitter)

        #creation onglet Edition
        ongletEdition=Menu(barreDemenu,tearoff=False)
        barreDemenu.add_cascade(label="Edition",menu=ongletEdition)
        ongletEdition.add_command(label="Copier",command=self.copier)
        ongletEdition.add_command(label="Annuler", command=self.annuler)
        ongletEdition.add_command(label="Retablir", command=self.retablir)
        ongletEdition.add_command(label="Coller", command=self.coller)
        ongletEdition.add_command(label="Couper", command=self.couper)

        #creation onglet affichage

        ongletAffichage=Menu(barreDemenu,tearoff=False)
        barreDemenu.add_cascade(label="Affichage",menu=ongletAffichage)
        ongletAffichage.add_command(label="zoom-avant",command=self.zoom_avant)
        ongletAffichage.add_command(label="zoom-arriere", command=self.zoom_arriere)


        #creation onglet Aide

        ongletAide=Menu(barreDemenu,tearoff=False)
        barreDemenu.add_cascade(label="Aide",menu=ongletAide)
        ongletAide.add_command(label="aide", command=self.aide)


        self.fenPrincipal.config(menu=barreDemenu)






