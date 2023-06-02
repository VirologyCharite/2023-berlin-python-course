from secrets import getSecretWord


def playHangman():
    secret = getSecretWord()
    nLetters = len(secret)
    print(f"The secret word has {nLetters} letters.")
    display = ["-"] * nLetters

    while True:
        print(" ".join(display))
        guess = input("Guess a letter: ")

        for index in range(nLetters):
            if guess == secret[index]:
                display[index] = guess

        if "-" not in display:
            break


playHangman()
