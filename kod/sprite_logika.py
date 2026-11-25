from pathlib import Path
import tkinter as tk

root = tk.Tk()
root.title("Sprite atlas")

sprite_w = 32
sprite_h = 32

sheet_path = Path(__file__).resolve().parent.parent / "img" / "sprite.png"
sheet = tk.PhotoImage(file=str(sheet_path))


def get_sprite(col, row):
    #Vystrihne jeden 32x32 sprite zo sprite atlasu 
    x = col * sprite_w
    y = row * sprite_h
    sprite = tk.PhotoImage(width=sprite_w, height=sprite_h)
    root.tk.call(sprite, "copy", sheet, "-from", x, y, x + sprite_w, y + sprite_h)
    return sprite


def rotate_90(sprite):
    #Otočí tkinter PhotoImage o 90° proti smeru hodinových ručičiek
    w, h = sprite.width(), sprite.height()
    out = tk.PhotoImage(width=h, height=w)
    rows = []
    transparent = []
    for ny in range(w):
        row = []
        for nx in range(h):
            ox, oy = w - 1 - ny, nx
            if sprite.transparency_get(ox, oy):
                row.append("#000000")
                transparent.append((nx, ny))
            else:
                r, g, b = sprite.get(ox, oy)
                row.append(f"#{r:02x}{g:02x}{b:02x}")
        rows.append("{" + " ".join(row) + "}")
    out.put(" ".join(rows))
    for nx, ny in transparent:
        out.transparency_set(nx, ny, True)
    return out


def flip_variants(sprite):
    #Vráti zoznam variantov: originál, horizontálne, vertikálne, oboje.
    return [
        sprite,
        sprite.subsample(-1, 1),   # horizontálne otočenie
        sprite.subsample(1, -1),   # vertikálne otočenie
        sprite.subsample(-1, -1),  # horizontálne aj vertikálne otočenie (180°)
    ]


# Jednoduché listy rozdelené podľa kategórií zo sprite atlasu
voda_coords = [(0, 0), (1, 0), (2, 0), (3, 0)]
voda = [get_sprite(col, row) for col, row in voda_coords]

cesta_roh = get_sprite(7, 0)
cesta_rovna = get_sprite(8, 0)
cesta_rovna_90 = rotate_90(cesta_rovna)
cesta = (
    flip_variants(cesta_roh)
    + flip_variants(cesta_rovna)
    + [
        cesta_rovna_90,                    # vertikálna cesta (90°)
        cesta_rovna_90.subsample(-1, -1),  # vertikálna cesta (270°)
    ]
)

# Postavy (goblin, netopier, duch/rytier, príšera, lukostrelec, čarodejník)
postavy_coords = [(0, 1), (1, 1), (2, 1), (3, 1), (5, 1), (6, 1)]
postavy = [get_sprite(col, row) for col, row in postavy_coords]

# Zvyšné veci (brehy, tráva, delo, strely, efekty výbuchu, S/E značky, kryštály)
# Pozn.: delo (4, 1) je tu medzi objektmi; ak ho chceš ako postavu, stačí presunúť súradnicu do postavy_coords
ostatne_coords = [
    (4, 0), (5, 0), (6, 0), (9, 0),
    (4, 1), (7, 1), (8, 1), (9, 1),
    (0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2),
    (7, 2), (8, 2), (9, 2),
]
ostatne = [get_sprite(col, row) for col, row in ostatne_coords]


def show_sprite(sprite, grid_col, grid_row):
    canvas = tk.Canvas(
        root, width=sprite_w, height=sprite_h,
        bg="#787878", highlightthickness=0
    )
    canvas.grid(row=grid_row, column=grid_col, padx=2, pady=2)
    canvas.create_image(0, 0, image=sprite, anchor="nw")


def show_list(nazov, sprites, grid_row):
    tk.Label(root, text=nazov, anchor="w").grid(row=grid_row, column=0, sticky="w", padx=6)
    for i, sprite in enumerate(sprites, start=1):
        show_sprite(sprite, i, grid_row)


show_list("Voda:", voda, 0)
show_list("Cesta:", cesta, 1)
show_list("Postavy:", postavy, 2)
show_list("Ostatné:", ostatne, 3)

root.mainloop()