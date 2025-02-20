

while True:
    try:
        eval_num = int(input("Enter num to evaluate: "))
        break
    except TypeError:
        continue

prvocislo = True

for i in range(2, eval_num):
    if eval_num % i == 0:
        prvocislo = False

if prvocislo:
    je_prvocislo = "je"
else:
    je_prvocislo = "neni"

print(f"{eval_num} {je_prvocislo} prvocislo")
