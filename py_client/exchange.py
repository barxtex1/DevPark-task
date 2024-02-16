import requests


url = 'http://localhost:8000/api'
data = {
    "input_currency": 'pln',
    "output_currencies": 'eur,usd',
    "amount": 123.22,
    "date": '2023-11-23'
}

response = requests.get(url, params=data)

print(response.json())