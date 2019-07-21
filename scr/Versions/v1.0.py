#!/usr/bin/env python
# coding: utf-8

# # Creacion de Captcha para imagenes
# 
# 
# ##  Programa obtiene un arreglo de imagenes guardadas en una capeta, y escribe en ellas el codigo generado por el programa de generacion de Captcha
# ### Codigo creado por  Efren Mario Gonzalez Lopez 17/07/2019
# #### Github: https://github.com/DarknessZ3R0/Captcha_Create
# 

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

def captcha_img_string()
    captcha_text = create_random_captcha_text()
    captcha_img=[]
    file=glob.glob(img_captcha_path)
    
    int i=0
    for i in range(3):
        c_string=''
        tmp=captcha_text[i]
        c_strin="..\img_data\Mayusculas\\"+tmp+".png"
        for caFile in file:
            

#Inicio, creacion de captcha y creacion de la imagen con captcha y guardado con su nombre
def img_captcha_creation():
    TEXT_COLOR =(195,38,226)#(238,238,238)
    SHADOW_COLOR=(238,238,238)#(195,38,226)
    X_data = []
    files=glob.glob(image_path) #solo funciona con jpg,"Probar con PNG y JPEG"
    for myFile in files:
       
         # Crear Captcha 
        captcha_img_text = create_random_captcha_text()
        print(captcha_text) #visualizacion del captcha

        #reacomodo del captcha para la imagen
        i=0
        j=0
        img_captcha=''
        for i in range(3):
            temp=captcha_img_text[i]
            img_captcha+=str(temp)
            j=j+1
            img_captcha+=str('   ')#Espacio
            j=j+1
        #fin del acomodo, y se guarda en otra variable para poder ser usada despues
        print(img_captcha)#visualizacion del captcha reacomodado

        #Selecion de tipo de letra, si quieres una en especial, descargar el TTF o OTF y modificar la ultima parte

        print(myFile) #Localiza la imagen en una carpeta
        image = cv2.imread (myFile)
        X_data.append (image)
        img = Image.open(myFile)
        draw = ImageDraw.Draw(img)
        fnt = ImageFont.truetype(font_path,250)
        draw.text((300,100), img_captcha,font=fnt,fill=(TEXT_COLOR),owidth=1,ocolor=(SHADOW_COLOR)) #Posiciones, "texto a dibujar en la imagen" ,Tipo de letra,color

        img.save("..\img_output/"+captcha_text + '.jpg') #Guarda el archivo generado con el nombre del captcha generado original

    print('X_data shape:', np.array(X_data).shape)


    # In[ ]:
    print("\n------------------------- Todo salio perfecto!! -------------------------------")
    




# In[ ]:

img_captcha_creation();


