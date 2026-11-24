import requests


with requests.Session() as session:
    session.headers.update({
    "Accept": "application/json"
})
    
    request_get = session.get('https://jsonplaceholder.typicode.com/posts/10', timeout=10)
    assert request_get.status_code == 200
    data_get = request_get.json()
    assert data_get['id'] == 10
    print('Post title = ', data_get['title'], sep='')
    
    payload_post = {
    "title": "CRUD Automation",
    "body": "Creating a post",
    "userId": 1
    }
    request_post = session.post('https://jsonplaceholder.typicode.com/posts', json=payload_post, timeout=10)
    assert request_post.status_code == 201
    data_post = request_post.json()
    assert data_post['title'] == payload_post['title']
    assert data_post['body'] == payload_post['body']
    print('ID data_post = ', data_post['id'], sep='')
    
    payload_put = {
    "title": "Updated with PUT",
    "body": "Full update",
    "userId": 1
    }
    request_put = session.put('https://jsonplaceholder.typicode.com/posts/10', json=payload_put, timeout=10)
    assert request_put.status_code == 200
    data_put = request_put.json()
    assert data_put['title'] == payload_put['title']
    assert data_put['body'] == payload_put['body']
    assert data_put['id'] == 10
    
    payload_patch = {
    "title": "Updated with PATCH"
    }
    request_patch = session.patch('https://jsonplaceholder.typicode.com/posts/10', json=payload_patch, timeout=10)
    assert request_patch.status_code == 200
    data_patch = request_patch.json()
    assert data_patch['title'] == payload_patch['title']
    assert data_patch['id'] == 10
    
    request_del = session.delete('https://jsonplaceholder.typicode.com/posts/10', timeout=10)
    assert request_del.status_code == 200
    print('Post deleted successfully')