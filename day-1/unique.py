import sys

names_seen = []

for line in sys.stdin:
    # Get rid of newline and whitespace.
    line = line.strip()
    if line.startswith(">"):
        # Get rid of the leading > sign.
        name = line[1:]
        if name in names_seen:
            print("Saw name again:", name)
        else:
            # print(f"New name: {name!r}")
            names_seen.append(name)
