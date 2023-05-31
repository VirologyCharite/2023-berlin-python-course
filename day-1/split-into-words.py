import sys

data = sys.stdin.read()
# data = open("dracula.txt").read()

for line in data.split("\n"):
    for word in line.split(" "):
        print(word)
