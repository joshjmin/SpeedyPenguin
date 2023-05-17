import tkinter

# Set up the window
window = tkinter.Tk()
window.title('My very first tkinter GUI')
window.geometry('400x400')

# Create a canvas
canvas = tkinter.Canvas(window, height=400, width=400)
canvas.pack()

# Create a background
background1 = canvas.create_rectangle(0, 0, 200, 200, fill='red')
background3 = canvas.create_rectangle(200, 0, 400, 200, fill='green')
background2 = canvas.create_rectangle(200, 200, 400, 400, fill='yellow')
background4 = canvas.create_rectangle(0, 200, 200, 400, fill='blue')

# Create some text
text = tkinter.StringVar()
text.set('Windows 95')

label = tkinter.Label(canvas, textvariable=text, fg='white', bg='black', font=("Courier New", 24))
label.pack()

canvas.create_window(200, 200, window=label)

# Main loop
window.mainloop()
