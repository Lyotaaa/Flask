import requests

"""Создать пользователя"""
response = requests.post(
    "http://127.0.0.1:5000/owner/",
    json={
        "email": "yandex.ru",
        "password": "123",
    },
)
print(response.status_code)
print(response.text)

"""Найти пользователя"""
# response = requests.get("http://127.0.0.1:5000/owner/1", )
# print(response.status_code)
# print(response.text)

"""Обновить информацию"""
# response = requests.patch("http://127.0.0.1:5000/owner/1",
#                          json={
#                              "email": "@yandex.net",
#                              "password": "123",
#                          })
# print(response.status_code)
# print(response.text)
#
# response = requests.get("http://127.0.0.1:5000/owner/1", )
# print(response.status_code)
# print(response.text)

"""Удалить пользователя"""
# response = requests.delete("http://127.0.0.1:5000/owner/1")                          )
# print(response.status_code)
# print(response.text)
#
# response = requests.get("http://127.0.0.1:5000/owner/1", )
# print(response.status_code)
# print(response.text)
