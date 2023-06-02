from random import randint


def getSecretWord():
    wantedLine = randint(0, 853)
    with open('words.txt') as fp:
        line = 0
        for word in fp:
            if line == wantedLine:
                return word.lower().strip()
            line += 1
