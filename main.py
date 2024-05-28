'''
Projet : YouTube Video Downloader V1
Ce projet est une application de téléchargement de vidéos YouTube développée en Python,
utilisant le framework CustomTkinter pour l'interface utilisateur.
L'application permet aux utilisateurs de télécharger facilement des vidéos YouTube en entrant simplement l'URL de la vidéo souhaitée.
L'interface intuitive et esthétique, grâce à CustomTkinter, offre une expérience utilisateur agréable et efficace.

Modification à apporter :
gestion des erreurs lors du téléchargement de la vidéo

'''

import tkinter
import customtkinter
from pytube import YouTube

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

#fenêtre
root = customtkinter.CTk()
root.title("YouTube Video Downloader V1")
root.geometry("400x210")

#function
def telecharger():
    try: 
        YtLink = lien.get()
        Ytobjet = YouTube(YtLink)
        video = Ytobjet.streams.get_highest_resolution()
        titre.configure(text=Ytobjet.title + " est en cours de téléchargement ...")
        video.download()

    except:
        Tterminer.configure("Une erreur est survenue lors du téléchargement de la vidéo.", text_color="red")
    Tterminer.configure(text="Video téléchargée avec succès !", text_color="green")

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

#bouton
btn1 = customtkinter.CTkButton(root, text="Télécharger", command=telecharger)
btn1.pack(padx=10, pady=10)


root.mainloop()