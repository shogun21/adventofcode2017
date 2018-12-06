with open("input", "r") as f:
    invalidphrases = 0
    phrases = 0
    for line in f:
        phrases += 1
        seen = []
        for word in line.split():
            if (word in seen):
                invalidphrases += 1
                break
            else:
                seen.append(word)

print ('validphrases: ' + str(phrases - invalidphrases))
