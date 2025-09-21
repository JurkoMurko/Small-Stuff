import PIL

from PIL import Image
import os.path, sys
import numpy as np
from os import listdir

# path = "C:\\Users\\quint\\OneDrive\\Desktop\\handwriting\\letters"
# path2 = "C:\\Users\\quint\\OneDrive\\Desktop\\handwriting\\letters\\cropped"
# path3 = "C:\\Users\\quint\\OneDrive\\Desktop\\handwriting\\letters\\cropped\\zoomed"

# dirs = os.listdir(path)
# dirs2 = os.listdir(path2)
# dirs3 = os.listdir(path3)

def crop():
    for item in dirs:
        fullpath2 = os.path.join(path,item)
        fullpath = os.path.join(path + "\\cropped",item)         #corrected
        if os.path.isfile(fullpath2):
            im = Image.open(fullpath2)
            f, e = os.path.splitext(fullpath)
            imCrop = im.crop((13, 90, 213, 330)) #corrected
            imCrop.save(f + 'CroppedTwice.png', "PNG", quality=100)

def crop2():
    for item in dirs2:
        fullpath = os.path.join(path2 + "\\zoomed",item)
        fullpath2 = os.path.join(path2,item)    
        print(fullpath)  
        print(fullpath2)  #corrected
        if os.path.isfile(fullpath2):
            print("AHHHHH")
            im = Image.open(fullpath2)
            f, e = os.path.splitext(fullpath)
            print(bbox(im))  # (33, 12, 223, 80)
            im2 = im.crop(bbox(im))
            
            im2.save(f + 'Cropped.png', "PNG", quality=100)

# charList = []
# def listTime():    
#     for item in dirs3:
#         fullpath = os.path.join(path3,item)
          
#         if os.path.isfile(fullpath):
#             im = Image.open(fullpath)
#             charList.append(im)

# listTime()

def bbox(im):
    a = np.array(im)[:,:,:3]  # keep RGB only
    m = np.any(a != [255, 255, 255], axis=2)
    coords = np.argwhere(m)
    y0, x0, y1, x1 = *np.min(coords, axis=0), *np.max(coords, axis=0)
    return (x0, y0, x1+1, y1+1)

# xtraD = 0
# im1 = charList[0]
# im2 = charList[42]
# back_im = im1.copy()
# back_im.paste(im2, (625 + xtraD, 1271 - im2.height))
# xtraD += im2.height
# back_im.paste(im2, (625 + xtraD, 1271 - im2.height))

typeIT = []
writeIT = []
key = """abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789()!<>?.,^:_+-*/=%$&€"';[]#"""
keySplit = [key]
whatUWant = input("what do you want to type?    ")

def Translator(w):
    typeIt = []
    typeIt = w.split()
    
    for i in range (0,len(typeIt)):
        lets = [x for x in typeIt[i]]
        print(lets)
        for i in range (0,len(lets)):
            writeIT.append(key.index(lets[i]) + 1)
        writeIT.append(-1)

Translator(whatUWant)
print(writeIT)
f, e = os.path.splitext(path)

back_im.save(f + 'rocket_pillow_paste_pos.jpg', quality=95)
