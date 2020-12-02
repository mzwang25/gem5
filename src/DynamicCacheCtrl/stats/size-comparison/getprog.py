import pandas as pd


print("benchmark,32,64,128,256,512,1024,2048,4096,8192")
dfs = []
files = ["int_32kB",
         "int_64kB",
         "int_128kB",
         "int_256kB",
         "int_512kB",
         "int_1024kB",
         "int_2048kB",
         "int_4096kB",
         "int_8192kB"
        ]


for f in files:
    dfs.append(pd.read_csv(f + ".txt"))

for bench in range(dfs[0].shape[0]):
    mntimes = []
    mntimes.append(dfs[0].iloc[bench][1])

    for df in dfs:
        mntimes.append(df.iloc[bench][2:].mean())

    print(",".join(map(str,mntimes)))
