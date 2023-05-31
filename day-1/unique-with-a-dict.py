import sys

names_seen = {}

for line in sys.stdin:
    line = line.strip()
    if line.startswith(">"):
        name = line[1:]
        if name in names_seen:
            print(f"We have already seen name {name!r}",
                  names_seen[name], "times")
            names_seen[name] = names_seen[name] + 1
        else:
            names_seen[name] = 1
