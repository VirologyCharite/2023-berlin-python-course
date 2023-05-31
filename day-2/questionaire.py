import csv

nSkips = 3
skipCount = 0
stats = {}


with open("sofia-questionaire.csv") as fp:
    reader = csv.reader(fp)

    while skipCount < nSkips:
        next(reader)
        skipCount = skipCount + 1

    for row in reader:
        language1 = row[9].strip().lower()
        if language1 and language1 != "n/a":
            language, level = language1.split()
            if language in stats:
                stats[language] = stats[language] + 1
            else:
                stats[language] = 1


def printSummary():
    total = sum(stats.values())
    for language in stats:
        count = stats[language]
        pct = count / total * 100.0
        # print(language, count, pct)
        print(f"{language:15} {count:2} {pct:5.2f}%")

    print("There are", total, "students.")


printSummary()
