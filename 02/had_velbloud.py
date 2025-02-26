import sys


snake_notation = sys.argv[1]
all_words = snake_notation.split("_")

cammelCase = ""
for i, word in enumerate(all_words):
    if i == 0:
        cammelCase += word
    cammelCase += word.capitalize()

print(cammelCase)
