# Taschenrechner

print("Taschenrechner")
print("q = beenden")

while True:
    zahl1 = input("\nErste Zahl: ")
    if zahl1 == "q":
        break

    rechenart = input("Rechenart (+, -, *, /): ")
    if rechenart == "q":
        break

    zahl2 = input("Zweite Zahl: ")
    if zahl2 == "q":
        break

    # text in Zahlen umwandeln
    a = float(zahl1)
    b = float(zahl2)

    if rechenart == "+":
        print("Ergebnis:", a + b)
    elif rechenart == "-":
        print("Ergebnis:", a - b)
    elif rechenart == "*":
        print("Ergebnis:", a * b)
    elif rechenart == "/":
        if b == 0:
            print("Durch 0 geht nicht")
        else:
            print("Ergebnis:", a / b)
    else:
        print("Die Rechenart gibt es nicht")

print("Tschüss")
