# EFEITOS NA BARRA ##########################

bar_color='red'
bar_border=7
bar_b_color='green'
bar_height=10
bar_distance=450

#############################################
lost = False

class Barra:
    def __init__(self, canvas, length):
        self.canvas = canvas
        self.length = length
        self.id = canvas.create_rectangle(0, 0, length, bar_height, fill=bar_color, width=bar_border, outline=bar_b_color)
        self.canvas.move(self.id, 200, bar_distance)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all("<KeyPress-Left>", self.move_left)
        self.canvas.bind_all("<KeyPress-Right>", self.move_right)

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        self.pos = self.canvas.coords(self.id)

        if self.pos[0] <= 0:
            self.x = 0

        if self.pos[2] >= self.canvas_width:
            self.x = 0

        global lost

        if lost == False:
            self.canvas.after(10, self.draw)

    def move_left(self, event):
        if self.pos[0] >= 0:
            self.x = -3

    def move_right(self, event):
        if self.pos[2] <= self.canvas_width:
            self.x = 3