# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 21:56:30 2021

@author: TG
"""

from tkinter import *
import tkinter.font as tkFont
import webbrowser
"""
# Load module. Same result as "import Jeu1Source"
from importlib.machinery import SourceFileLoader
myfile1 = "Jeu1.py"
Jeu1Source = SourceFileLoader('Jeu1Source', myfile1).load_module()
"""
#creer une fenetre
window = Tk()
window.geometry("1080x720")
window.minsize(1080,720)
window.maxsize(1080,720)
playerList = [None]*8

def clear_window():
   for widgets in window.winfo_children():
      widgets.destroy()

def InstaEnzo():
   webbrowser.open_new("https://instagram.com/enzo_sgm")

def InstaElios():
   webbrowser.open_new("https://instagram.com/elios.pxt")

def stockPlayer(entree1,entree2,entree3,entree4,entree5,entree6,entree7,entree8):
    playerList[0] = entree1.get()
    playerList[1] = entree2.get()
    playerList[2] = entree3.get()
    playerList[3] = entree4.get()
    playerList[4] = entree5.get()
    playerList[5] = entree6.get()
    playerList[6] = entree7.get()
    playerList[7] = entree8.get()
    
    for i in range(8) :
        if playerList[i] == "Nom du joueur..." :
            playerList[i] = None
    Game()
    
def PlayerMenu():
    clear_window()
    window.title("Configuration Joueurs")
    window.config(background='#000316')
    
    Home = Button(window, text="  Accueil ",  font=('Courier New',20), bg="#050027", fg="white")
    Home['command'] = lambda: Start()
    Home.pack( side = TOP)

    label_title = Label(window, text="Entrez le nom de tous les joueurs :", font=('Courier New',25), bg="#000316",fg="white")
    label_title.pack(side = TOP,pady=20)
    label_title2 = Label(window, text="(8 joueurs maximum, laissez vide si il y a moins de joueurs)", font=('Courier New',12), bg="#000316",fg="white")
    label_title2.pack(side = TOP,pady=5)
    
    
    frameName1 = Frame(window,background='#000316')
    frameName1.pack(side=TOP)
    Joueur1 = Label(frameName1, text="Joueur 1 :", font=('Courier New',20), bg="#000316",fg="white")
    Joueur1.pack(side = LEFT,pady=10)
    value1 = StringVar()
    value1.set("Nom du joueur...")
    entree1 = Entry(frameName1, textvariable=value1, width=25, font=('Courier New',20))
    entree1.pack(side = LEFT,padx=20,pady=10)
  
    frameName2 = Frame(window,background='#000316')
    frameName2.pack(side=TOP)
    Joueur2 = Label(frameName2, text="Joueur 2 :", font=('Courier New',20), bg="#000316",fg="white")
    Joueur2.pack(side = LEFT,pady=10)
    value2 = StringVar()
    value2.set("Nom du joueur...")
    entree2 = Entry(frameName2, textvariable=value2,  width=25, font=('Courier New',20))
    entree2.pack(side = LEFT,padx=20,pady=10)
    
    frameName3 = Frame(window,background='#000316')
    frameName3.pack(side=TOP)
    Joueur3 = Label(frameName3, text="Joueur 3 :", font=('Courier New',20), bg="#000316",fg="white")
    Joueur3.pack(side = LEFT,pady=10)
    value3 = StringVar()
    value3.set("Nom du joueur...")
    entree3 = Entry(frameName3, textvariable=value3,  width=25, font=('Courier New',20))
    entree3.pack(side = LEFT,padx=20,pady=10) 
       
    frameName4 = Frame(window,background='#000316')
    frameName4.pack(side=TOP)
    Joueur4 = Label(frameName4, text="Joueur 4 :", font=('Courier New',20), bg="#000316",fg="white")
    Joueur4.pack(side = LEFT,pady=10)
    value4 = StringVar()
    value4.set("Nom du joueur...")
    entree4 = Entry(frameName4, textvariable=value4,  width=25, font=('Courier New',20))
    entree4.pack(side = LEFT,padx=20,pady=10)
    
    frameName5 = Frame(window,background='#000316')
    frameName5.pack(side=TOP)
    Joueur5 = Label(frameName5, text="Joueur 5 :", font=('Courier New',20), bg="#000316",fg="white")
    Joueur5.pack(side = LEFT,pady=10)
    value5 = StringVar()
    value5.set("Nom du joueur...")
    entree5 = Entry(frameName5, textvariable=value5, width=25, font=('Courier New',20))
    entree5.pack(side = LEFT,padx=20,pady=10)
    
    frameName6 = Frame(window,background='#000316')
    frameName6.pack(side=TOP)
    Joueur6 = Label(frameName6, text="Joueur 6 :", font=('Courier New',20), bg="#000316",fg="white")
    Joueur6.pack(side = LEFT,pady=10)
    value6 = StringVar()
    value6.set("Nom du joueur...")
    entree6 = Entry(frameName6, textvariable=value6, width=25, font=('Courier New',20))
    entree6.pack(side = LEFT,padx=20,pady=10)
    
    frameName7 = Frame(window,background='#000316')
    frameName7.pack(side=TOP)
    Joueur7 = Label(frameName7, text="Joueur 7 :", font=('Courier New',20), bg="#000316",fg="white")
    Joueur7.pack(side = LEFT,pady=10)
    value7 = StringVar()
    value7.set("Nom du joueur...")
    entree7 = Entry(frameName7, textvariable=value7, width=25, font=('Courier New',20))
    entree7.pack(side = LEFT,padx=20,pady=10)
    
    frameName8 = Frame(window,background='#000316')
    frameName8.pack(side=TOP)
    Joueur8 = Label(frameName8, text="Joueur 8 :", font=('Courier New',20), bg="#000316",fg="white")
    Joueur8.pack(side = LEFT,pady=10)
    value8 = StringVar()
    value8.set("Nom du joueur...")
    entree8 = Entry(frameName8, textvariable=value8, width=25, font=('Courier New',20))
    entree8.pack(side = LEFT,padx=20,pady=10)
    
    
    boutonLaunch=Button(window, text="Lancer la partie",  font=('Courier New',25), bg="#FFFFFF",fg="black")
    boutonLaunch['command'] = lambda: stockPlayer(entree1,entree2,entree3,entree4,entree5,entree6,entree7,entree8)
    boutonLaunch.pack(side=TOP,pady=15)
    window.mainloop()
    
    
def Game():
    #window.destroy()
    clear_window()
    window.title("Menu Jeux")
    window.config(background='#13008F')
  
    
    
    frame = Frame(window)
    frame.grid(row=0,column=1, pady=0)

    
  
   
    Home = Button(frame, text="  Accueil ",  font=('Courier New',20), bg="#050027", fg="white")
    Home['command'] = lambda: Start()
    Home.pack( side = LEFT)
    
    Settings = Button(frame, text="Paramètres",  font=('Courier New',20), bg="#050027", fg="white")
    Settings['command'] = lambda: SettingsMenu(Game)
    Settings.pack( side = LEFT)
    
    boutonJeu1=Button(window, text="ESKE T'é SOUL ?",  font=('Courier New',25), bg="#FFFFFF", fg="black")
    boutonJeu1['command'] = lambda: Game()
    boutonJeu1.grid(row=1,column=0, padx=15,pady=20)
    
    boutonJeu2=Button(window, text="JSP ENCORE     ",  font=('Courier New',25), bg="#FFFFFF", fg="black")
    boutonJeu2['command'] = lambda: Game()
    boutonJeu2.grid(row=1,column=1, padx=15,pady=20) 
    
    boutonJeu3=Button(window, text="JSP ENCORE     ",  font=('Courier New',25), bg="#FFFFFF", fg="black")
    boutonJeu3['command'] = lambda: Game()
    boutonJeu3.grid(row=1,column=2, padx=15,pady=20) 
    
    
    window.mainloop()
    
"""  
def Jeu1(window):
    Jeu1Source.Start(window)
"""  

def SettingsMenu(fromMenu):
    clear_window()
    window.title("Settings")
    window.config(background='#13008F')

    
    Back = Button(window, text="Retour",  font=('Courier New',20), bg="#050027", fg="white")
    Back['command'] = lambda: fromMenu()
    Back.grid(row=0,column=0, padx=15,pady=15)
    
    
    window.mainloop()
    

    
def Start():
    clear_window()
    #personaliser la fenetre
    window.title("Accueil")
    window.config(background='#000316')
    
    playerList = [None]*8
      
    Settings = Button(window, text="Paramètres",  font=('Courier New',20), bg="#050027", fg="white")
    Settings['command'] = lambda: SettingsMenu(Start)
    Settings.pack( side = TOP)
    
    #ajouter un txt
    label_title = Label(window, text="Prêt à se péter le front ?", font=('Courier New',40), bg="#000316",fg="white")
    label_title.pack(expand=YES)

   
    #ajouter un bouton
    boutonLaunch=Button(window, text="OK LET'S GO !",  font=('Courier New',30), bg="#FFFFFF",fg="black")
    boutonLaunch['command'] = lambda: PlayerMenu()
    boutonLaunch.pack()
    
    #ajouter un txt
    label_title = Label(window, text="Développé par les cracks de leur génération", font=('Courier New',12), bg="#000316",fg="white")
    label_title.pack(expand=YES)
    
    # bouton insta
    boutonInsta1=Button(window, text="insta Enzo",  font=('Courier New',10), bg="#FFFFFF",fg="black", command = InstaEnzo)
    boutonInsta1.pack(side=LEFT)

    boutonInsta2=Button(window, text="insta Elios",  font=('Courier New',10), bg="#FFFFFF",fg="black", command = InstaElios)
    boutonInsta2.pack(side=RIGHT)
   

    #afficher
    window.mainloop()


Start()