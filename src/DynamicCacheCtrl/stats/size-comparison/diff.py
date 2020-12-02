#!/usr/bin/python

import pandas as pd
import sys

files = [
          "int_128kB.txt",
          "int_256kB.txt",
          "int_512kB.txt",
          "int_1024kB.txt",
          "int_2048kB.txt",
          "int_4096kB.txt",
          "int_8192kB.txt",
        ]

for i in range(1, len(files)):
    col = (pd.read_csv(files[i-1]).iloc[:,0])
    base = pd.read_csv(files[i-1]).drop('Name', 1)
    cmpw = pd.read_csv(files[i]).drop('Name', 1)


    diff = cmpw.div(base)
    percent = diff
    percent.insert(0, "benchmark", col)

    percent.to_csv("diff_" + files[i])
