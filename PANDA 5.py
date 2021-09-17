import pandas as pd

datos={
    'nombre':['juan','laura','pepe'],
    'edad':[42,40,37],
    'departamento':['comunicacion','administarcion','ventas']
}

df=pd.DataFrame(datos)

print(df)