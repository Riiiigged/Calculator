# Einfacher Taschenrechner

print("Einfacher Taschenrechner")
print("Rechenarten: +  -  *  /")
print("Gib 'q' ein, um zu beenden")

while True:
    # Nach der ersten Zahl fragen
    first = input("\nErste Zahl eingeben: ")
    if first == "q":
        break

    # Nach der Rechenart fragen
    op = input("Rechenart eingeben (+, -, *, /): ")
    if op == "q":
        break

    # Nach der zweiten Zahl fragen
    second = input("Zweite Zahl eingeben: ")
    if second == "q":
        break

    # Den Text in Zahlen umwandeln
    a = float(first)
    b = float(second)

    # Rechnen
    if op == "+":
        print("Ergebnis:", a + b)
    elif op == "-":
        print("Ergebnis:", a - b)
    elif op == "*":
        print("Ergebnis:", a * b)
    elif op == "/":
        if b == 0:
            print("Man kann nicht durch null teilen!")
        else:
            print("Ergebnis:", a / b)
    else:
        print("Das ist keine gültige Rechenart.")

print("Auf Wiedersehen!")
