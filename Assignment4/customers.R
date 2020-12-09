library(dplyr)
library(tidyr)

dis = read.csv('district_r.csv')
loan = read.csv('loans_r.csv')
acc = read.csv('data/accounts.csv')
card = read.csv('data/cards.csv')
link = read.csv('data/links.csv')
cli = read.csv('data/clients.csv')
pay = read.csv('data/payment_orders.csv')
trc = read.csv('data/transactions.csv')


df = acc
df$district_name = dis$name[df$district_id]
df$district_id = NULL
colnames(df)[1:2] = c('account_id','opening_date')


num_card = c()
for(x in link$id){
  num_card = c(num_card,nrow(card[card$link_id==x,]))
}
link$num_card = num_card
df$credit_cards = aggregate(num_card ~ account_id, link, sum)$num_card



has_loan = c()
amount = c()
payment = c()
term = c()
status = c()
default = c()
max_w = c()
min_w = c()
cc = c()
max_b = c()
min_b = c()

for(x in df$account_id){
  info = loan[loan$account_id==x,]
  if(nrow(info) == 0){
    has_loan = c(has_loan,'F')
    amount = c(amount,'NA')
    payment = c(payment,'NA')
    term = c(term,'NA')
    status = c(status,'NA')
    default = c(default,'NA')
  }
  else{
    has_loan = c(has_loan,'T')
    amount = c(amount,info$amount)
    payment = c(payment,info$payment)
    term = c(term, info$term)
    status = c(status,info$status)
    default = c(default,info$default)
  }
  info2 = trc[trc$account_id==x,]
  max_w = c(max_w,max(info2$amount))
  min_w = c(min_w,min(info2$amount))
  max_b = c(max_b,max(info2$balance))
  min_b = c(min_b,min(info2$balance))
  cc = c(cc,nrow(info2[info2$type == 'credit',]))
}
df$loan = has_loan
df$loan_amount = amount
df$loan_payment = payment
df$loan_term = term
df$loan_status = status
df$loan_default = default
df$max_withdrawal = max_w
df$min_withdrawal = min_w
df$cc_payment = cc
df$max_balance = max_b
df$min_balance = min_b


write.csv(df,'customers_r.csv')
