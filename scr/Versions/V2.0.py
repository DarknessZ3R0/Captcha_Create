#!/usr/bin/env python
# coding: utf-8

# # Creacion de Captcha para imagenes
# 
# 
# ##  Programa obtiene un arreglo de imagenes guardadas en una capeta, y escribe en ellas el codigo generado por el programa de generacion de Captcha
# ### Codigo creado por  Efren Mario Gonzalez Lopez 17/07/2019
# #### Github: https://github.com/DarknessZ3R0/Captcha_Create
# version: 2.1 
# release date: 21/07/2019


# #### Archivos necesarios

# In[1]:


from captcha.image import ImageCaptcha
import matplotlib.pyplot as plt
import random
import cv2
import glob
import numpy as np
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
import os


# ## main

# In[2]:





#image_path = input("Directorio de imagenes (Preferencia : ..\Captcha\img\*.jpg )")
#font_path  = input("Directorio de Fonts (Preferencia : ..\Captcha\\fonts\MPC.otf)")
image_path = "..\img_input\*.jpg"
font_path = "..\\fonts\MPC.otf"


# In[3]:


number_list = ['0','1','2','3','4','5','6','7','8','9']

alphabet_lowercase = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

alphabet_uppercase = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def create_random_captcha_text(captcha_string_size=4):

    captcha_string_list = []

    base_char = alphabet_lowercase + alphabet_uppercase + number_list

    for i in range(captcha_string_size):

       
        char = random.choice(base_char)

       
        captcha_string_list.append(char)

    captcha_string = ''

    
    for item in captcha_string_list:
        captcha_string += str(item)

    return captcha_string

def captcha_img_string(captcha_text):
    img_captcha_path="..\img_data\letras\*.png"
    img_captcha_pathMins="..\img_data\letras\minusculas\*.png"
    
    #captcha_text = "A1Bc"
    captcha_img=[]
    tam= len(captcha_text)
   # print(tam)
    
    #print(captcha_text)
    i=0
    file=glob.glob(img_captcha_path)
    for i in range(len(captcha_text)):
        file=glob.glob(img_captcha_path)
        c_string=''
        tmp=captcha_text[i]
        tmp= tmp+".png"
        c_string="..\img_data\letras\\"+tmp
        #print(c_string)
        for caFile in file:
            if caFile == c_string:
                captcha_img.append(c_string)
                #print(captcha_img)   
        file=glob.glob(img_captcha_pathMins)
        c_string="..\img_data\letras\minusculas\\"+tmp
        for caFile in file:
            if caFile == c_string:
                captcha_img.append(c_string)
        
           
    
   # print(len(captcha_img))
    #print(captcha_img)
    return captcha_img

#Inicio, creacion de captcha y creacion de la imagen con captcha y guardado con su nombre
def img_captcha_creation():
    TEXT_COLOR =(195,38,226)#(238,238,238)
    SHADOW_COLOR=(238,238,238)#(195,38,226)
    fnt = ImageFont.truetype(font_path,250)
    X_data = []
    files=glob.glob(image_path) #solo funciona con jpg,"Probar con PNG y JPEG"
    for myFile in files:
       
         # Crear Captcha 
        captcha_text = create_random_captcha_text();
        captcha_img_text = captcha_img_string(captcha_text)
        print(captcha_text) #visualizacion del captcha

     
      
        #Selecion de tipo de letra, si quieres una en especial, descargar el TTF o OTF y modificar la ultima parte      
        print(myFile) #Localiza la imagen en una carpeta
        image = cv2.imread (myFile)
        #imageL=""
        imageA = captcha_img_text[0]
        imageB = captcha_img_text[1]
        imageC = captcha_img_text[2]
        imageD = captcha_img_text[3]
        
                    
        img0 = Image.open(myFile)
        img1 = Image.open(imageA)
        img2 = Image.open(imageB)
        img3 = Image.open(imageC)
        img4 = Image.open(imageD)
        
        width,height = img0.size
        
        trans =Image.new('RGBA',(width,height),(0,0,0,0))
        trans.paste(img0,(0,0))
        trans.paste(img1,(250,100),mask=img1)
        trans.paste(img2,(450,100),mask=img2)
        trans.paste(img3,(650,100),mask=img3)
        trans.paste(img4,(850,100),mask=img4)
        new=trans.convert('RGB')
        new.save("..\img_output/"+captcha_text + '.jpg') #Guarda el archivo generado con el nombre 
        #del captcha generado original

    


    # In[ ]:
    print("\n------------------------- Todo salio perfecto!! -------------------------------")
    




# In[ ]:

img_captcha_creation();


