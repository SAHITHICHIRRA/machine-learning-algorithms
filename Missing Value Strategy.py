import numpy as np
import pandas as pd

marks = [40,None,60,70,None,90]

df = pd.DataFrame(marks)

print(df.isnull())

mean_fill = df.fillna(df.mean())

median_fill = df.fillna(df.median())

print(mean_fill)
print(median_fill)
