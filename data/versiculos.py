##Versiculos biblicos

import requests

BASE_URL = "https://bible-api.com"

def obtener_versiculo(libro, capitulo, versiculo, traduccion="web"):
    referencia = f"{libro}+{capitulo}:{versiculo}" ## Armamos las referencias del versiculo con los datos entregados de la función
    url = f"{BASE_URL}/{referencia}?translation={traduccion}" ##La referencia la entregamos a la API
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        return {
            "texto": data["text"].strip(),
            "referencia": data["reference"],
            "traduccion": data["translation_name"]
        }
    
    except requests.exceptions.RequestException as e:
        print("Error al obtener el versiculo: ", e)
        return None


##Hacemos una prueba

if __name__ == "__main__":
    versiculo = obtener_versiculo("John", 3, 16)
    
    if versiculo:
        print("📖", versiculo["referencia"])
        print(versiculo["texto"])
        print("Traducción:", versiculo["traduccion"])
    

