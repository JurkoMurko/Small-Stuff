from PIL import Image
import os
import numpy as np
import random

path3 = "img folder"
path4 = "paper"

dirs3 = os.listdir(path3)
dirs4 = os.listdir(path4)

line = 1

charList = []

def listTime():
    global im1

    for item in dirs3:
        fullpath = os.path.join(path3, item)

        if os.path.isfile(fullpath):
            im = Image.open(fullpath)
            charList.append(im)

    for item in dirs4:
        fullpath = os.path.join(path4, item)
        if os.path.isfile(fullpath):
            im1 = Image.open(fullpath)

listTime()

xtraH = 0
next = False

typeIT = []
writeIT = []
key = """abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789()!<>?.,^:_+-*/=%$&€"';[]#"""
keySplit = [*key]

moveDown = "jgyp,."
moveUp = """^'_"<>="""
moveFUp = """^"'"""
mDSplit = [*moveDown]
mUSplit = [*moveUp]
mFUSplit = [*moveFUp]

whatUWant = input("what do you want to type?    ")

mDTrans = []
mUTrans = []
mFUTrans = []

def Translator(w):
    global back_im
    typeIT = w.split()
    print(typeIT)
    print(len(typeIT))
    for i in range(0, len(typeIT)):
        lets = [x for x in typeIT[i]]
        next = False
        for i in range(0, len(lets)):
            if lets[i] == " ":
                writeIT.append(-2)

            else:

                writeIT.append(keySplit.index(lets[i]) + 1)
        writeIT.append(-1)

def Translator2(w, writeIT):
    for i in range(0, len(w)):
        writeIT.append(keySplit.index(w[i]) + 1)
    print(f"this is {writeIT}")

Translator2(mDSplit, mDTrans)
Translator2(mUSplit, mUTrans)
Translator2(mUSplit, mFUTrans)

def paster(w):
    global line
    xtraD = 0
    xtraH = 0
    back_im = im1.copy()
    print(w)
    for i in range(0, len(w)):
        if w[i] == -1:
            xtraD += 125
        elif w[i] == -2:
            xtraH += 250
            xtraD = 0
            line += 1
        else:
            im2 = charList[w[i] - 1]
            if line == 1:
                im2 = im2.resize((int(np.round(im2.width * random.uniform(2.90, 3.10))), int(
                    np.round(im2.height * random.uniform(2.90, 3.10)))), resample = Image.Resampling.NEAREST)
            else:
                im2 = im2.resize((int(np.round(im2.width * random.uniform(.90, 1.10))), int(
                    np.round(im2.height * random.uniform(.90, 1.10)))), Image.Resampling.NEAREST)

            if w[i] in mDTrans:
                print("\n\ndown")
                back_im.paste(
                    im2, (625 + xtraD, 1271 + int(np.round(im2.height * random.uniform(1.10, 1.40) + xtraH))))

            elif w[i] in mUTrans:
                print("up")
                back_im.paste(
                    im2, (625 + xtraD, 1271 - int(np.round(im2.height * random.uniform(1.3, 1.6) + xtraH))))

            elif w[i] in mFUTrans:
                print("FUP")
                back_im.paste(
                    im2, (625 + xtraD, 1271 - int(np.round(im2.height * random.uniform(2.5, 3.2) + xtraH))))

            else:
                print("else")
                back_im.paste(im2, (625 + xtraD, 1271 - xtraH - im2.height))

            xtraD += im2.width + \
                random.randint(- np.round(im2.width/8), np.round(im2.width/8))
        xtraD += 10 + random.randint(0, 4)
    f, e = os.path.splitext(path)
    back_im.save(f + 'rocket_pillow_paste_pos.jpg',  quality=100)

def paster2(w):
    xtraD = 0

    back_im = im1.copy()
    for i in range(0, 50):
        print("in")
        im2 = charList[i]
        back_im.paste(im2, (625 + xtraD, 1271 - im2.height))
        xtraD += im2.width
        f, e = os.path.splitext(path)

    back_im.save(f + 'rocket_pillow_paste_pos.jpg', quality=95)

xtraH = 0
Translator(whatUWant)
print(f"------>")
paster(writeIT)
