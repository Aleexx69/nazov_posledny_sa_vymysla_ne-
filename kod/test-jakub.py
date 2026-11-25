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

show_sprite(0, 0)  # prvý sprite voda
show_sprite(1, 0)  # druhý sprite v prvom riadku voda2
show_sprite(2,0)
show_sprite(3,0)
show_sprite(4,0)
show_sprite(5,0)
show_sprite(6,0)
show_sprite(7,0)
show_sprite(8,0)
show_sprite(9,0)

show_sprite(0, 1)  # prvý sprite v druhom riadku
show_sprite(1, 1)
show_sprite(2, 1)
show_sprite(3, 1)
show_sprite(4, 1)
show_sprite(5, 1)
show_sprite(6, 1)
show_sprite(7, 1)
show_sprite(8, 1)
show_sprite(9, 1)

show_sprite(0, 2)  # prvý sprite v druhom riadku
show_sprite(1, 2)
show_sprite(2, 2)
show_sprite(3, 2)
show_sprite(4, 2)
show_sprite(5, 2)
show_sprite(6, 2)
show_sprite(7, 2)
show_sprite(8, 2)
show_sprite(9, 2)

root.mainloop()