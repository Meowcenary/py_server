import requests
response = requests.get(something_dynamic)
print('status code:', response.status_code)
print('content length:', response.headers['content-length'])
print(response.text)
