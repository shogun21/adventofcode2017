with open("input", "r") as f:
    
    blocks = []
    configurations = []
    steps = 0
    N = 0
    
    for line in f:
        for block in line.split():
            blocks.append(int(block))
            N += 1
    
    while (str(blocks) not in configurations):
        
        configurations.append(str(blocks))
        
        count = max(blocks)
        i = blocks.index(count)
        
        blocks[i] = 0
        while (count > 0):
            i += 1
            if (i >= N):
                i = 0
            blocks[i] += 1
            count -= 1
            
        steps += 1

    print ("Steps: " + str(steps))
