import sys

names_seen = {}

for line in sys.stdin:
    line = line.strip()
    if line.startswith(">"):
        name = line[1:]
        if name in names_seen:
            names_seen[name] = names_seen[name] + 1
        else:
            names_seen[name] = 1

for name in names_seen:
    count = names_seen[name]
    if count > 1:
        print(f"We saw name {name!r}", count, "times")
