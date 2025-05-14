import scipy.misc
from PIL import Image
import numpy as np
import random
img=scipy.misc.read("download.jpeg")
count_pun=0
count_ind=0
count=0
while count<=10000:
    x=random.randint(0,2735)
    y=random.randint(0,2480)
    z=0
    if img[x][y][z]==60:
        count_pun+=1
    if img[x][y][z]==0:
        count_ind+=1



    count+=1
print(count_pun)
print(count_ind)
print(count_pun/(count_pun+count_ind))