from tkinter import *
import time
from PIL import Image, ImageTk

from barra import *
from bola import *

Bola = Bola
Barra = Barra

def set_level(event):
    global level, length
    level = int(level_entry.get())
    length = 500 / level
    level_label.destroy()
    level_entry.destroy()
    submit_button.destroy()
    init_game()

def init_game():
    global Barra, Bola, score_now, game
    Barra = Barra(canvas, length, "olive")
    Bola = Bola(canvas, Barra, "white")

    score_now = canvas.create_text(370, 20, text="Você acertou " + str(count) + "x", fill="lime", font=("Arial", 20))
    game = canvas.create_text(400, 300, text=" ", fill="white", font=("Arial", 40))

    canvas.bind_all("<Button-1>", start_game)

    start_game()

def start_game(event=None):
    global lost, count
    lost = False
    count = 0
    score()
    canvas.itemconfig(game, text=" ")
    time.sleep(1)
    Barra.draw()
    Bola.draw()

def score():
    canvas.itemconfig(score_now, text="Você acertou " + str(count) + "x")

#def game_over():
#    canvas.itemconfig(game, text="Game over!")

root = Tk()
root.title("Ping Pong")
root.resizable(0, 0)
root.wm_attributes("-topmost", 1)
#root.iconbitmap('gameico.ico')

canvas = Canvas(root, width=800, height=600, bd=0, highlightthickness=0)
canvas.pack()

background_image_path = "BGImage.png"
bg_image = Image.open(background_image_path)
bg_photo = ImageTk.PhotoImage(bg_image)

canvas.create_image(0, 0, image=bg_photo, anchor=NW)

level_label = Label(root, text="Qual nível você gostaria de jogar? 1/2/3/4/5", font=("Arial", 20))
level_label.pack()
level_entry = Entry(root, font=("Arial", 20))
level_entry.pack()
submit_button = Button(root, text="Enviar", font=("Arial", 20), command=lambda: set_level(None))
submit_button.pack()
submit_button.bind("<Return>", set_level)

root.mainloop()
