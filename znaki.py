# definicje wyglądu cyferek
#        1    2    3    4    5    6    7
#      12345123451234512345123451234512345
zer = "01110100011000110001100011000101110"
jed = "01100001000010000100001000010011111"
dwa = "01110100010000100010001000100011111"
trz = "01110100010000100110000011000101110"
czt = "00010001100101010010111110001000010"
pie = "11111100001111000001000011000101110"
sze = "01110100011000011110100011000101110"
sie = "11111000010001000100010000100001000"
osi = "01110100011000101110100011000101110"
dzi = "01110100011000101111000011000101110"
#      12345123451234512345123451234512345

def znak(sx, zn): # sx - przesunięcie w prawo o ilość pixeli, zn - znak do wyświetlenia
    z = 0
    for y in range(1,8):
        for x in range(5):
            if sx+x <= 15:
                display1.set_pixel(sx+x, y, int(zn[z]))
            elif sx+x > 15:
                display2.set_pixel(sx+x-16, y, int(zn[z]))
            z = z + 1

