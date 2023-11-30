import requests, json
url = 'http://127.0.0.1:8000/api/auth'
data={'username' : 'admin', 'password': 'admin'}
response = requests.post(url, data)
myToken = response.json()
print(myToken)
header = {'Authorization' : 'Token ' + myToken['token']}
response = requests.get('http://127.0.0.1:8000/api/question_list', headers = header) 
print(response.text)
