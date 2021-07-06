#Statistical analysis 
install.packages('treemap')
#classify data
data = world.happiness.report.2021

#Transform data into R dataframe
as_data_frame(data)

#Take a look at data 
head(data)

summary(data)
#conducting an Anova 
#Question set up: Is there a significant difference between Regions and the ladder score?

#testing assumptions
plotNormalHistogram(data$Ladder.score)
#The data is normally distrubuted

# Homogeneity of Variance test 
fligner.test(Ladder.score ~ Regional.indicator, data=data)

# The p value is > .05, assumption passed

#last assumption is our sample size which is great than 20, this is passed

#Conducting one way Anova


dataANOVA <- aov(data$Ladder.score ~ data$Regional.indicator)
summary(dataANOVA)

#The F statistical proved significant

# Post Hocs analysis with adjustment for type 1 error
pairwise.t.test(data$Ladder.score, data$Regional.indicator, p.adjust="bonferroni")


# Western europe, Sub-Suharan Africa, Middle east, and south asia are the significant groups 

# data visualization
# Ladder score vs GDP
d <- ggplot(data = data, aes(x = Ladder.score, y = Logged.GDP.per.capita))
d + geom_point() + geom_smooth(method=lm)


d <- ggplot(data = data, aes(x = Ladder.score, y = Generosity))
d + geom_point() + geom_smooth(method=lm)

d <- ggplot(data = data, aes(x = Ladder.score, y = Healthy.life.expectancy))
d + geom_point() + geom_smooth(method=lm)

d <- ggplot(data = data, aes(x = Ladder.score, y = Regional.indicator))
d + geom_point() + geom_smooth(method=lm)

#Correlation Test

cor.test(data$Logged.GDP.per.capita, data$Freedom.to.make.life.choices, method="pearson", use = "complete.obs")

# the countries GDP has a weak correlation with the Freedom to make life choices factor

# conducting linear regression
lin_reg <- lm(Social.support ~ Ladder.score, data)
print(lin_reg)

# y = 0.08097x + 0.36674 is the linear model

summary(lin_reg)

