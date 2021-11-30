import requests

BASE = "http://127.0.0.1:5000/"

data = [{'views': 100000, 'name': 'Hello world', 'likes': 1000},
        {'views': 8000, 'name': 'Good morning', 'likes': 500},
        {'views': 12000, 'name': 'Good night', 'likes': 15}]

for i in range(len(data)):
    response = requests.put(BASE + 'video/' + str(i), data[i])
    print(response.json())

input()
response = requests.get(BASE + 'video/2')
print(response.json())

input()
response = requests.get(BASE + 'video/6')
print(response.json())

input()
response = requests.patch(BASE + 'video/2',{'likes': 22})
print(response.json())

input()
response = requests.get(BASE + 'video/2')
print(response.json())