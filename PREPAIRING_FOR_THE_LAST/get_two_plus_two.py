import requests

server, port, a, b = input(), int(input()), int(input()), int(input())
params = {'a': a, 'b': b}
response = requests.get(server + ':' + str(port), params=params)
data = response.json()
print(*sorted(data['result']))
print(data['check'])
