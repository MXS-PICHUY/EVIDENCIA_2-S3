import pandas as pd
import numpy as np

array=np.array([
    [10,11,12,13],
    [20,21,22,23],
    [30,31,32,33]
])
columnas=['C1','C2','C3','C4']

df=pd.DataFrame(array,columns=columnas)

print(df)