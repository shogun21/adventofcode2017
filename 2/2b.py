with open("input.dat", "r") as f:
    checksum = 0
    for line in f:
        vals = list(map(int, line.split()))
        for a in vals:
            for b in vals:
                if (a != b and a % b == 0):
                    div1 = a
                    div2 = b
        checksum += (max([div1, div2]) / min([div1, div2]))
    print(checksum)
