import pandas as pd

f = "256kB.txt"

df = pd.read_csv(f)

columns = list(df.columns)[1:]
newdf = df.copy()

for i in range(1, len(columns)):
    newdf[columns[i]] = df[columns[i]] - df[columns[i - 1]]



newdf.to_csv("int_" + f)
