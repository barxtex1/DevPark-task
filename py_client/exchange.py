import requests


url = 'http://localhost:8000/api/exchange'
data = {
    "input_currency": 'pln',
    "output_currencies": 'eur,usd,amd',
    "amount": 123.45,
    "date": '2022-08-24'
}

response = requests.get(url, params=data)

print(response.json())