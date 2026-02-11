import sys
import pandas as pd

print("arguments", sys.argv)

month = int(sys.argv[1])
print(f"Runnin pipeline for month {month}")

df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
print(df.head())

df.to_parquet(f"output_{month:02d}.parquet")
print(f"Saved output_{month:02d}.parquet")