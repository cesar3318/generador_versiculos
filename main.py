##Punto de entrada
from data.versiculos import obtener_versiculo
from save.obtener_referencia import leer_Estado
from save.obtener_referencia import guardar_Estado
from utils.helpers import traducir_texto
from services.image_service import editar_Imagen
from utils.helpers import mostrar_mensaje
from services.facebook_service import subir_Historia
from dotenv import load_dotenv
import tkinter as tk
import os

#Cargamos dotenv
load_dotenv()


#Hacemos un pequeño mensaje que nos indique que se logro subir un versiculo a facebook


##Obtener la referencia del versiculo inicial o actualizado según la referencia

guardar_Estado() ##Esta función sobreescribira el archivo para dar el versiculo siguiente
variable_Leer_Estado = leer_Estado() ##Aqui se guarda el estado del JSON del archivo que contiene el versiculo

##Obtener el texto biblico de la referencia

versiculo = obtener_versiculo(variable_Leer_Estado["libro"], variable_Leer_Estado["capitulo"], variable_Leer_Estado ["versiculo"])

if versiculo:
    print("📖", versiculo["referencia"])
    print(versiculo["texto"])
    ##Traducimos el texto a español
    versiculo_traducido = traducir_texto(versiculo["texto"])
    print("versiculo traducido", versiculo_traducido)
    ##Insertamos el versiculo en la imagen
    imagen_versiculo = editar_Imagen(versiculo_traducido, versiculo["referencia"])
    #Subirla a facebook
    token_Acceso = os.getenv("ACCESS_TOKEN")
    pagina_id = os.getenv("ID_PAGE")
    #print("mi token", pagina_id, token_Acceso)
    #print("resultado, ", imagen_versiculo)
    subir_Historia(imagen_versiculo, pagina_id, token_Acceso)
    
    
    
    
    
    
    
    
    
    #Mostrar un mensaje de que se subio correctamente
    #root = tk.Tk()  # Crear la ventana principal de Tkinter
    #root.withdraw()  # Ocultar la ventana principal para que solo aparezca el toast
    #mostrar_mensaje("Versículo subido correctamente a Facebook")  # Llamar a la función para mostrar el toast
    # Cerrar automáticamente la ventana raíz después de 4 segundos
    #root.after(30000, root.destroy)  # Se cierra todo automáticamente
    #root.mainloop()  # Ejecutar el loop principal de Tkinter para mantener la interfaz activa
    
