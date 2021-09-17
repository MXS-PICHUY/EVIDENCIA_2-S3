import pandas as pd

df=pd.DataFrame()

df['mañana']=None
df['tarde']=None
df['noche']=None

df.loc['lunes']=['tension','alergia','sedante']
df.loc['martes']=['tension','none','alergia']
df.loc['miercoles']=['protector','alergia','tension']

print(df)