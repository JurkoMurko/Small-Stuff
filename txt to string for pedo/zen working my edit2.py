from sndhdr import what
from PIL import Image
import os
import numpy as np
import random

def printVar(var):
    print(f"{var=}")

def init_charImageList():
    for item in dirs3:
        fullpath = os.path.join(path3, item)
        if os.path.isfile(fullpath):
            im = Image.open(fullpath)
            charImageList.append(im)


def Translator(wordsString):
    last = -4
    wordList = wordsString.split()
    print(wordList)
    print(len(wordList))

    for i in range(0, len(wordList)):
        print(f"{wordList=}")
        letterList = [x for x in wordList[i]]
        print(f"{letterList=}")
        for i in range(0, len(letterList)):
            if letterList[i] == "n" and last == -3:
                writeIT.append(-2)
            elif letterList[i] == "t" and last == -3:
                writeIT.append(-3)
            elif letterList[i] == "\\":
                last = -3
            else:
                writeIT.append(keySplit.index(letterList[i]) + 1)
                last = keySplit.index(letterList[i]) + 1
        writeIT.append(-1)
        last = -1


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


def paster2(wordString):
    xtraD = 0
    xtraH = 0
    bgImageCopy = bgImage.copy()

    for letter in wordString:
        letterImage = findImage(letter)
        
        if line == 1:
            letterImage = letterImage.resize((int(np.round(letterImage.width * random.uniform(2.90, 3.10))), int(np.round(letterImage.height * random.uniform(2.90, 3.10)))), Image.NEAREST)
        else:
            letterImage = letterImage.resize((int(np.round(letterImage.width * random.uniform(.90, 1.10))), int(np.round(letterImage.height * random.uniform(.90, 1.10)))), Image.NEAREST)

        bgImageCopy.paste(letterImage, (625 + xtraD, 1271 + xtraH - letterImage.height))

        xtraD += letterImage.width + random.randint(- np.round(letterImage.width/8), np.round(letterImage.width/8))
        xtraD += 10 + random.randint(0, 4)

    bgImageCopy.save('rocket_pillow_paste_pos.jpg',  quality=100)


def findImage(letter):
    if letter.isupper():
        return Image.open(f"{path3}\z{letter}.png")
    elif letter.islower() :
        return Image.open(f"{path3}\{letter}.png")
    elif letter == " ":
        print(6)
        return Image.open(r"G:\My Drive\juraj@andrews\Code\Small Shit\txt to string for pedo\img folder" + "\\space.png")
    else:
        raise Exception("fuck of with your fancy letter shit")


def paster(indexList):
    global line
    xtraD = 0
    xtraH = 0
    bgImageCopy = bgImage.copy()

    for i in range(0, len(indexList)):
        if indexList[i] == -1:
            xtraD += 125
        elif indexList[i] == -3:
            xtraD += 500
        elif indexList[i] == -2:
            xtraH += 250
            xtraD = 0
            line += 1
        else:
            letterImage = charImageList[indexList[i] - 1]

            if line == 1:
                letterImage = letterImage.resize((int(np.round(letterImage.width * random.uniform(2.90, 3.10))), int(
                    np.round(letterImage.height * random.uniform(2.90, 3.10)))), Image.NEAREST)
            else:
                letterImage = letterImage.resize((int(np.round(letterImage.width * random.uniform(.90, 1.10))), int(
                    np.round(letterImage.height * random.uniform(.90, 1.10)))), Image.NEAREST)

            if indexList[i] in mDTrans:
                bgImageCopy.paste(letterImage, (625 + xtraD, 1271 - int(
                    np.round(letterImage.height - (letterImage.height * random.uniform(.20, .50)) + xtraH))))
            elif indexList[i] in mUTrans:
                bgImageCopy.paste(
                    letterImage, (625 + xtraD, 1271 - int(np.round(letterImage.height * random.uniform(1.3, 1.6) + xtraH))))
            elif indexList[i] in mFUTrans:
                bgImageCopy.paste(
                    letterImage, (625 + xtraD, 1271 - int(np.round(letterImage.height * random.uniform(2.5, 3.2) + xtraH))))
            else:
                bgImageCopy.paste(
                    letterImage, (625 + xtraD, 1271 + xtraH - letterImage.height))

            xtraD += letterImage.width + \
                random.randint(- np.round(letterImage.width/8), np.round(letterImage.width/8))
        xtraD += 10 + random.randint(0, 4)

    bgImageCopy.save('rocket_pillow_paste_pos.jpg',  quality=100)

# ----------------------------------------------------------------------------------------------------------

lowerPath = "image folder\\lowercase"
longPath = r"G:\My Drive\juraj@andrews\Code\Small Shit\txt to string for pedo\img folder"
path3 = "img folder"
bgImage_path = r"paper\paper.jpg"

dirs3 = os.listdir(path3)

line = 1

charImageList = []

typeIT = []
writeIT = []
key = """abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789()!<>?.,^:_+-*/=%$&€"';[]#"""
keySplit = [*key]

moveDown = "jgyp,."
mDSplit = [*moveDown]
moveUp = """^'_"<>="""
moveFUp = """^"'"""
mUSplit = [*moveUp]
mFUSplit = [*moveFUp]

mDTrans = []
mUTrans = []
mFUTrans = []

# ----------------------------------------------------------------------------------------------------------

# init_charImageList()
bgImage = Image.open(bgImage_path)

whatUWant = input("what do you want to type?:    ")
# Translator(whatUWant)
# print(Tran2(whatUWant))
# paster(writeIT)
paster2(whatUWant)
