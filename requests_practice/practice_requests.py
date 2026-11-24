import requests

url = 'https://jsonplaceholder.typicode.com/users/2'
response = requests.get(url, timeout=10)
print(response.status_code)
data = response.json()
print(data['name'], data['email'], sep='\n')

url_post = 'https://jsonplaceholder.typicode.com/posts'
payload = {
    "title": "QA Automation",
    "body": "I am learning API testing",
    "userId": 2
}
request = requests.post(url_post, json = payload, timeout=10)
print(request.status_code)
data_post = request.json()
print(data_post['id'])

assert request.status_code == 201
assert data_post['title'] == payload['title']

url_test = 'https://jsonplaceholder.typicode.com/posts/5'
response_test = requests.get(url_test, timeout=10)
assert response_test.status_code == 200
data_test = response_test.json()
assert data_test['id'] == 5
print(data_test['title'])

url_test_post = 'https://jsonplaceholder.typicode.com/posts'
payload_test = {
    "title": "My API Automation Test",
    "body": "Testing GET and POST requests",
    "userId": 5
}
request_test_post = requests.post(url_test_post, json=payload_test, timeout=10)
assert request_test_post.status_code == 201

data_resp_test = request_test_post.json()
assert data_resp_test['title'] == payload_test['title']
assert data_resp_test['body'] == payload_test['body']
print(data_resp_test['id'])