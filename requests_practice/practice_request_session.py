import requests

with requests.Session() as session:
    session.headers.update({
    "Accept": "application/json"
    })
    response1 = session.get('https://jsonplaceholder.typicode.com/posts/3', timeout=10)
    response2 = session.get('https://jsonplaceholder.typicode.com/posts/4', timeout=10)
    
    assert response1.status_code == 200
    assert response2.status_code == 200
    data1 = response1.json()
    data2 = response2.json()
    assert data1['id'] == 3
    assert data2['id'] == 4
    print(data1['title'])
    print(data2['title'])