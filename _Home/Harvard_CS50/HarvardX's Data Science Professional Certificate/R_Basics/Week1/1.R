# installing the dslabs package
install.packages("dslabs")
library(dslabs)
install.packages("tidyverse")
a <- 3
b <- 2
c <- -1
(-b + sqrt(b^2 - 4*a*c)) / (2*a)
(-b - sqrt(b^2 - 4*a*c)) / (2*a)

#excercise 1
n = 100
x = seq(1,n)
print(x)
sum(x)
#3 antwoord c
#4
log(sqrt(100),base=10)
#5
x=5
log(exp(x))

library(tidyverse)
library(dslabs)
data(murders)

murders %>%
    ggplot(aes(population, total, label=abb, color=region)) +
    geom_label()
