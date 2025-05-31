import tkinter as tk

WIDTH = 400
HEIGHT = 400

# main window
root = tk.Tk()
root.title("Snake | Score: 0")
root.resizable(False, False)

# add game field
canvas = tk.Canvas(
    root, 
    width=WIDTH,
    height=HEIGHT,
    bg="black",
    highlightthickness=0
)

canvas.pack()

# execute main cycle
root.mainloop()