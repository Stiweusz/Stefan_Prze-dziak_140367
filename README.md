# Proste Programy Python

## Opis
Repozytorium zawiera cztery proste programy Python oraz aplikację webową w Flask.

## Zawartość
- `program1.py`: Hello World
- `program2.py`: API - przewidywany wiek
- `program3.py`: Kalkulator
- `app.py`: Web API - decyzja kredytowa

## Uruchomienie
1. Stwórz środowisko wirtualne:
```
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate   # Windows
```
2. Zainstaluj zależności:
```
pip install -r requirements.txt
```
3. Uruchom aplikację:
```
python app.py
```

## Przykład zapytania:
```
http://127.0.0.1:5000/kredyt?wiek=25&dochod=5000
```
