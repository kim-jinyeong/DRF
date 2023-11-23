# Django REST API Framework 를 사용한 CRUD

## 버전
- Python 3.9.13
- Django 4.2.6
- Django REST Framework 3.14.0

## 환경 설치

가상환경 생성 및 활성화 
```
python -m venv env # env 라는 이름의 venv 가상환경 생성
가상환경 설치 폴더 안에 Script 폴더 이동후 activate 명령어 실행
```

가상환경 활성화 후 패키지 설치 명령어 실행
```
pip install -r requirements.txt
```

## REST Api

Endpoint |HTTP 메소드 | CRUD | 결과
-- | -- |-- |--
`api/question`| GET | READ | 모든 글 읽기
`api/question/:id` | GET | READ | 하나의 글 읽기
`api/question`| POST | CREATE | 새로운 글 생성
`api/question/:id` | PUT | UPDATE | 하나의 글 수정
`api/question/:id` | DELETE | DELETE | 하나의 글 삭제

## 테스트
서버 실행
```
python manage.py runserver
```
Token auth 를 적용 시켰기 때문에 토큰 인증 필요

SuperUser 생성 후 토큰 요청,
```
# python
import requests
url = 'http://127.0.0.1:8000/api/auth'
data={'username' : 'username', 'password': 'password'}
response = requests.post(url, data)
```
응답 받은 토큰은 str 타입이므로 json 타입으로 변경 후 api 요청
```
# python
myToken = response.json()
header = {'Authorization' : 'Token ' + myToken['token']}
response = requests.get('http://127.0.0.1:8000/api/question_list', headers = header)
print(response.text) 
```
