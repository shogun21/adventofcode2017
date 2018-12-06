with open("input", "r") as f:
    invalidphrases = 0
    phrases = 0
    for line in f:
        phrases += 1
        seen = []
        breaker = False
        for word in line.split():
            
            letters = list(word)
            letters.sort()

            for _letters in seen:
                if (letters == _letters):
                    invalidphrases += 1
                    breaker = True
                    break

            if (breaker):
                break
            
            seen.append(letters)

print ('validphrases: ' + str(phrases - invalidphrases))
