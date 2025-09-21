from asyncore import write
import PIL

from PIL import Image
import os.path, sys
import numpy as np
from os import listdir
import time
import random
# path = "C:\\Users\\quint\\OneDrive\\Desktop\\handwriting\\letters"
# path2 = "C:\\Users\\quint\\OneDrive\\Desktop\\handwriting\\letters\\cropped"
path3 = "img folder"
path4 = "paper"

# dirs = os.listdir(path)
# dirs2 = os.listdir(path2)
dirs3 = os.listdir(path3)
dirs4 = os.listdir(path4)

line = 1

# def crop():
#     path 
#     for item in dirs:
#         fullpath2 = os.path.join(path,item)
#         fullpath = os.path.join(path + "\\cropped",item)         #corrected
#         if os.path.isfile(fullpath2):
#             im = Image.open(fullpath2)
#             f, e = os.path.splitext(fullpath)
#             imCrop = im.crop((13, 90, 213, 330)) #corrected
#             imCrop.save(f + 'CroppedTwice.png', "PNG", quality=100)

# ##crop()

# def crop2():
    
#     n = 0
#     for item in dirs2:
#         fullpath = os.path.join(path2 + "\\zoomed",item)
#         fullpath2 = os.path.join(path2,item)    
        
         
#           #corrected
#         if os.path.isfile(fullpath2):
#             print("AHHHHH")
#             im = Image.open(fullpath2)
#             print(item)
            
#             g, e = os.path.splitext(path2 + "\\zoomed\\")
#             print(bbox(im))  # (33, 12, 223, 80)
#             im2 = im.crop(bbox(im))
#             if n < 10:
#                 im2.save(g + "0" + str(n * 10) +'.png', "PNG", quality=100)
#                 print(g + str(n * 10) +'.png') 
#             else:
#                 im2.save(g + str(n * 10) +'.png', "PNG", quality=100)
#                 print(g + str(n * 10) +'.png') 
            
#         n += 1
charList = []
def listTime():
    global im1
    
    for item in dirs3:
        fullpath = os.path.join(path3,item)
          
        
        if os.path.isfile(fullpath):
            im = Image.open(fullpath)
            charList.append(im)
    

    for item in dirs4:
        fullpath = os.path.join(path4,item)
        if os.path.isfile(fullpath):
            im1 = Image.open(fullpath)
            

listTime()

xtraH = 0
next = False
def bbox(im):
    a = np.array(im)[:,:,:3]  # keep RGB only
    m = np.any(a != [255, 255, 255], axis=2)
    coords = np.argwhere(m)
    y0, x0, y1, x1 = *np.min(coords, axis=0), *np.max(coords, axis=0)
    return (x0, y0, x1+1, y1+1)

##xtraD = 0
##im1 = charList[0]
##im2 = charList[42]
##back_im = im1.copy()
##back_im.paste(im2, (625 + xtraD, 1271 - im2.height))
##xtraD += im2.height
##back_im.paste(im2, (625 + xtraD, 1271 - im2.height))
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
whatUWant = input("what do you want to type?    ")

mDTrans = []
mUTrans = []
mFUTrans = []


def Translator(w):
    global back_im
    last = -4
    typeIT = w.split()
    print(typeIT)
    print(len(typeIT))
    for i in range (0,len(typeIT)):
        lets = [x for x in typeIT[i]]
        next = False
        for i in range (0,len(lets)):
            
            if lets[i] == "n" and last == -3:
                writeIT.append(-2)
            elif lets[i] == "t" and last == -3:
                writeIT.append(-3)
            elif lets[i] == "\\":
                last = -3

            else:

                writeIT.append(keySplit.index(lets[i]) + 1)
                last = keySplit.index(lets[i]) + 1
        writeIT.append(-1)
        last = -1
    
def Translator2(w, writeIT):
    for i in range (0,len(w)):
        writeIT.append(keySplit.index(w[i]) + 1)
        print(f"this is {writeIT}")
        
Translator2(mDSplit,mDTrans)
Translator2(mUSplit,mUTrans)
Translator2(mUSplit,mFUTrans)   
            
def paster(w):
    global line
    xtraD = 0
    xtraH = 0
    back_im = im1.copy()
    print(w)
    for i in range (0,len(w)):
        
        if w[i] == -1:
            xtraD += 125
        elif w[i] == -3:
            xtraD += 500
        elif w[i] == -2:
            xtraH += 250
            xtraD = 0
            line += 1
        else:
            
            
            

            im2 = charList[w[i] -1]
            if line == 1:
                im2 = im2.resize((int(np.round(im2.width * random.uniform(2.90, 3.10))), int(np.round(im2.height * random.uniform(2.90, 3.10)))), Image.NEAREST)
            else:
                im2 = im2.resize((int(np.round(im2.width * random.uniform(.90, 1.10))), int(np.round(im2.height * random.uniform(.90, 1.10)))), Image.NEAREST)
            
            if  w[i] in mDTrans:
                print("\n\ndown")
                back_im.paste(im2, (625 + xtraD, 1271 - int(np.round(im2.height - (im2.height * random.uniform(.20, .50)) + xtraH))))
                    
            
            elif w[i] in mUTrans:
                    print("up")
                    back_im.paste(im2, (625 + xtraD, 1271 - int(np.round(im2.height * random.uniform(1.3, 1.6) + xtraH))))
                    

            elif w[i] in mFUTrans:
                    print("FUP")
                    back_im.paste(im2, (625 + xtraD, 1271 - int(np.round(im2.height * random.uniform(2.5, 3.2) + xtraH))))
                    

            else:
                print("else")
                back_im.paste(im2, (625 + xtraD, 1271 + xtraH - im2.height))
                    
            xtraD += im2.width + random.randint(- np.round(im2.width/8),np.round(im2.width/8) )
        xtraD += 10 + random.randint(0,4)
    # f, e = os.path.splitext(path)
    back_im.save('rocket_pillow_paste_pos.jpg',  quality=100)
            
            
    


def paster2(w):
    xtraD = 0
    
    back_im = im1.copy()
    for i in range (0,50):
        print("in")
        im2 = charList[i]
        back_im.paste(im2, (625 + xtraD, 1271 - im2.height))
        xtraD += im2.width 
        f, e = os.path.splitext(path)
        
    back_im.save(f + 'rocket_pillow_paste_pos.jpg', quality=95)


xtraH = 0
print(charList)
Translator(whatUWant)
paster(writeIT)

print(writeIT)






##crop2()
