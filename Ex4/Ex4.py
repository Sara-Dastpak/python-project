'''
Sara Dastpak
4012061016
'''
# calculating the position of each piece
def position(letter, number):
    mapping_dic = {"a":1, "b": 2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8}
    coordinate = []
    coordinate.append(mapping_dic[letter])
    coordinate.append(number)
    return coordinate
# calculating any posible place that knight can be in
def possible_place_bishop(coorlist):
    possible = []
    i = coorlist[0]
    j = coorlist[1]
    while i < 8 and j < 8:
        i = i + 1
        j = j + 1
        possible.append([i , j])
    i = coorlist[0]
    j = coorlist[1]
    while i > 1 and j < 8:
        i = i - 1
        j = j + 1
        possible.append([i , j])
    i = coorlist[0]
    j = coorlist[1]
    while i > 1 and j > 1:
        i = i - 1
        j = j - 1
        possible.append([i , j])
    i = coorlist[0]
    j = coorlist[1]
    while i < 8 and j > 1:
        i = i + 1
        j = j - 1
        possible.append([i , j])
    return possible
# calculating any posible place that bishop can be in
def possible_place_knight(coorlist):
    possible = []
    i = coorlist[0]
    j = coorlist[1]
    if i + 2 < 8 and j + 1 < 8:
        possible.append([i + 2, j + 1])
    if i - 2 > 1 and j + 1 < 8:
        possible.append([i - 2, j + 1])
    if i - 2 > 1 and j - 1 > 1:
        possible.append([i - 2, j - 1])
    if i + 2 < 8 and j - 1 > 1:
        possible.append([i + 2, j - 1])
    if i + 1 < 8 and j + 2 < 8:
        possible.append([i + 1, j + 2])
    if i - 1 > 1 and j + 2 < 8:
        possible.append([i - 1, j + 2])
    if i - 1 > 1 and j - 2 > 1:
        possible.append([i - 1, j - 2])
    if i + 1 < 8 and j - 2 > 1:
        possible.append([i + 1, j - 2])
    return possible
def EX4():
    alphabet = ['a','b','c','d','e','f','g','h']
    knight_hrz = input("Please enter horizontal position of the knight(a,b,c,d,e,f,g,h): ")
    knight_hrz = knight_hrz.lower()
    if len(knight_hrz) > 1:
        return "Horizontal input is not a letter"
    elif knight_hrz not in alphabet:
        return "Horizontal input is not a proper letter"
    knight_vrt = int(input("Please enter vertical position of the knight(1,2,3,4,5,6,7,8): "))
    if knight_vrt > 8:
        return "Vertical input for knight is not a proper number"
    bishop_hrz = input("Please enter horizontal position of the bishop(a,b,c,d,e,f,g,h): ")
    bishop_hrz = bishop_hrz.lower()
    if len(bishop_hrz) > 1:
        return "Horizontal input is not a letter"
    elif bishop_hrz not in alphabet:
        return "Horizontal input is not a proper letter"
    bishop_vrt = int(input("Please enter vertical position of the beshop(1,2,3,4,5,6,7,8): "))
    if bishop_vrt > 8:
        return "Vertical input for bishop is not a proper number"
    if knight_hrz == bishop_hrz and knight_vrt == bishop_vrt:
        return "They can't be in the same square"
    knight_coor = position(knight_hrz, knight_vrt)
    bishop_coor = position(bishop_hrz, bishop_vrt)
    knight_places = possible_place_knight(knight_coor)
    bishop_places = possible_place_bishop(bishop_coor)
    for item in knight_places:
        if item == bishop_coor:
            return "Knight can attack bishop"
    for item in bishop_places:
        if item == knight_coor:
            return "Bishop can attack knight"
    else:
        return "Nither of them can attack each other"
print(EX4())
