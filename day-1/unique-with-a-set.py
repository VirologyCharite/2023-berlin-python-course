import sys

names_seen = set()

for line in sys.stdin:
    line = line.strip()
    if line.startswith(">"):
        name = line[1:]
        if name in names_seen:
            print("Saw name again:", name)
        else:
            names_seen.add(name)
