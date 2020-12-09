library(dplyr)
library(tidyr)
df = read.csv('data/loans.csv')


len = length(df)
terms = df[,6:len]
labels = colnames(terms)

a = data.frame(which(terms == 'X',TRUE))
a = a[order(a$row),]

df = df[,1:5]
df$term = labels[a$col]
df = as.data.frame(apply(df,2, function(y) gsub('X','',y)))

tidy_df = df %>%
  separate(term,
           into=c('term','st'),
           sep='_')

status = c()
default = c()
for(x in tidy_df$st){
  if(x == 'A'){
    status = c(status,'expired')
    default = c(default,'F')
  }
  else if(x == 'B'){
    status = c(status,'expired')
    default = c(default,'T')
  }
  else if(x == 'C'){
    status = c(status,'current')
    default = c(default,'F')
  }
  else{
    status = c(status,'current')
    default = c(default,'T')
  }
}

tidy_df$status = status
tidy_df$default = default
tidy_df$st = NULL
tidy_df


write.csv(tidy_df,'loans_r.csv')
