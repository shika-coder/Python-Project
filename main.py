def printAll():
    aus1 = "[1] Rechnen"
    aus2 = "\n[2] Kontaktliste"
    print(aus1, aus2)

printAll()
auswahl = int(input("Deine Auswahl: "))


def rechner():

    number1 = int(input("Nummer1: "))
    operator = input("Operator: ")
    number2 = int(input("Nummer2: "))

    if operator == "+":
        print(number1 + number2)
    if operator == "-":
        print(number1 - number2)
    if operator == "*":
        print(number1 * number2)
    if operator == "/":
        print(number1 / number2)

Kontakte = []


def Kontaktliste():

    Name = input("wie heisst du?: ")
    Nummer = int(input("Nummer: "))
    
    Kontakte.extend([Name, Nummer])


if auswahl == 1:
    rechner()
if auswahl == 2:
    Kontaktliste()
    print(Kontakte)
