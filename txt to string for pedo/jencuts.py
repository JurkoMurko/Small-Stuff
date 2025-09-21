from PIL import Image
import random

# def init_charImageList():
#     for item in dirs3:
#         fullpath = os.path.join(imgFolder, item)
#         if os.path.isfile(fullpath):
#             im = Image.open(fullpath)
#             charImageList.append(im)


# def Tran2(wordString):
#     numberList = []
#     print(f"{wordString=}")
#     for word in wordString.split():
#         print(f"{word=}")
#         for letter in word:
#             if letter == "\\":
#                 if letter == "t":
#                     numberList.append(-3)
#                 elif letter == "n":
#                     numberList.append(-2)
#             else:
#                 print(f"{letter=}")
#                 numberList.append(keySplit.index(letter) + 1)
#         numberList.append(-1)
#     return numberList


def paster(wordString):
    bgImage = Image.open(bgImage_path)
    xtraD = 0
    xtraH = 0
    bgImageCopy = bgImage.copy()
    
    for letter in wordString:
        tempHeight = 0

        if letter == " ":
            xtraD += 90
            continue
        
        letterImage = findImage(letter)

        if letter in "jgyp,.":
            tempHeight -= int(letterImage.height/2)
        
        if letter in """^'_"<>=""":
            xtraD += int(letterImage.height/2)
        
        randHeight = int(letterImage.height * random.uniform(.90, 1.10) * 1)
        randWidth = int(letterImage.width * random.uniform(.90, 1.10) * 1)
        letterImage = letterImage.resize((randWidth, randHeight), Image.NEAREST)

        if xtraD + 625 + 100 + letterImage.width > bgImage.width:
            xtraD = 0
            xtraH += 200

        bgImageCopy.paste(letterImage, (625 + xtraD, 1271 + xtraH - tempHeight - letterImage.height))

        xtraD += letterImage.width + random.randint(0,20)

    bgImageCopy.save('rocket_pillow_paste_pos.jpg',  quality=100)


def findImage(letter):
    if letter.isupper():
        return Image.open(f"{imgFolder}\z{letter}.png")
    elif letter.islower() :
        return Image.open(f"{imgFolder}\{letter}.png")
    else:
        try:
            return Image.open(f"{imgFolder}\{letter}.png")
        except FileNotFoundError as err:
            raise Exception(f"fuck of with your fancy letter shit {letter}doesn't have a file", err)


imgFolder = "images"
bgImage_path = r"paper\paper.jpg"

# dirs3 = os.listdir(imgFolder)
# line = 1
# charImageList = []

whatUWant = input("what do you want to type?:    ")
paster(whatUWant)
