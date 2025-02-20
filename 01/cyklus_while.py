soucet = 0

while True:
    vstup = input("Zadej číslo: ")

    if not vstup:
        break

    if not vstup.isdigit():
        print("Nezadal jsi číslo")
        continue

    print(f"Zadáno číslo {vstup}")
    soucet += int(vstup)

print(f"Součet je {soucet}")
