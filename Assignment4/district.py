import pandas as pd

df = pd.read_csv('data/districts.csv')

df[['municipality500','municipality1999','municipality9999','municipality10000']] = df.municipality_info.str.replace('[','').str.replace(']','').str.split(',').tolist()
df = df.drop('municipality_info',axis=1)

df[['unemployment_rate95','unemployment_rate96']] = df.unemployment_rate.str.replace('[','').str.replace(']','').str.split(',').tolist()
df = df.drop('unemployment_rate',axis=1)

df[['commited_crimes95','commited_crimes96']] = df.commited_crimes.str.replace('[','').str.replace(']','').str.split(',').tolist()
df = df.drop('commited_crimes',axis=1)

df.to_csv('district_py.csv',index=False)