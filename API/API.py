import requests
import json

request = requests.get('http://api.open-notify.org')
print(request.text)
print(request.status_code)

people = requests.get('http://api.open-notify.org/astros.json')
print(people.text)
people_json  = people.json()
print(people_json)

#To print the number of people in space
print("Number of people in space:",people_json['number'])#To print the names of people in space using a for loop
for p in people_json['people']:
    print(p['name'])
    
##         Codigo Facilito   
    
if __name__ == '__main__':
    url = 'http://www.google.com.co'
    response = requests.get(url) #si regresa 200 todo esta bien
    
    if response.status_code == 200:
        content = response.content
        print(response.content) # entrega todas las etiquetas html de la web
        
        file = open('google.html','wb')
        file.write(content)
        file.close()
    
    print('\n\n\n\n')
    
    url = 'http://httpbin.org/get'
    args = { 'nombre' : 'Robinson' , 'curso' : 'Python' , 'nivel' : 'Intermedio'}
    response = requests.get(url , params = args) #si regresa 200 todo esta bien
    print(response.url)
    
    if response.status_code == 200:
        """content = response.content
        print(content) # entrega todas las etiquetas html de la web
        response_json = response.json()
        print(response_json)
        origin = response_json['origin']
        print(origin)"""
        response_json = json.loads(response.text)
        origin = response_json['origin']
        print(origin)
    
    url = 'http://httpbin.org/post'
    payload = { 'nombre' : 'Robinson' , 'curso' : 'Python' , 'nivel' : 'Intermedio'}
    headers = {'Content-Type' : 'application/json' , 'acces_token' : '12345'}
    response = requests.post(url , json = payload , headers = headers) #serializa: convierte en un diccionario json
    #esponse = requests.post(url , data = json.dumps(payload)) #nosotros serializamos los datos con json.dumps()
    
    print(response.url)
    
    if response.status_code == 200:
        #print(response.content)
        headers_response = response.headers
        server = headers_response['Server']
        print(server)