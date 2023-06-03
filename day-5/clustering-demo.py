from sklearn.cluster import KMeans, DBSCAN
import matplotlib.pyplot as plt
import argparse


parser = argparse.ArgumentParser(description="Make a cluster plot")

parser.add_argument(
    "--method", choices=("k-means", "dbscan"),
    default="k-means",
    help="Set the clustering method."
)

parser.add_argument(
    "--clusters", "-k", default=5, type=int,
    help="Give the number of clusters (for k-means)."
)

args = parser.parse_args()


x = [4, 5, 10, 4, 3, 11, 14, 6, 10, 12]
y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]

data = list(zip(x, y))


def elbowPlot():
    inertias = []

    for i in range(1, 11):
        kmeans = KMeans(n_clusters=i, n_init="auto")
        kmeans.fit(data)
        inertias.append(kmeans.inertia_)

    plt.plot(range(1, 11), inertias, marker="o")
    plt.title("Elbow method")
    plt.xlabel("Number of clusters")
    plt.ylabel("Inertia")
    plt.show()


if args.method == "dbscan":
    clustering = DBSCAN(eps=3, min_samples=2)
    filename = "dbscan-demo.pdf"
else:
    clustering = KMeans(n_clusters=args.clusters, n_init="auto")
    filename = f"k-means-{args.clusters}-demo.pdf"


clustering.fit(data)

plt.scatter(x, y, c=clustering.labels_)

plt.savefig(filename)
print(f"{args.method} plot saved to {filename!r}.")
