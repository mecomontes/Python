# Fuente:

Comienza por descargar el archivo ZIP fuente desde este enlace 

```
http://data.gov.uk/dataset/road-accidents-safety-data
```

y extrae el contenido.


# **Leyendo el Archivo**

El primer archivo con el que trabajaremos es una compilación de todos los accidentes automovilísticos 
en Inglaterra durante el período entre 1979 – 2004, para extraer todos los accidentes suscitadas en 
Londres en el año 2000.


## Excel

Intenta abrir Accidents7904.csv en Excel. Mejor no lo intentes. Si no posees memoria 
suficiente, esto podría colapsar tu pc. 


## ¿Qué sucede?

Deberías ver un error “Archivo No Cargado Completamente” dado que Excel sólo maneja un millón de filas a la vez.

Probamos esto en LibreOffice también y recibimos un error similar –

    “Los datos no pudieron ser cargados completamente porque el número máximo de filas ha sido excedido.”

Para solventar esto podemos abrir un archivo en Pandas.


## Pandas

En un nuevo directorio de proyecto, activa un entorno virtual, y luego instala Pandas:

``` 
$ pip install pandas==0.16.1
```

Ahora puedes usar el script!.
