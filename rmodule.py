import requests

response=requests.get("https://api.github.com")
print(response.text)


response = requests.get("https://jsonplaceholder.typicode.com/posts")
print(response.json())
data = {
    "title": "My Post",
    "body": "Hello World",
    "userId": 1
}

response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json=data
)

print(response.json())