import shutil, os

""" Para copiar un archivo, usando el modulo shutil, debemos acceder al método ‘copy’ el cual recibe como parámetros dos valores (origen, destino)"""

os.chdir('C:\\')  
shutil.copy('C:\\spam.txt', 'C:\\delicious')        #el primer parámetro es origen, el segundo es el destino (copia el archivo spam.txt a la carpeta delicious)
shutil.copy('eggs.txt', 'C:\\delicious\\eggs2.txt') #el archivo eggs.txt se copiaa a la carpeta delicious pero se guarda con el nombre eggs2.txt
shutil.copytree('C:\\bacon', 'C:\\bacon_backup')    #se copia la carpeta completa bacon a la carpeta bacon_backup

shutil.move('C:\\bacon.txt', 'C:\\eggs')            # Tambien se pueden mover archivos
shutil.move('C:\\bacon.txt', 'C:\\eggs\\new_bacon.txt') #o mover archivos y cambiar su nombre

""" 
    os.unlink(path) Para borrar un archivo.
    os.rmdir(path) Para borrar una carpeta que puede estar vacía o contener otras carpetas y archivos.
    shutil.rmtree(path) Para eliminar una carpeta con todo su contenido
"""
# eliminar todas las peliculas de la carpeta descargas
carpeta = 'c:\\descargas'
for filename in os.listdir(carpeta):
    if filename.endswith('.mp4'):
        print("eliminando: " + str(filename))
        os.unlink(filename)
        
# comprimir archivos
import zipfile

newZip = zipfile.ZipFile('new.zip', 'w')
newZip.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED)
newZip.close()


import zipfile, os
os.chdir('C:\\')

exampleZip = zipfile.ZipFile('example.zip')
exampleZip.namelist()

spamInfo = exampleZip.getinfo('spam.txt')
spamInfo.file_size
spamInfo.compress_size

exampleZip.close()
	
# leer un archivo comprimido
os.chdir('C:\\')
 
exampleZip = zipfile.ZipFile('example.zip')
exampleZip.namelist()
 
spamInfo = exampleZip.getinfo('spam.txt')
spamInfo.file_size
spamInfo.compress_size
 
exampleZip.close()

#extraer archivos comprimidos
os.chdir('C:\\')
exampleZip = zipfile.ZipFile('example.zip')
exampleZip.extractall()
exampleZip.close()