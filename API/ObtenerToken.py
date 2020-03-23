import requests

client_id = '369215fa00432fd6b039'
client_secret = 'bcce46a5a7943981310e8f7cb1425bf1541507aa'

code = '35d1a2e36db2d2dbc24'
access_token = '373000f72e50c19b24a930893e1b4ef322b85802'

if __name__ == '__main__':
    url = 'http://github.com/login/oauth/access_token'
    payload = {'client_id' : client_id , 'client_secret' : client_secret , 'code' : code}
    headers = {'Accept' : 'application/json'}
    
    response = requests.post(url, json = payload , headers = headers)
    
    if response.status_code == 200:
        response_json = response.json()
        
        access_token = respnse_json['access_token']
        print(access_token)