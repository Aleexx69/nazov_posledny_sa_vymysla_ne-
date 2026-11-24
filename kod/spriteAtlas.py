import sys
import cv2


# TO ZAPNEM TAK ZE: cd kod, a potom "python a nazov programu lolol"

## import img
try:
    img=cv2.imread("../img/sprite.png",cv2.IMREAD_ANYCOLOR)
except IOError:
    print("nigger")

tile_first = img[0:32, 0:32]      #vykreslenie prvej casti obrazka, prvý parameter je riadok a druhý je stĺpec
                                  #sprite ma velkost 32 na 32 


while True:
    cv2.imshow("test",tile_first)
    cv2.imshow("dsds", img)        #ukaze obrazok
    nazov_posledny_sa_vymysla_ne = tk.Tk()                                #nazov
    nazov_posledny_sa_vymysla_ne.title('Niggerrssss')                     #title okna ig
    nazov_posledny_sa_vymysla_ne.geometry('512x512')                      #šírka x výška px
    imagessss = tk.PhotoImage(file="../img/sprite.png", width=32, height=32)                   #imagessss - nazov obrazka, tk.photoimage - vykreslenie obrázka, umiestnenie
    image_label = tk.Label(nazov_posledny_sa_vymysla_ne, image=imagessss) #priradenie, ze kde sa ma vykreslit, a ktorý presne
    image_label.pack()                                                    
    nazov_posledny_sa_vymysla_ne.mainloop()
    cv2.waitKey(0)
    sys.exit()

## split img



##save to list
