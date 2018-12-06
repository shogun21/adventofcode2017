with open("input", "r") as f:
    instructions = []
    N = 0
    steps = 0
    i = 0
    
    for line in f:
        instructions.append(int(line))
        N += 1

    while (i >= 0 and i < N):
        jump = instructions[i]
        if (jump >= 3):
            instructions[i] -= 1
        else:
            instructions[i] += 1
        i += jump
        steps += 1
            
    print ("Steps: " + str(steps))
        
