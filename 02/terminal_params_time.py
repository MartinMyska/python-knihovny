import sys


total_min = int(sys.argv[1])
hours = total_min // 60
minutes = total_min % 60

print(f"{hours}:{minutes}")
