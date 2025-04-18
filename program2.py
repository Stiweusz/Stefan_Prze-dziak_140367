import requests

name = "John"
response = requests.get(f"https://api.agify.io?name={name}")
if response.status_code == 200:
    data = response.json()
    print(f"Przewidywany wiek dla {name} to {data['age']} lat.")
else:
    print("Błąd pobierania danych.")
