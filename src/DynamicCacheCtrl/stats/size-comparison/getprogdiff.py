#!/usr/bin/python
import pandas as pd


print("benchmark,64,128,256,512,1024,2048,4096,8192")
dfs = []
files = [
         "diff_int_64kB",
         "diff_int_128kB",
         "diff_int_256kB",
         "diff_int_512kB",
         "diff_int_1024kB",
         "diff_int_2048kB",
         "diff_int_4096kB",
         "diff_int_8192kB"
        ]


for f in files:
    dfs.append(pd.read_csv(f + ".txt"))

for bench in range(dfs[0].shape[0]):
    mntimes = []
    for df in dfs:
        mntimes.append(df.iloc[bench][3:].mean())

    print(",".join(map(str,mntimes)))
