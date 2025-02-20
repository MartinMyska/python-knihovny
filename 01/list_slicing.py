seznam = [49, 38, 18, 82, 85, 60, 94, 21, 20, 14, 37,
          80, 13, 66, 41, 68, 82, 88, 41, 52, 28, 35, 55]

delka = 5
i = 1

while True:
    print(seznam[0 + i:delka + i])
    i += delka
    print(i)
    print(len(seznam))
    if len(seznam) / i <= 1:
        break
