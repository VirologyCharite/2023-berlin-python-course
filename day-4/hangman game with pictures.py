from secrets import getSecretWord
numberOfGuesses = 0
errorCount = 0

pictures = [
    """
    
    
    """,
 
    """
    ----------
    
    """,
    """
    ----------
    |    |
    """,
    """
    ----------
    |    |
    |    0
    """,
    """
    ----------
    |    |
    |    0
    |    |
    """,
    """
    ----------
    |    |
    |    0
    |    |
    |   /|
    """,
    """
    ----------
    |    |
    |    0
    |    |
    |   /|\
    """,
    """
    ----------
    |    |
    |    0
    |    |
    |   /|\
    |    |
    """,
    """
    ----------
    |    |
    |    0
    |    |
    |   /|\
    |    |
    |   /
    """,
    """
    ----------
    |    |
    |    0
    |    |
    |   /|\
    |    |
    |   / \
    """,
    """
    ----------
    |    |
    |    0
    |    |
    |   /|\
    |    |
    |   / \
    |_____________
    """
]

secret = getSecretWord()
nLetters = len(secret)
print(f"The word has {nLetters} letters")
print(f"The word is {secret}")
display = ["_"] * nLetters
maxErrors = len(pictures)
turn = 10
guess = 0

while True:
    print(pictures[errorCount])
    print(" ".join(display))
    guess = input("Guess the letter?")
    numberOfGuesses += 1

    found = False
    for index in range(len(secret)):
        if guess == secret[index]:
            display[index] = guess
            found = True

    if not found:
        errorCount += 1

        if errorCount == maxErrors:
            print("RIP")
            break

    if "_" not in display:
        print("You are saved!")
        break
