##Busca en el archivo de json, la referencia para que en base a esa referencia busque el siguiente versiculo o capitulo

import json ##Para leer o editar archivos JSON
import os ##Importamos el modulo OS para interactuar con el sistema de archivos
from data.versiculos import obtener_versiculo ##Para hacer llamadas a la API
BASE_DIR = os.path.dirname(os.path.abspath(__file__)) ##file, se ejecuta donde se esta ejecutando el archivo
##abspath, es una ruta absoluta
##dirname hace que devuelva la carpeta
RUTA_ESTADO = os.path.join(BASE_DIR, "estado.json")



def leer_Estado(): ## Leer estado del json
    ##Verifica si existe el archivo en la ruta indicada
    if not os.path.exists(RUTA_ESTADO):
        ##Si no, dara un error
        raise FileNotFoundError("No existe estado.json", RUTA_ESTADO)
    
    ##Abre el archivo estado.json en modo de lectura
    ##utf-8 asegura que se lean correctamente los caracteres especiales
    with open(RUTA_ESTADO, "r", encoding="utf-8") as f:
        ##Carga el contenido JSON del archivo y lo convierte en un diccionario de python
        return json.load(f)
    
def guardar_Estado(): ##sobreescribir al archivo para agregarle versiculos
    ##Obtenemos el versiculo actualizado
    versiculo_actualizado = actualizar_Estado()
    print("resultado", actualizar_Estado())
    
    with open(RUTA_ESTADO, "w", encoding="utf-8") as f:
        ##Convetimos un objeto de python en texto JSON y lo guardamos en el archivo
        json.dump(
            {
                "libro": versiculo_actualizado["libro"],
                "capitulo": versiculo_actualizado["capitulo"],
                "versiculo": versiculo_actualizado["versiculo"]        
                
            },
            f,
            indent=4, ##Hace que el JSON se vea mas bonito y elegible
            ensure_ascii=False ##Permite caracteres especiales
            
        )
def actualizar_Estado(): ##Obtener el return del versiculo que se va a guardar y devolver el siguiente a travez de un diccionario que viene de leer_Estado
    referencia_anterior = leer_Estado()
    
    
    libro = referencia_anterior["libro"]
    capitulo = referencia_anterior["capitulo"]
    versiculo = referencia_anterior["versiculo"]
    
    
    versiculo_siguiente = versiculo + 1 ##Sumamos 1 para obtener el siguiente versiculo, mas adelante se vera si existe o no
    ##print("referencia posterior", versiculo_siguiente)
    ##Verificar si tiene el siguiente versiculo
    resultado = obtener_versiculo(libro, capitulo, versiculo_siguiente)
    
    if resultado:
        return {
            "libro": libro,
            "capitulo": capitulo,
            "versiculo": versiculo_siguiente
        }
        
    ##Verificar si tiene capitulo siguiente
            
    capitulo_siguiente = capitulo + 1
    
    resultado = obtener_versiculo(libro, capitulo_siguiente, 1)
    
    if resultado:
        return {
            "libro": libro,
            "capitulo": capitulo_siguiente,
            "versiculo": 1
        }
    
    ##Verificar si tiene libro siguiente
    
    ##Creamos una lista de todos los nombres, de todos los libros de la biblia
    
    LIBROS_BIBLIA = (
    "Genesis, Exodus, Leviticus, Numbers, Deuteronomy, "
    "Joshua, Judges, Ruth, 1 Samuel, 2 Samuel, "
    "1 Kings, 2 Kings, 1 Chronicles, 2 Chronicles, "
    "Ezra, Nehemiah, Esther, Job, Psalms, Proverbs, "
    "Ecclesiastes, Song of Solomon, Isaiah, Jeremiah, Lamentations, "
    "Ezekiel, Daniel, Hosea, Joel, Amos, Obadiah, Jonah, "
    "Micah, Nahum, Habakkuk, Zephaniah, Haggai, Zechariah, Malachi, "
    "Matthew, Mark, Luke, John, Acts, Romans, "
    "1 Corinthians, 2 Corinthians, Galatians, Ephesians, "
    "Philippians, Colossians, 1 Thessalonians, 2 Thessalonians, "
    "1 Timothy, 2 Timothy, Titus, Philemon, Hebrews, "
    "James, 1 Peter, 2 Peter, 1 John, 2 John, 3 John, "
    "Jude, Revelation"
)
    ##Creamos una lista limpia de libros
    LIBROS_LISTA = [libro.strip() for libro in LIBROS_BIBLIA.split(",")]
    ##A traves de la variable libro buscamos la posición en la que se encuentra el array
    indice = LIBROS_LISTA.index(libro)
    print("indice", indice)
    
    indice_siguiente = indice + 1 ##Siguiente indice de libro
    
    ##Obtenemos el nombre del libro de ese indice
    
    if indice_siguiente < len(LIBROS_LISTA):
        libro_siguiente = LIBROS_LISTA[indice_siguiente]
        print("libro siguiente", libro_siguiente)
        
        if libro_siguiente:
            
            return {
            "libro": libro_siguiente,
            "capitulo": 1,
            "versiculo": 1
        }
    
    
    return { ##Si llega hasta apocalipsis, al final volvera a empezar desde cero
        "libro": "Genesis",
        "capitulo": 1,
        "versiculo": 1
    }
    
    

