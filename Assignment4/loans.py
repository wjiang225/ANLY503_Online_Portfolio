import pandas as pd

df = pd.read_csv('data/loans.csv')

terms = df.iloc[:,5:]
label = list(terms.columns)
term_value = terms.values.tolist()

t = []
for x in term_value:
    index = x.index('X')
    t.append(label[index])

df = df.drop(columns=label)

term = []
status = []
default = []
for x in t:
    tm,st = x.split('_')
    term.append(tm)
    if st == 'A':
        status.append('expired')
        default.append('F')
    elif st == 'B':
        status.append('expired')
        default.append('T')
    elif st == 'C':
        status.append('current')
        default.append('F')
    else:
        status.append('current')
        default.append('T')

df['term'] = term
df['status'] = status
df['default'] = default


df.to_csv('loans_py.csv',index=False)