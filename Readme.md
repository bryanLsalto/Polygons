# ConvexPolygon

En este directorio se encuentran tres programas/clases. Primero de todo la clase ConvexPolygon dentro del fichero polygons.py, tambien un programa para crear un bot en telegram (bot.py), y otro programa para enviar comandos a un interprete y poder hacer diferentes operaciones con polígonos(interprete.py).

## Getting Started

Para poder ejecutar estos programas necesitaremos unos cuantos módulos previamente instalados. Aparte de un sistema de comunicación entre antlr y python.

### Prerequisites

Para el correcto funcionamiento de nuestros programas necesitaremos los modulos PILLOW y python-telegram.bot. Aparte de tener instalado el antlr, y su mecanismo de comunicación para utilizarlo con python.


```
>> sudo apt-get install antlr4
```
```
>> pip3 install antlr4-python3-runtime
```
```
>> pip3 install python-telegram-bot
```
```
>> python3 -m pip install --upgrade pip
>> python3 -m pip install --upgrade Pillow
```


### Installing

Antes de correr los programas necesitamos Crear los archivos que contendran la gramatica que nuestros programas interprete.py y bot.py utilizarán para entender los comandos que interpretarán.


```
>> antlr4 -Dlanguage=Python3 -no-listener -visitor Expr.g
```

Una vez ya este todo instalado, podremos ejecutar nuestros programas de la siguiente manera.
En el caso se polygons.py lo mejor será utilizar un interprete y cargar sus modulos y clase.

```
>> python3
>> from polygons import *
```
Una vez ya tengamos los modulos cargados, los podemos utlizar para realizar diferentes funciones y crear instancias de polígonos. Una instancia de un polígono es capaz de realizar operaciones con otros polígonos pasados por parametro, para tener la información de cada función de la clase se puede consultar la documentación del progroma polygons.py.


En el caso del interprete, solo tendremos que ejecutar el programa y empezar a interactuar con el mediante los comandos.
 ```
>> python3 interprete.py
```

Para utilizar el bot es muy parecido al caso anterior, pero no tendremos que interactuar con él mediante la terminal, utilizaremos nuestra cuenta de telegram y el usuario del bot, simulando una charla.
 ```
>> python3 bot.py
```

## Running the tests

No existe un test automata pero podemos comparar si los resultados del fichero input.txt se corresponden con la salida de output.txt. Todos las operaciones tanto de la clase como del interprete funcionan bien. Menos cuando hay una operación de intersección luego de una unión, entonces el resultado da incorrecto, estamos en proceso de solucionarlo. Todas las demas funciones funcionan correctamente. 

### Break down into end to end tests

El fichero input.txt contiene un gran abanico de casos y nos permite ver la variedad de funciones y comandos que se pueden llegar a hacer con la gramática creada.

```
p1 := [0 0 0 1 1 1 0.2 0.8]
print p1
color p1, {0 0 1}
draw "imagen.png", p1
```

## Built With

* [ANTLR](https://www.antlr.org) - Utilizado para crear la gramatica del interprete
* [PILLOW](https://python-pillow.org) - Utilizado para dibujar polígonos
* [python-telegram-bot](www.python-telegram-bot.org) - Usado para interactuar con el bot


## Authors

* **Bryan Leonardo Salto Salao** 
