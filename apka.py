wiek = input("Podaj wiek: ")
# Sprawdzamy, czy wiek jest złożony z cyfr
if wiek.isdigit() == False:
    exit("Wiek musi być liczbą")
wiek = int(wiek)
#region = input("Czy jesteś z USA (T - tak, N - nie")
if wiek >= 18:
    print("Witamy!")
else: print("Żegnamy, przyjdz za ", 18 - wiek, " lat")
