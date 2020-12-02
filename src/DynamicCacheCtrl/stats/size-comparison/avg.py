#!/usr/bin/python
import pandas as pd
import sys

fs = [
  "diff_int_128kB.txt",
  "diff_int_256kB.txt",
  "diff_int_512kB.txt",
  "diff_int_1024kB.txt",
  "diff_int_2048kB.txt",
  "diff_int_4096kB.txt",
  "diff_int_8192kB.txt"
]

for f in fs:
    df = pd.read_csv(f)
    print(df.iloc[3][3:].mean())
