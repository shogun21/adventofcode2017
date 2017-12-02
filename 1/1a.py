fp = open("input.dat", "r")
line = fp.readline()

i = 0
prev = 0
total = 0
first = 0
for num in line:
    if (i == 0):
        first = int(num)
    if (int(num) == prev):
        total += int(num)
    prev = int(num)
    i += 1

if (prev == first):
    total += prev

print (total)
