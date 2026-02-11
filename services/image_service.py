##Edición de imagenes
import random
import os #Util para manejar rutas y esas cosas
from PIL import Image, ImageDraw, ImageFont #Importa la clase Image y otras necesarias de la librería Pillow para trabajar con imágenes

#Para las imagenes
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Carpeta donde está este .py
INPUT_DIR = os.path.join(BASE_DIR, "..", "images", "base")      # Sube una carpeta y entra a donde se encuentra el archivo

#Para el tipo de letra
FONT_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_FONT_DIR = os.path.join(FONT_DIR, "..", "fonts", "Montserrat-SemiBoldItalic.ttf")

#Direción de la carpeta donde se va a guardar la imagen editada
GUARDADO_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_GUARDADO_DIR = os.path.join(GUARDADO_DIR, "..", "images", "output")


def elegir_Numero_Imagen(): #Creamos una función que devolvera un número random entre el 1 y el 30
    return random.randint(1, 30)


def elegir_Imagen(): #Creamos una función que elegira la imagen conforme al número random que devolvio la función correspondiente y la editara
    numero_random = elegir_Numero_Imagen()
    ruta = os.path.join(INPUT_DIR, f"{numero_random}.jpg") #Contruye la ruta de forma segura
    #print("La ruta del archivo", ruta)
    #Verificamos si la ruta de la imagen existe, para que el codigo no se rompa
    if not os.path.exists(ruta):
        raise FileNotFoundError(f"No existe la imagen: {ruta}")
    img = Image.open(ruta) #Abre el archivo de imagen que está en esa ruta y lo convierte en un objeto que Python puede editar
    return img, numero_random

def editar_Imagen(texto_versiculo, referencia): #Editamos la imagen y le agregamos texto
    img, numero_random = elegir_Imagen()
    
    img = img.resize((1920, 1080)) #Redimensionamos la imagen para que este correcta
    
    draw = ImageDraw.Draw(img) #Preparamos el lienzo para que este sea dibujado
    
    ##Hacemos que el texto del versiculo sea mas manejable o maneable para que quepa bien en la imagen
    #Por cada 7 palabras, se baja de renglon para que todo no este en una sola linea
    palabras = texto_versiculo.split()            # Separa el texto en palabras
    lineas = []
    for i in range(0, len(palabras), 7):          # Cada 7 palabras, genera números desde 0 hasta len(palabras) de 7 en 7, esto nos permite tomar bloques de 7 palabras a la vez.
        linea = " ".join(palabras[i:i+7])        # toma un subconjunto de palabras, desde i hasta i+6, y une esas palabras con espacios para formar una línea de texto
        lineas.append(linea)                     # Agregamos la línea creada a la lista lineas
    texto_final = "\n".join(lineas)              # Une las líneas con salto de línea
    
    ##Le agregamos la referencia de versiculo al final con salto de linea concatenando
    
    texto_final = texto_final + "\n" + referencia

    #-------------------------------------------------------------------------------------------------
    
    fuente = ImageFont.truetype(INPUT_FONT_DIR, 85) #Fuente del texto
    
    draw.text(
        (50, 50), #Posición del texto
        texto_final,
        fill="white",
        font=fuente
    )
    
    ruta_guardado = os.path.join(INPUT_GUARDADO_DIR, "imagen_final.jpg")
    print("ruta guardado: ", ruta_guardado)
    img.save(ruta_guardado, quality=95)
    return ruta_guardado

    
    
    


    

    
    
    
    

    