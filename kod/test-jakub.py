import tkinter as tk

root = tk.Tk()

sheet = tk.PhotoImage(file="../img/sprite.png")

sprite_w = 32
sprite_h = 32

def show_sprite(col, row):
    canvas = tk.Canvas(
        root, width=sprite_w, height=sprite_h,
        highlightthickness=0
    )
    canvas.pack()

    # col a row určujú pozíciu sprite-u v mriežke
    canvas.create_image(
        -col * sprite_w,
        -row * sprite_h,
        image=sheet,
        anchor="nw"
    )

show_sprite(0, 0)  # prvý sprite
show_sprite(1, 0)  # druhý sprite v prvom riadku
show_sprite(0, 1)  # prvý sprite v druhom riadku

root.mainloop()