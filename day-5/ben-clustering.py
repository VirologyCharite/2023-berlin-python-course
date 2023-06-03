from sklearn.cluster import KMeans, DBSCAN
import matplotlib.pyplot as plt
import argparse
import pandas as pd

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

parser.add_argument(
    "--eps", default=1.0, type=float,
    help="The EPS value (for DBSCAN)."
)

parser.add_argument(
    "--output", "-o",
    help="The (Excel) filename to write the results to."
)

parser.add_argument(
    "--sheet", default="agg",
    help="The Excel sheet name to read."
)

parser.add_argument(
    "--input", default="ben-data.xlsx",
    help="The Excel file to read."
)

parser.add_argument(
    "--indexColumn", default="category",
    help="The name of the Excel index column."
)

parser.add_argument(
    "--cols", nargs="*",
    help="Give the names of the columns to keep (default is all columns)."
)

args = parser.parse_args()

df = pd.read_excel(args.input, sheet_name=args.sheet,
                   index_col=args.indexColumn)

if args.cols:
    # args.cols.insert(0, "category")
    df = df[args.cols]

df.dropna(inplace=True)

# print(df.to_string())


if args.method == "dbscan":
    clustering = DBSCAN(eps=args.eps, min_samples=2)
    filename = "dbscan-demo.pdf"
else:
    clustering = KMeans(n_clusters=args.clusters, n_init="auto")
    filename = f"k-means-{args.clusters}-demo.pdf"

clustering.fit(df)

df["cluster"] = clustering.labels_

print(f"BS says: There were {max(clustering.labels_) + 1} clusters.")
print(f"TJ says: There were {len(set(clustering.labels_))} clusters.")

if args.output:
    df.to_excel(args.output, sheet_name=args.sheet)
