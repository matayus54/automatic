import pyautogui
import math
from pathlib import Path
import pathlib
import glob
import os
from os import listdir

def main():
# carpeta actual
    ruta= Path('.')
    BASE_PATH = os.getcwd()
    print(BASE_PATH)

# tomamos los archivos
    onlyfiles = [f for f in listdir(BASE_PATH) 
    if os.path.isfile(os.path.join(BASE_PATH, f))]
    print(onlyfiles)
# imprimimos
    for i in onlyfiles:
        print(i, os.path.getsize(BASE_PATH+'/'+i))
# creamos carpetas segun las extensiones 
    diccionario = {k : [v for v in ruta.glob(f'*{k}')] for k in {archivo.suffix for archivo in ruta.iterdir()}}
    
    print(diccionario)
    for extension, archivos in diccionario.items():
        carpeta = ruta / extension[1:]
        carpeta.mkdir(exist_ok=True)
        for archivo in archivos:
            archivo.replace(carpeta / archivo.name)

# ejecutamos el proyecto
if __name__ == '__main__':
    main()

