import pandas as pd
df=pd.DataFrame()

nombres=['juan','laura','pepe']
edades=[42,40,37]

df['nombre']=nombres
df['edad']=edades

nueva_fila={'nombre':'paco','edad':29}
df=df.append(nueva_fila,ignore_index=True)

nueva_fila=pd.Series(['ana',33],index=df.columns)
df=df.append(nueva_fila,ignore_index=True)

print(df)