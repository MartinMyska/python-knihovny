# Napiš funkci, která ze slovníku vytvoří nový slovník,
# kde klíče a hodnoty budou zaměněné
# Použij dict comprehension

def obrat_slovnik(slovnik: dict):
    swapped_dictionary = {}
    for key, value in slovnik.items():
        swapped_dictionary[f"{value}"] = f"{key}"
    return swapped_dictionary


def swap_dict(slovnik: dict):
    return {value: key for key, value in slovnik.items()}


# Napoveda:
def napoveda(iterable1, iterable2):
    # dict comprehension:
    return {k: v for k, v in zip(iterable1, iterable2)}


iterable1 = [0, 1, 2]
iterable2 = ['a', 'b', 'c']
print(napoveda(iterable1, iterable2))


original_dict = {"A": 0, "b": 1, "C": 3}

print(original_dict)

print(obrat_slovnik(original_dict))
print(swap_dict(original_dict))
