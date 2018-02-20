import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import random
import cv2


#random string
def random_string():
    str_digits = '0123456789'
    str_lowercase= 'abcdefghijklmnopqrstuvwxyz'
    str_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    str_all = str_digits +  str_lowercase + str_uppercase
    string = random.sample(str_all,1)
    randomstring = ''.join(string)
    return randomstring

#random color
def random_color():
    a = random.uniform(0,1)
    b = random.uniform(0,1)
    c = random.uniform(0,1)
    return (a,b,c)

#random size
def random_size():
    a = random.uniform(40,60)
    return a

#random angle
def random_angle():
    a = random.uniform(-30,30)
    return a

#random font family
def random_font():
    dict = {1: 'Italic', 2: 'Maiandra GD', 3: 'Segoe Script'}
    num = random.randint(1,3)
    return dict[num]


#initialize coordinate
plt.figure(figsize=(3,1.5))
plt.xlim(0,300)
plt.ylim(0,150)

#put text
plt.text(random.randint(0,5),random.randint(30,45),random_string(), color = random_color(),size = random_size(),rotation = random_angle(),family = random_font())
plt.text(random.randint(60,65),random.randint(30,45),random_string(),color = random_color(),size = random_size(),rotation = random_angle(),family = random_font())
plt.text(random.randint(120,125),random.randint(30,45),random_string(),color = random_color(),size = random_size(),rotation = random_angle(),family = random_font())
plt.text(random.randint(180,185),random.randint(30,45),random_string(),color = random_color(),size = random_size(),rotation = random_angle(),family = random_font())
plt.text(random.randint(240,245),random.randint(30,45),random_string(),color = random_color(),size = random_size(),rotation = random_angle(),family = random_font())

plt.axis('off')
plt.savefig('CAPTCHA1.jpg')

img = cv2.imread('CAPTCHA1.jpg')

rows,cols,ch=img.shape
pts_x1=np.float32([[random.randint(40,50),random.randint(40,50)],[150,random.randint(40,50)],[random.randint(40,50),180]])
pts_y1=np.float32([[random.randint(30,40),random.randint(30,40)],[150,random.randint(40,50)],[random.randint(40,50),200]])

M=cv2.getAffineTransform(pts_x1,pts_y1)

dst=cv2.warpAffine(img,M,(cols,rows))


for i in range(150):
    for j in range(300):
        b,g,r = dst[i,j]
        if b==0 and g==0 and r==0:
            dst[i,j] = (255,255,255)

#Create 500 noisy pixels
for i in range(500):
    j = random.randint(0,150-1)
    k = random.randint(0,300-1)
    color = (random.randrange(256),random.randrange(256),random.randrange(256))
    dst[j,k] = color


cv2.imwrite('CAPTCHA.jpg', dst)
