import requests

url_put = 'https://jsonplaceholder.typicode.com/posts/5'
payload_put = {
    "title": "Learning PUT requests",
    "body": "I can update API resources",
    "userId": 1
}

request_put = requests.put(url_put, json=payload_put, timeout=10)

assert request_put.status_code == 200

data_put = request_put.json()

assert data_put['title'] == payload_put['title']
assert data_put['body'] == payload_put['body']
assert data_put['id'] == 5
print(data_put['title'])

url_patch = 'https://jsonplaceholder.typicode.com/posts/7'
payload_patch = {
    "title": "Learning PATCH requests"
}

request_patch = requests.patch(url_patch, json=payload_patch, timeout=10)

assert request_patch.status_code == 200

data_patch = request_patch.json()

assert data_patch['title'] == payload_patch['title']
assert data_patch['id'] == 7

print(data_patch['title'])

url_del = 'https://jsonplaceholder.typicode.com/posts/9'

request_del = requests.delete(url_del, timeout=10)

assert request_del.status_code == 200
print(request_del.status_code)
print('Post deleted successfully')
