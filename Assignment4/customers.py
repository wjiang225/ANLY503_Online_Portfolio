import pandas as pd
from pandas import DataFrame

dis = pd.read_csv('district_py.csv',low_memory=False)
loan = pd.read_csv('loans_py.csv',low_memory=False)
acc = pd.read_csv('data/accounts.csv',low_memory=False)
card = pd.read_csv('data/cards.csv',low_memory=False)
link = pd.read_csv('data/links.csv',low_memory=False)
cli = pd.read_csv('data/clients.csv',low_memory=False)
pay = pd.read_csv('data/payment_orders.csv',low_memory=False)
trc = pd.read_csv('data/transactions.csv',low_memory=False)

dis_name = []
for x in acc.district_id:
    dis_name.append(dis[dis['id']==x].reset_index().name[0])


df = DataFrame()
df['account_id'] = acc.id
df['district_name'] = dis_name
df['open_date'] = acc.date
df['statement_frequency'] = acc.statement_frequency


num_customer = []
for x in acc.id:
    num_customer.append(len(link[link['account_id']==x]))
df['num_customers'] = num_customer


num_card = []
for x in link.id:
    num_card.append(len(card[card['link_id']==x]))
link['num_card'] = num_card
cred_card = []
for x in acc.id:
    cred_card.append(sum(link[link['account_id']==x].num_card))
df['credit_cards'] = cred_card


if_loan = []
amount = []
payment = []
term = []
status = []
default = []
for x in acc.id:
    l = len(loan[loan['account_id'] == x])
    if l == 0:
        if_loan.append('F')
        amount.append('NA')
        payment.append('NA')
        term.append('NA')
        status.append('NA')
        default.append('NA')

    else:
        if_loan.append('T')
        amount.append(loan[loan['account_id'] == x].reset_index().amount[0])
        payment.append(loan[loan['account_id'] == x].reset_index().payments[0])
        term.append(loan[loan['account_id'] == x].reset_index().term[0])
        status.append(loan[loan['account_id'] == x].reset_index().status[0])
        default.append(loan[loan['account_id'] == x].reset_index().default[0])

df['loan'] = if_loan
df['loan_amount'] = amount
df['loan_payments'] = payment
df['loan_term'] = term
df['loan_status'] = status
df['loan_default'] = default

max_w = []
min_w = []
cc = []
max_b = []
min_b = []

for x in acc.id:
    info = trc[trc['account_id'] == x]
    max_w.append(max(info.amount))
    min_w.append(min(info.amount))

    max_b.append(max(info.balance))
    min_b.append(min(info.balance))

    cred = info[info['type'] == 'credit']
    cc.append(len(cred))

df['max_withdrawal'] = max_w
df['min_withdrawal'] = min_w
df['cc_payments'] = cc
df['max_balance'] = max_b
df['min_balance'] = min_b

df.to_csv('customers_py.csv',index=False)