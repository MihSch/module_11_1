import requests

r = requests.get('https://technical.city/ru/cpu/Core-i5-12400F-protiv-Ryzen-5-5600')


print(r.content[0:1000])
print(r.headers['Date'])
print(r.status_code)
print(r.history)


