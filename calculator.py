print("Taschenrechner")
print("q = beenden")

while True:
    zahl1 = input("\nErste Zahl: ")
    if zahl1 == "q":
        break

    rechenart = input("Rechenart (+, -, *, / oder plus, minus, mal, geteilt): ").lower()
    if rechenart == "q":
        break

    zahl2 = input("Zweite Zahl: ")
    if zahl2 == "q":
        break

    a = float(zahl1)
    b = float(zahl2)

    if rechenart == "+" or rechenart == "plus":
        print("Ergebnis:", a + b)
    elif rechenart == "-" or rechenart == "minus":
        print("Ergebnis:", a - b)
    elif rechenart == "*" or rechenart == "mal":
        print("Ergebnis:", a * b)
    elif rechenart == "/" or rechenart == "geteilt":
        if b == 0:
            print("Durch 0 geht nicht")
        else:
            print("Ergebnis:", a / b)
    else:
        print("Die Rechenart gibt es nicht")

print("Tschüss")
