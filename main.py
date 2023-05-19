from tkinter import *
import time
from PIL import Image, ImageTk
#############################################
from barra import *
from bola import *
#############################################
Bola = Bola
Barra = Barra
#############################################
def set_level(event):
    global level, length
    level = int(level_entry.get())
    length = 300 / level
    level_label.destroy()
    level_entry.destroy()
    submit_button.destroy()
    init_game()
#############################################
def init_game():
    global Barra, Bola, score_now, game, count, lost
    Barra = Barra(canvas, length)
    Bola = Bola(canvas, Barra, game_over, score)

    score_now = canvas.create_text(370, 20, text="Você acertou " + str(count) + "x", fill="white", font=("Arial", 20))
    game = canvas.create_text(400, 300, text=" ", fill="white", font=("Arial", 40))

    #canvas.bind_all("<Button-1>", start_game)

    start_game()
#############################################
def start_game(event=None):
    global lost, count
    lost = False
    count = 0
    score()
    canvas.itemconfig(game, text=" ")
    time.sleep(1)
    Barra.draw()
    Bola.draw()
#############################################
def score():
    global count
    count += 1
    canvas.itemconfig(score_now, text="Você acertou " + str(count - 1) + "x")
#############################################
def game_over():
    canvas.itemconfig(game, text="Game over!", fill='yellow', font=("Arial", 70, "bold"))

#############################################

root = Tk()
root.title("Ping Pong")
root.resizable(0, 0)
root.wm_attributes("-topmost", 1)

canvas = Canvas(root, width=800, height=600, bd=0, highlightthickness=0)
canvas.pack()

background_image_path = "BGImage.png"
bg_image = Image.open(background_image_path)
bg_photo = ImageTk.PhotoImage(bg_image)

canvas.create_image(0, 0, image=bg_photo, anchor=NW)

level_label = Label(root, text="Qual nível você gostaria de jogar? [Entre 1 e 10] ", font=("Arial", 20, "italic"))
level_label.pack()
level_entry = Entry(root, font=("Arial", 20), background="yellow", width=5)
level_entry.pack()
submit_button = Button(root, text="Jogar", background="green", width=6, font=("Arial", 15), command=lambda: set_level(None))
submit_button.pack()
submit_button.bind("<Return>", set_level)

root.mainloop()
