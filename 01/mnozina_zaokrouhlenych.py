# Napiš funkci, která vrátí ze iterovatelného vstupu
# množinu zaokrouhlených hodnot

def mnozina_zaokrouhlenych(vstup):
    return {round(num_uneven) for num_uneven in vstup}


mnozina = [1.4567, 2, 345, 345.00, 0.001]
rounded_list = mnozina_zaokrouhlenych(mnozina)
print(rounded_list)
