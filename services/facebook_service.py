##Seleción de versiculos


import requests

def subir_Historia(ruta_imagen, page_id, access_token): #Esta función se encargara de subir la historia a facebook
    
    print("se esta ejecutando...")
    
    url = f"https://graph.facebook.com/v24.0/{page_id}/photos"
    
    data = {
        "access_token": access_token
    }
    
    
    
    try:
        with open(ruta_imagen, "rb") as archivo:
            files = {"source": archivo}
            response = requests.post(url, data=data, files=files)
            if response.status_code == 200:
                print("se logro la ejecución...")
            else:
                print("no se logro la ejecucion")
                print("respuesta:", response)
        return response.json()
    except Exception as e:
        print("No se logro subir nada: ", e)
        return None
    