# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 22:54:56 2021
 
@author: Enzo
"""

from tkinter import *
import tkinter as Tkinter  
import tkinter.font as tkFont
import time, random


"""# Special Python function to load module with its file name
from importlib.machinery import SourceFileLoader

# My handout
myfile = "tg.py"

# Load module. Same result as "import mycode"
mycode = SourceFileLoader('mycode', myfile).load_module()
"""

from datetime import datetime 

counter = 0
running = False
go = False


#Code Main :
window = Tk()

def clear_window():
    for widgets in window.winfo_children():
        widgets.destroy()
    window.config(background='#13008F')


def counter_label(label):  
    def count():  
        if running:  
            global counter
            if counter>=200:              
                label['text'] = "T'es eclaté tu mets 20 ans, tu bois la !"
            else: 
                tt = datetime.fromtimestamp(counter) 
                string = tt.strftime("%M:%S") 
                display= string  
                label['text']=display         
                label.after(10, count)   
                counter += 1   
    count()       
    
def Start(label):  
    global running  
    running=True
    counter_label(label)
    
def Stop():  
    global running
    running = False
    
def Reset(label):  
    global counter  
    counter=0  
    tt = datetime.fromtimestamp(counter) 
    string = tt.strftime("%M:%S") 
    display=string  
    label['text']= display
    
    
def wait(label):
    rdn = random.randint(200,1000)
    def count():
        global go
        if not go :
            global counter
            if counter >= rdn :
                go = True
                counter = 0
                Start(label)
            elif counter>=100:              
                label['text'] = "Attention..."
            elif counter>=50:              
                label['text'] = "Attention.."
            else:  
                label['text']= "Attention."
            label.after(10, count )  
            counter += 1   
    count()


def Jouer():
    global go
    global count
    #clear avant de jouer
    clear_window()
    label = Tkinter.Label(window, text="Attention.", fg="black", font=("Verdana 30 bold",60))  
    label.place(relx=0.5, rely=0.5, anchor=CENTER)  
    f = Tkinter.Frame(window)
    
    if not go :
        wait(label)
    
    rdn = random.randint(1000,9000)
    
    """print ("1")
    label['text']= "Attention."
    print (rdn)
    
    window.mainloop()
    
    time.sleep(rdn/1000)
    label['text'] = "Attention.."
    print ("2")
    time.sleep(1)
    label['text'] = "Attention..."
    print ("3")
    time.sleep(1)
    label['text'] = "Atzevzezbzbz"
    """
    """def waithere():
        var = IntVar()
    root.after(3000, var.set, 1)
    print("waiting...")
    root.wait_variable(var)
    
    
    
    print ("1")
    waithere()
    print ("2")
    """
    
    
    """#transformer en quand espace pressed
    var = Tkinter.IntVar()
    button = Tkinter.Button(window, text = "Click Me", command = lambda: var.set(1))
    button.place(relx = .5, rely = .5, anchor = "c")
    
    print("waiting...")
    button.wait_variable(var)
    print("done waiting.")"""
 
    
    start = Tkinter.Button(f, text='Start', width=6, command=lambda:Start(label))  
    stop = Tkinter.Button(f, text='Stop',width=6, command=Stop)  
    reset = Tkinter.Button(f, text='Reset',width=6, command=lambda:Reset(label))  
    f.pack(anchor = 'center',pady=5) 
    start.pack(side="left")  
    stop.pack(side ="left")  
    reset.pack(side="left")
    
      
def StartJ1():
    #personaliser la fenetre
    window.title("J'suis Bourré")
    window.geometry("1080x720")
    window.config(background='#000316')
    
    #clear avant de jouer
    clear_window()
    
    #ajoute le bouton pour commencer
    boutonJouer=Button(window, text="Zé parti",  font=('Courier New',40), bg="#FFFFFF",fg="black")
    boutonJouer['command'] = lambda: Jouer()
    boutonJouer.place(relx=0.5, rely=0.5, anchor=CENTER)
    
    #ajoute la consigne
    label_title = Label(window, text="But : appuyer le plus vite sur espace avant que le verre tombe par terre, le plus lent boit", font=('Courier New',12), bg="#000316",fg="white")
    label_title.pack(side = BOTTOM, pady= 80)

    #afficher
    window.mainloop()


StartJ1()



