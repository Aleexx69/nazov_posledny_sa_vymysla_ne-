import sys
import cv2


# TO ZAPNEM TAK ZE: cd kod, a potom "python a nazov programu lolol"

## import img

try:
    img=cv2.imread("../img/sprite.png",cv2.IMREAD_ANYCOLOR)
except IOError:
    print("nigger")

while True:
    cv2.imshow("test",img)
    cv2.waitKey(0)
    sys.exit()

## split img



##save to list