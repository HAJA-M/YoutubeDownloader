'''
Projet : YouTube Video Downloader V1.0
Ce projet est une application de téléchargement de vidéos YouTube développée en Python,
utilisant le framework CustomTkinter pour l'interface utilisateur.
L'application permet aux utilisateurs de télécharger facilement des vidéos YouTube en entrant simplement l'URL de la vidéo souhaitée.
L'interface intuitive et esthétique, grâce à CustomTkinter, offre une expérience utilisateur agréable et efficace.

Modification à apporter :
gestion des erreurs lors du téléchargement de la vidéo [1]
Ajout d'une barre de progression pour indiquer l'avancement du téléchargement de la vidéo [1]

'''

import tkinter
import customtkinter
from pytube import YouTube

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

#fenêtre
root = customtkinter.CTk()
root.title("YouTube Video Downloader V1.2")
root.geometry("500x300")

#function
def telecharger():
    try: 
        YtLink = lien.get()
        Ytobjet = YouTube(YtLink, on_progress_callback=encours)
        video = Ytobjet.streams.get_highest_resolution()
        titre.configure(text=Ytobjet.title + " est en cours de téléchargement ...")
        video.download()
        Tterminer.configure(text="Video téléchargée avec succès !", text_color="green")
        print("Téléchargement OK !")

    except:
        Tterminer.configure(text="Une erreur est survenue lors du téléchargement de la vidéo.", text_color="red")
        print("Une erreur est survenue lors du téléchargement de la vidéo.")

def encours(stream, chunk, bytes_remaining):
    taille_total = stream.filesize
    byte_telecharger = taille_total - bytes_remaining
    pourcentage = byte_telecharger / taille_total * 100
    print(f"{pourcentage}%")
    valeur_pourcentage = str(int(pourcentage))
    textPourcentage.configure(text=valeur_pourcentage + "%")
    textPourcentage.update()

    #barre de progression mise à jour
    barre.set(float(pourcentage)/100)

    if pourcentage == 100:
        barre.configure(progress_color="green")

#titre
titre = customtkinter.CTkLabel(root, text="Votre lien YouTube :")
titre.pack(padx=10, pady=10)

#lien
urlvar = tkinter.StringVar()
lien = customtkinter.CTkEntry(root, width=500, height=40, textvariable=urlvar)
lien.pack(padx=10, pady=10)

#telechargement terminer
Tterminer = customtkinter.CTkLabel(root, text="")
Tterminer.pack(padx=10, pady=10)

#barre de progression
barre = customtkinter.CTkProgressBar(root, width=500, height=5,progress_color="red")
barre.set(0)
barre.pack(padx=10, pady=10)

textPourcentage = customtkinter.CTkLabel(root, text="0%")
textPourcentage.pack(padx=10, pady=10)

#bouton
btn1 = customtkinter.CTkButton(root, text="Télécharger", command=telecharger)
btn1.pack(padx=10, pady=10)


root.mainloop()