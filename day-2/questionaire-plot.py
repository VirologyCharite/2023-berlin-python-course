import csv
from collections import Counter
import matplotlib.pyplot as plt

nSkips = 3
skipCount = 0
stats = Counter()


with open("sofia-questionaire.csv") as fp:
    reader = csv.reader(fp)

    while skipCount < nSkips:
        next(reader)
        skipCount += 1

    for row in reader:
        language1 = row[9].strip().lower()
        if language1 and language1 != "n/a":
            language, level = language1.split()
            stats[language] += 1


def printSummary():
    total = stats.total()
    for language in stats:
        count = stats[language]
        pct = count / total * 100.0
        print(f"{language:15} {count:2} {pct:5.2f}%")

    print("There are", total, "students.")


def plotSummary():
    languages = []
    counts = []
    fig, ax = plt.subplots()

    # Put the languages and counts into the corresponding variables.
    for language in sorted(stats):
        count = stats[language]
        languages.append(language.title())
        counts.append(count)

    ax.bar(languages, counts)

    ax.set_ylabel("Count")
    ax.set_title("Student first language counts")
    plt.xticks(rotation=31)

    plt.savefig("student-languages.pdf")


printSummary()
plotSummary()
