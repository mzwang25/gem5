#!/usr/bin/python

import pandas as pd
import sys

print(pd.read_csv(sys.argv[1]).iloc[:,0])

base = pd.read_csv(sys.argv[1]).drop('Name', 1)
cmpw = pd.read_csv(sys.argv[2]).drop('Name', 1)

diff = base.subtract(cmpw)
pdiff = diff.divide(base)
percent = pdiff.mul(100)

print("%diff")
print(percent)

