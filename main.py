from tkinter import *
from tkinter.ttk import *
from tkinter.scrolledtext import *
from PIL import Image, ImageTk
import tkinter.font as font
import random

p_score = 0
c_score = 0


def result(player):
    global p_score
    global c_score
    comp = random.choice(["Rock", "Paper", "Scissor"])
    if (player == comp):
        disp_lbl.config(
            text="Computer chose {} and the Turn is a Tie".format(comp))
        p_score += 1
        c_score += 1
        disp_lbl_2.config(
            text="Score: {}:{} [player:computer]".format(p_score, c_score))
    elif ((player == "Rock" and comp == "Paper") or (player == "Paper" and comp == "Scissor") or (player == "Scissor" and comp == "Rock")):
        disp_lbl.config(
            text="Computer chose {} and Computer wins this Turn".format(comp))
        c_score += 2
        disp_lbl_2.config(
            text="Score: {}:{} [player:computer]".format(p_score, c_score))
    else:
        disp_lbl.config(
            text="Computer chose {} and You win this Turn".format(comp))
        p_score += 2
        disp_lbl_2.config(
            text="Score: {}:{} [player:computer]".format(p_score, c_score))


def rock_com():
    player = "Rock"
    result(player)


def paper_com():
    player = "Paper"
    result(player)


def scissor_com():
    player = "Scissor"
    result(player)


def final_sc():
    global p_score
    global c_score
    disp_lbl.config(text="Thank you for Playing !!")
    disp_lbl_2.config(
        text="Final Score: {}:{} [player:computer]".format(p_score, c_score))


def new_game():
    global p_score
    global c_score
    p_score = 0
    c_score = 0
    disp_lbl.config(text="Let's Begin the Game!!")
    disp_lbl_2.config(text="Scoreboard")


root = Tk()
root.title("Rock Paper Scissor")
root.geometry("700x850")
root.resizable(0, 0)
root.iconbitmap("Icon.ico")
img = Image.open("banner.jpg")
photo = ImageTk.PhotoImage(img)
lab = Label(image=photo).place(x=0, y=50)
title = Label(root, text="Rock Paper Scissor",
              font="Gotham_black 25 bold underline",
              anchor="center").place(x=190, y=5)
choose = Label(root, text="Choose your Weapon!!",
               font="Gotham_black 25 bold", anchor="center").place(x=170, y=400)
photo1 = PhotoImage(file="Rock.png")
tphoto1 = photo1.subsample(6, 6)
rock_btn = Button(root, image=tphoto1, command=rock_com).place(x=10, y=470)
photo2 = PhotoImage(file="Paper.png")
tphoto2 = photo2.subsample(6, 6)
paper_btn = Button(root, image=tphoto2, command=paper_com).place(x=270, y=470)
photo3 = PhotoImage(file="Scissor.png")
tphoto3 = photo3.subsample(6, 6)
paper_btn = Button(root, image=tphoto3,
                   command=scissor_com).place(x=530, y=470)
disp_lbl = Label(root, background="red", width=54, text="Let's Begin the Game!!",
                 font="Gotham_black 18 bold", anchor=S, justify=CENTER)
disp_lbl.place(x=0, y=650)
disp_lbl_2 = Label(root, background="red", width=39, text="Scoreboard",
                   font="Gotham_black 25 bold", anchor=S, justify=CENTER)
disp_lbl_2.place(x=0, y=700)
style = Style()
style.configure('W.TButton', font=('Gotham_black', 25, 'bold'),
                foreground='red', background="yellow")
fin_button = Button(root, text='Final Score',
                    style='W.TButton', command=final_sc).place(x=10, y=770)
new_button = Button(root, text='New Game',
                    style='W.TButton', command=new_game).place(x=480, y=770)
root.mainloop()
