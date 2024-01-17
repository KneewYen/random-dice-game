from tkinter import *
from math import*
import random
import time
from tkinter import messagebox
fenetre1=Tk()

j1,j2,mj1,mj2,m1,m2,ch1,ch2,r,rpi,col1,col2="","",120,120,0,0,0,0,0,0,'',''

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        fenetre1.destroy()
def widget():
  tex1 = Label(fenetre1, text='Voici les règles du jeu du lancer de dé:',font=('Arial', 30)) # widget, zone pour le texte 
 
  tex1.pack()	# une méthode pour faire apparaître le widget précédent 
 
  text2 = Label (fenetre1, text='Tous les participants commencent avec 120$, chaque joueur doit miser un montant sur la face du dé à 6 face et le gagnant raportera la mise. \n Ainsi, deviner le chiffre fera de votre mise fois 6 alors que deviner la nature du chiffre (pair/impair) doublera votre mise. \n Toutefois, si vous devinez la mauvaise nature du chiffre ou le mauvais chiffre, vous perdrez votre mise. \n Attention, il est suggéré de ne pas misez la totalité de votre fortune sinon le jeu ne durera pas longtemps😅. \n Bonne chance! ', fg='red') 
 
  text2.pack() 
 
  text3 = Label (fenetre1, text='À vos dés', font=('Arial', 15), fg='blue') 
  bou1 = Button(fenetre1, text='Commencer',command = fenetre1.destroy) # widget (type bouton)  
  bou1.pack() # une méthode pour faire apparaître le widget précédent
  text3.pack() 
  fenetre1.protocol("WM_DELETE_WINDOW", on_closing)
  fenetre1.mainloop()

def rules():
    règles=input('Voulez vous voir les règles du jeu?')
    while règles not in ('Oui','oui','Non','non'):
        règles=input('Oui ou Non?')
    if règles in ('Oui','oui'):
        widget()

print("Bonjour et bienvenue au jeu de 🎲")
rules()

from turtle import Turtle
joe = Turtle()
 
def dice1():
  joe.pendown()
  joe.forward(100)
  joe.left(90)
  joe.forward(100)
  joe.left(90)
  joe.forward(100)
  joe.left(90)
  joe.forward(100)
  joe.penup()
  joe.goto(50, 50)
  joe.pendown()
  joe.color("black")
  joe.dot(10)
  joe.hideturtle()
  
def dice2():
  joe.pendown()
  joe.forward(100)
  joe.left(90)
  joe.forward(100)
  joe.left(90)
  joe.forward(100)
  joe.left(90)
  joe.forward(100)
  joe.penup()
  joe.goto(30, 50)
  joe.pendown()
  joe.color("black")
  joe.dot(10)
  joe.penup()
  joe.goto(60, 50)
  joe.pendown()
  joe.color("black")
  joe.dot(10)
  joe.hideturtle()
  
def dice3():
  joe.pendown()
  joe.forward(100)
  joe.left(90)
  joe.forward(100)
  joe.left(90)
  joe.forward(100)
  joe.left(90)
  joe.forward(100)
  joe.penup()
  joe.goto(30, 30)
  joe.pendown()
  joe.color("black")
  joe.dot(10)
  joe.penup()
  joe.goto(50, 50)
  joe.pendown()
  joe.color("black")
  joe.dot(10)
  joe.penup()
  joe.goto(70, 70)
  joe.pendown()
  joe.color("black")
  joe.dot(10)
  joe.hideturtle()
  
def dice4():
  joe.pendown()
  joe.forward(100)
  joe.left(90)
  joe.forward(100)
  joe.left(90)
  joe.forward(100)
  joe.left(90)
  joe.forward(100)
  joe.penup()
  joe.goto(20, 70)
  joe.pendown()
  joe.color("black")
  joe.dot(10)
  joe.penup()
  joe.goto(65, 70)
  joe.pendown()
  joe.color("black")
  joe.dot(10)
  joe.penup()
  joe.goto(22, 20)
  joe.pendown()
  joe.color("black")
  joe.dot(10)
  joe.penup()
  joe.goto(65, 20)
  joe.pendown()
  joe.color("black")
  joe.dot(10)
  joe.hideturtle()
  
def dice5():
  joe.pendown()
  joe.forward(100)
  joe.left(90)
  joe.forward(100)
  joe.left(90)
  joe.forward(100)
  joe.left(90)
  joe.forward(100)
  joe.penup()
  joe.goto(50, 50)
  joe.pendown()
  joe.color("black")
  joe.dot(10)
  joe.penup()
  joe.goto(20, 70)
  joe.pendown()
  joe.color("black")
  joe.dot(10)
  joe.penup()
  joe.goto(70, 70)
  joe.pendown()
  joe.color("black")
  joe.dot(10)
  joe.penup()
  joe.goto(22, 20)
  joe.pendown()
  joe.color("black")
  joe.dot(10)
  joe.penup()
  joe.goto(70, 20)
  joe.pendown()
  joe.color("black")
  joe.dot(10)
  joe.hideturtle()
  
def dice6():
  joe.pendown()
  joe.forward(100)
  joe.left(90)
  joe.forward(100)
  joe.left(90)
  joe.forward(100)
  joe.left(90)
  joe.forward(100)
  joe.penup()
  joe.goto(20, 70)
  joe.pendown()
  joe.color("black")
  joe.dot(10)
  joe.penup()
  joe.goto(45, 70)
  joe.pendown()
  joe.color("black")
  joe.dot(10)
  joe.penup()
  joe.goto(70, 70)
  joe.pendown()
  joe.color("black")
  joe.dot(10)
  joe.penup()
  joe.goto(45, 20)
  joe.pendown()
  joe.color("black")
  joe.dot(10)
  joe.penup()
  joe.goto(22, 20)
  joe.pendown()
  joe.color("black")
  joe.dot(10)
  joe.penup()
  joe.goto(70, 20)
  joe.pendown()
  joe.color("black")
  joe.dot(10)
  joe.hideturtle()

def name():
    global j1,j2,mj1,mj2,m1,m2,ch1,ch2,r,rpi,col1,col2
    print("Vous allez maintenant choisir vos noms")
    j1=input("Joueur 1 veuillez entrer votre nom: ")
    while not j1.isalpha():
        j1=input("Joueur 1 veuillez entrer un vrai nom: ")
    print('Quel est votre couleur préférée parmi ["red","blue","yellow","purple","black","green","orange","pink","grey"]: ')
    col1=input()
    while col1 not in ["red","blue","yellow","purple","black","green","orange","pink","grey"]:
        col1=input("Choisissez une couleur disponible: ")
    print(col1)

    j2=input("Joueur 2 veuillez entrer votre nom: ")
    while not j2.isalpha():
        j2=input("Joueur 2 veuillez entrer un vrai nom: ")
    while j1==j2:
        print("Vous devez entrer des noms différents...")
        j2=input("Joueur 2 veuillez entrer votre nom: ")
        while not j2.isalpha():
            j2=input("Joueur 2 veuillez entrer un vrai nom: ")
    print('Quel est votre couleur préférée parmi ["red","blue","yellow","purple","black","green","orange","pink","grey"]: ')
    col2=input()
    while col2 not in ["red","blue","yellow","purple","black","green","orange","pink","grey"]:
        col2=input("Choisissez une couleur disponible: ")
    print(col2)


def bet():
    global j1,j2,mj1,mj2,m1,m2,ch1,ch2,r,rpi,col1,col2
    m1,m2=0,0
    print("Les joueurs vont procéder à entrer leur mises\n")

    print(j1,",C'est à votre tour")
    time.sleep(0.5)
    ch1=input("Choisissez un nombre entre 1 et 6, «pair» ou «impair»: ")
    while ch1 not in ["1","2","3","4","5","6","pair","impair"]:
        ch1=input("Choisissez un nombre entre 1 et 6, «pair» ou «impair»: ")
    while True:
        m1=input("Choisissez maintenant votre mise: ")
        while not m1.isdigit():
            m1=input("Entrer un nombre: ")
        m1=int(m1)
        if m1>0 and m1<=mj1:
            break

    print("")
    print(j2,",C'est à votre tour")
    time.sleep(0.5)
    ch2=input("Choisissez un nombre entre 1 et 6, «pair» ou «impair»: ")
    while ch2 not in ["1","2","3","4","5","6","pair","impair"]:
        ch2=input("Choisissez un nombre entre 1 et 6, «pair» ou «impair»: ")
    while True:
        m2=input("Choisissez maintenant votre mise: ")
        while not m2.isdigit():
            m2=input("Entrer un nombre: ")
        m2=int(m2)
        if m2>0 and m2<=mj2:
            break
        
    r=random.randint(1,6)
    if r%2==0:
        rpi="pair"
    if r%2==1:
        rpi="impair"
    print("")
    print("Le résultat du lancer du dé est",r,"\n")
    if r==1:
        joe.reset()
        dice1()
    if r==2:
        joe.reset()
        dice2()
    if r==3:
        joe.reset()
        dice3()
    if r==4:
        joe.reset()
        dice4()
    if r==5:
        joe.reset()
        dice5()
    if r==6:
        joe.reset()
        dice6()

    if ch1==str(r):
        m1=m1*5
        mj1=mj1+m1
        print(j1,"Vous avez gagné",m1,"$")
    if ch1==rpi:
        mj1=mj1+m1
        print(j1,"Vous avez gagné",m1,"$")
    if ch1!=str(r) and ch1!=rpi:
        m1=-m1
        mj1=mj1+m1
        print(j1,"Vous avex perdu",abs(m1),"$")
    print("il reste",mj1,"$ dans votre compte\n")
    
    if ch2==str(r):
        m2=m2*5
        mj2=mj2+m2
        print(j2,"Vous avez gagné",m2,"$")
    if ch2==rpi:
        mj2=mj2+m2
        print(j2,"Vous avez gagné",m2,"$")
    if ch2!=str(r) and ch2!=rpi:
        m2=-m2
        mj2=mj2+m2
        print(j2,"Vous avex perdu",abs(m2),"$")
    print("il reste",mj2,"$ dans votre compte\n")


def etoilegagnant(col,j):
    global j1,j2,mj1,mj2,m1,m2,ch1,ch2,r,rpi,col1,col2
    joe.reset()
    joe.penup()
    joe.goto(-100,0)
    joe.pendown()
    joe.pencolor(str(col))
    for i in range(5):
        joe.forward(200)
        joe.left(216)
    joe.penup()
    joe.goto(0,0)
    joe.pendown()
    joe.write(str(j),font=("Calibri", 30, "bold"))  

name()
while True:
    print("Le jeu va commencer!")
    mj1,mj2=120,120
    while mj1>0 and mj2>0:
        bet()
    if mj1==0 and mj2==0:
        print("Tous les joueurs sont a cours d'argent")
        print("Il n'y a pas de gagnant🥲")
    elif mj1==0:
        print(j2,"a gagné la partie!!⭐️")
        print(col2)
        etoilegagnant(col2,j2) 
    elif mj2==0:
        print(j1,"a gagné la partie!!⭐️")
        print(col1)
        etoilegagnant(col1,j1)
    rejouer=input("Voulez-vous rejouer le jeu de dé?: ")
    while rejouer not in ["non","oui","Non","Oui"]:
        rejouer=input("Répondez oui ou non: ")
    if rejouer in ["non","Non"]:
        print("Au plaisir de vous revoir!")
        break




