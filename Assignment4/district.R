library(dplyr)
library(tidyr)
df = read.csv('data/districts.csv')

df = as.data.frame(apply(df,2, function(y) gsub('\\[|\\]','',y)))

tidy_df = df %>%
  separate(municipality_info,
           into = c('municipality500','municipality1999','municipality9999','municipality10000'),
           sep=',') %>%
  separate(unemployment_rate,
           into = c('unemployment_rate95','unemployment_rate96'),
           sep=',') %>%
  separate(commited_crimes,
           into = c('commited_crimes95','commited_crimes96'),
           sep=',')


write.csv(tidy_df,'district_r.csv')
