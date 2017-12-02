fp = open("input.dat", "r")
line = fp.readline()

total = 0
length = len(line)
for i in range(length):
    num = int(line[i])
    if (num == int(line[int((i+length/2)%length)])):
        total += num

print (total)
