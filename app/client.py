import requests

response = requests.post("http://127.0.0.1:5000/hello/world/",
                         json={"json_kay": "json_value"},
                         headers={"token": "fafafqwwqfgqwg"},
                         params={
                             "k1": "v1",
                             "k2": "v2",
                         })
print(response.status_code)
print(response.text)