para correr el programa solo necesitamos entrar a cp y ejecutar el archivo final.py

![Antes](https://i.imgur.com/mArZzn8.png)

<img src="https://i.imgur.com/a9fkPcR.png" alt="Despues" width="500px">

# Diagrama De Flujo

<img src="https://i.imgur.com/oj9zJ0H.png" alt="Despues" width="1000px">

# Bucket Automation Project

This is a Robotic Process Automation project with Python. The main goal, keep the download workspace free and organised automatically using a stack data structure and a stack sorting algotithm.

## Virtual environment

```bash
python3 -m venv .venv && source .venv/bin/activate
```

Please check this post [.venv](https://www.linkedin.com/pulse/python-venv-qu%25C3%25A9-son-para-sirven-jorge-armando-blanquicett-matos/?trackingId=9MTYA26VFBImOjkwaXsSag%3D%3D)
if you don't know how python virtual environments works.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install -r requirements.txt
```

## Import usage in main.py

```python
import pyautogui
# PyAutoGUI is a cross-platform GUI automation Python module for human beings. Used to programmatically control the mouse & keyboard.

import os
# This module provides a portable way of using operating system dependent functionality

os.getenv
# Return the value of the environment variable key as a string if it exists, or default if it doesn’t.

from os import listdir
# Return a list containing the names of the entries in the directory given by path. The list is in arbitrary order, and does not include the special entries
```

## Knowing the position of things on the screen

```python
print('Press Ctrl-C to quit.')
try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print('\n')
```

## .env file

All real projects use an .env variable with information that you would not be willing to have exposed, don't lag behind, but if this becomes a problem, hardcode the main.py.

```env
BASE_PATH=/YOUR/PATH/TO/DOWNLOAD/STAGE
```

## List files in your chosen bucket

```python
import os
from os import listdir


BASE_PATH = os.getenv('BASE_PATH')
print(BASE_PATH)
onlyfiles = [f for f in listdir(BASE_PATH)
if os.path.isfile(os.path.join(BASE_PATH, f))]

print(onlyfiles)

for i in onlyfiles:
    print(i, os.path.getsize(BASE_PATH+'/'+i))
```

```bash
python main.py
```

```bash
/Users/jorgeabm/Downloads/buckets
['.DS_Store', 'f1.txt', 'f2.txt']
.DS_Store 6148
f1.txt 96775
f2.txt 12096
```

## Contributing

Pull requests or forks are welcome. If you feel noob to pull requests or forks, watch a youtube video or CTRL + C and CTRL + V the project and create a new project in github, don't let this limit you. Good luck from Jorge Blanquicett

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)

utils

#para actualizar: py -m pip install --upgrade pip

#instalar: py -m ensurepip --upgrade

#ejecutar el archivo py get-pip.py de https://bootstrap.pypa.io/get-pip.py

#pip install virtualenv

#pip install pyautogui

#linux:python3 -m venv .venv && source .venv/bin/activate

#windows: py -m venv v && v\Scripts\activate.bat

#recomienda añadir al path C:\Users\Predator\AppData\Roaming\Python\Python311\Scripts

    # print('Press Ctrl-C to quit.') #saber posición del mouse
    # try:
    #     while True:
    #         x, y = pyautogui.position()
    #         positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
    #         print(positionStr, end='')
    #         print('\b' * len(positionStr), end='', flush=True)
    # except KeyboardInterrupt:
    #     print('\n')

    # BASE_PATH = os.getenv('BASE_PATH')
    # print(BASE_PATH)
    # onlyfiles = [f for f in listdir(BASE_PATH)
    # if os.path.isfile(os.path.join(BASE_PATH, f))]

    # print(onlyfiles)

    # for i in onlyfiles:
    #     print(i, os.path.getsize(BASE_PATH+'/'+i))



    # ruta = pathlib.Path('.')
    # ruta = pathlib.cwd()
    # ruta = os.getcwd()

# 2. listar archivos

#print(os.listdir())

#print(os.listdir('Dataset'))

#print(list(Path().iterdir()))

#print(list(Path('Dataset').iterdir()))

# 3 unir paths/rutas

#print(os.path.join(os.getcwd(), 'Dataset'))

#print(PurePath.joinpath(Path.cwd(), 'Dataset'))

# 4 crear carpetas usando Python

#os.mkdir('Dataset')

#Path('Dataset').mkdir(exist_ok=True)

#os.makedirs(os.path.join('Dataset', 'Scripts'))

PurePath.joinpath(Path.cwd(), 'Dataset2', 'Scripts2').mkdir(parents=True)

    # imprimir extensiones de todos los archivos
    # for archivo in ruta.iterdir():
    #     print(archivo.suffix)

    # imprimir extensiones de archivos sin repetir
    # extensiones = {archivo.suffix for archivo in ruta.iterdir()}
    # print(f'extensiones: {extensiones}')

    # diccionario = {k : [v for v in ruta.glob(f'*{k}')]
    #                     for k in {archivo.suffix for archivo in ruta.iterdir()}}

    # for extension, archivos in diccionario.items():
    #     carpeta = ruta / extension[1:]
    #     carpeta.mkdir()
    #     for archivo in archivos:
    #         archivo.replace(carpeta / archivo.name)

## Obtener posición del ratón en la pantalla

#cord_x, cord_y = pyautogui.position()

#print(str(cord_x)+";"+str(cord_y))

## Mover el ratón a otra posición

#pyautogui.moveTo(240, 351)

## Hacer un click en la posición actual del ratón

#pyautogui.click()

## Hacer doble click en la posición actual del ratón

#pyautogui.doubleClick<()

## Escribir con el teclado en la posición clickada del ratón

#pyautogui.moveTo(469, 59)

#pyautogui.click()

#pyautogui.write('Texto que se escribe', interval=0.25)

## Digitar caracteres especiales:

#pyautogui.press('esc')

#pyautogui.press(['left', 'left', 'left'])

#pyautogui.keyUp('shift')

#pyautogui.hotkey('ctrl','c')

## Mostrar un mensaje de alerta:

#pyautogui.alert('ALERTA')

## Mover el ratón presionado el click izquierdo

#pyautogui. drag(10, 20, duration=0.3)

##10 Mover en dirección x (derecha)

##20 Mover en dirección y (abajo)

## Aplicación: dibujar un cuadrado en paint

#pyautogui.moveTo(84,219)

#pyautogui.drag(200,0,duration=0.3)

#pyautogui.drag(0,200,duration=0.3)

#pyautogui.drag(-200,0,duration=0.3)

#pyautogui.drag(0,-200,duration=0.3)

## Aplicación: Dibujar un círculo (aproximado) de radio 100 en paint

#pyautogui.moveTo(84, 219)

#radio = 200

#diferencial = 2.5

#teta = 0

#while teta<math.pi:

#dteta = math.asin(diferencial/(2\*radio))

#dx = diferencial*math.sin(2*teta+dteta)

#dy = diferencial*math.cos(2*teta+dteta)

#teta = teta+dteta

#pyautogui.drag(dx, -dy, duration=0)
