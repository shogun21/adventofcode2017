with open("input.dat", "r") as f:
    checksum = 0
    for line in f:
        vals = list(map(int, line.split()))
        checksum += (max(vals) - min(vals))
    print(checksum)
