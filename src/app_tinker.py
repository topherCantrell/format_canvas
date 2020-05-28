import requests

r = requests.get('https://uah.instructure.com/api/v1/courses/45964/files?per_page=1000')

print(r.text)