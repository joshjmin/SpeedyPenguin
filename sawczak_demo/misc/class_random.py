from tkinter import *

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 700

root = Tk()
root.geometry(f'{SCREEN_WIDTH}x{SCREEN_HEIGHT}')

canvas = Canvas(root, width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
canvas.pack()

class Block:

    def __init__(self, x: int, y: int, side: int, colour: str, speed: int):
        self.x = x
        self.y = y
        self.side = side
        self.colour = colour
        self.speed = speed

        self.canvas_obj = canvas.create_rectangle(x, y, x + side, y + side, fill=colour)

    def fall(self):
        self.y += self.speed
        canvas.move(self.canvas_obj, 0, self.speed)

block_1 = Block(0, 0, 20, 'blue', 50)
block_2 = Block(20, 0, 20, 'green', 50)
block_3 = Block(40, 0, 20, 'yellow', 50)
block_4 = Block(60, 0, 20, 'red', 50)
block_5 = Block(80, 0, 20, 'purple', 50)


def make_block_fall():
    if block_1.y < SCREEN_HEIGHT:
        block_1.fall()
        root.after(1000, make_block_fall)

root.after(1000, make_block_fall)
root.mainloop()
