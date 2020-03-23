import requests

if __name__ == '__main__':
    url = 'https://es.theepochtimes.com/assets/uploads/2019/05/GatitoBlanco-795x447.jpg'
    
    response = requests.get(url, stream = True) #stream realiza la peticion sin descargar el contenido sin cerrar la conexion
    with open('image.jpg','wb') as file: #importante para archivos pesados como pdf, imagenes y videos
        for chunk in response.iter_content():#descarga el contenido poco a poco
            file.write(chunk)
    
    response.close()