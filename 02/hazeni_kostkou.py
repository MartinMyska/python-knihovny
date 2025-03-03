import random
import sys


if len(sys.argv) != 3:
    exit(f"Usage: {sys.argv[0]} <pocet_stran> <pocet_hodu>")

dice_size = int(sys.argv[1])
throws_count = int(sys.argv[2])

print([random.randint(1, dice_size) for _ in range(throws_count)])
