import requests

r = requests.get(
    'http://127.0.0.1:5000/employee/ryo'
)
print(r.text)

r = requests.post(
    'http://127.0.0.1:5000/employee', data={'name': 'ryo'}
)
print(r.text)

r = requests.put(
    'http://127.0.0.1:5000/employee', data={
        'name': 'ryo', 'new_name': 'higashi'}
)
print(r.text)

r = requests.delete(
    'http://127.0.0.1:5000/employee', data={'name': 'higashi'}
)
print(r.text)