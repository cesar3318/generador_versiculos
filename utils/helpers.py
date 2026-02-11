#import requests
#import os
#from dotenv import load_dotenv
import argostranslate.translate
import tkinter as tk

def traducir_texto(texto, origen="en", destino="es"): ##Creamos una función que obtiene un texto y lo traduce usando una API
    
    # Cargar variables del archivo .env
    #load_dotenv()
    
    # Obtener la clave
    #API_KEY = os.getenv("API_KEY_TRADUCTOR")
    #print("La api key es: ", API_KEY) 
    
    #url = "https://language.uclassify.com/translate/v1/"
        
    
    
    try:
        traducir_texto = argostranslate.translate.translate(
            texto,
            origen,
            destino
        )
        return traducir_texto
    
    except Exception as e:
        print("Error al traducir", e)
        return None
    
def mostrar_mensaje(mensaje, duracion=10000): #Creamos una función que desplegara un mensaje en pantalla para avisar que se subio un versiculo a facebook correctamente
    
    toast = tk.Toplevel() #Crea una ventana pequeña
    toast.overrideredirect(True)  # Sin bordes ni barra de título
    toast.attributes("-topmost", True)  # Siempre encima de otras ventanas
    
    
    #Creamos una etiqueta con el mensaje
    label = tk.Label(toast, text=mensaje, bg="blue", fg="black", font=("Arial", 12), bd=2, relief="solid", padx=10, pady=5) #bd, es grosor del borde, el padx y pady, es el espaciado interno horizontal y vertical
    label.pack() #Empaquetar la etiqueta dentro de la ventana
    
    # Calcular posición en la esquina inferior derecha
    toast.update_idletasks()  # Actualiza dimensiones de la ventana
    ancho = toast.winfo_width()  # Obtener ancho de la ventana
    alto = toast.winfo_height()  # Obtener alto de la ventana
    
    pantalla_ancho = toast.winfo_screenwidth()  # Ancho de la pantalla
    pantalla_alto = toast.winfo_screenheight()  # Alto de la pantalla
    
    x = pantalla_ancho - ancho - 20  # Posición X (20 píxeles desde el borde derecho)
    y = pantalla_alto - alto - 50    # Posición Y (50 píxeles desde el borde inferior)
    
    toast.geometry(f"+{x}+{y}")  # Establecer la posición de la ventana
    
    # Configurar cierre automático del toast después de 'duracion' milisegundos
    toast.after(duracion, toast.destroy)


