import pandas as pd

datos=[
    {'nombre':'juan','edad':42,'departamento':'comunicacion'},
    {'nombre':'laura','edad':44,'departamento':'administracion'},
    {'nombre':'pepe','edad':37,'departamento':'ventas'}
]

df=pd.DataFrame(datos)

print(df)