def kalkulator(a, b, operacja):
    if operacja == "dodaj":
        return a + b
    elif operacja == "odejmij":
        return a - b
    elif operacja == "mnoz":
        return a * b
    elif operacja == "dziel":
        if b != 0:
            return a / b
        else:
            return "Nie można dzielić przez zero!"
    else:
        return "Nieznana operacja"

print(kalkulator(10, 5, "dodaj"))
