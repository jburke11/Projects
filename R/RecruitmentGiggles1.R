#######################################################
### Do giggles recruit allies?
#######################################################


# Load packages
library("dplyr")
library("readxl")
library("tidyverse")
library("ggpubr")
library("xlsx")
library("lubridate")
# Set working directory
setwd("C:/hyena")

# Load data
my_data <- read_xlsx("Table1.xlsx")
attach(my_data) 



# Get rid of data where giggles come from the aggressor 
# Use the subset function 
newdata <- subset(my_data, recip==FirstOfaggressor)

# subset function
newdata1 <- subset(my_data, recip==arriver)
dataset <- subset(my_data, recip!=arriver)

#### Determine relatedness between hyenas
# Create an emptry column to store the relatedness score
dataset$relatedness <- NA

# Assign relatedness between giggler and arriver
# Write a for loop with an if statement that says
# for each row of the dataset, if arriver = mom, relatedness_score_column <- 

#replace NAs with empty strings
dataset$arr_grandmom[is.na(dataset$arr_grandmom)] <- ""
dataset$recip_grandmom[is.na(dataset$recip_grandmom)] <- ""



for (i in 1:nrow(dataset)){ #cycle through each row of the dataset. i goes up by 1 on each cycle
  if(dataset$arriver[i]==dataset$recip_mom[i]) { # if the arriver column at row i equals the rec_mom column at row i then exectute the next line
    dataset$relatedness[i] <- 50    # this line only gets executed if what above it is TRUE.
    # This line says to save 0.5 as the value of your dataset, row i, column "relatedness"
  } else if (dataset$recip_mom[i]==dataset$arr_mom[i]) { # If recip and arr are sisters
    dataset$relatedness[i] <- 50
  } else if (dataset$arr_grandmom[i]==dataset$recip_grandmom[i]) {  # if the recip and arr are cousins
    dataset$relatedness[i] <- 12.5
  } else if (dataset$recip_grandmom[i]==dataset$arr_mom[i] ) { #aunt
    dataset$relatedness[i] <- 25
  } else if (dataset$recip_grandmom[i]==dataset$arr_mom[i] ) { #niece/nephew
    dataset$relatedness[i] <- 25                          
  }else if (dataset$recip[i]==dataset$arr_mom[i] ) {
    dataset$relatedness[i] <- 50 
  }else if (dataset$arriver[i]==dataset$recip_grandmom[i]) {
    dataset$relatedness[i] <- 25
  }else if (dataset$arr_grandmom[i]==dataset$recip[i]) {
    dataset$relatedness[i] <- 25 
  }else {
    dataset$relatedness[i] <- 0.0
  } # this is the closing bracket for the most recent else if statement
} # this is the closing bracket for the start of the for loop







### Use group_by to get the average relatedness of all of the arrivers for each aggression 
# The line below groups your data so that all of the arrivers for each aggression are grouped together (by aggid). 
# this will allow you to do stats on the groups.  For example, you'll be able to find the mean relatedness 
# of all the arrivers for each aggid. Which is what I do below.
grouped_by_giggle <- dataset %>% group_by(aggid)

# This finds the mean of the relatedness for each giggle and saves it.
#Change recip to a factor datatype
grouped_by_giggle$recip <- as.factor(grouped_by_giggle$recip)

meanrelatedness <- grouped_by_giggle %>% summarize(

  recip = first(recip),
  mean_relatedness = mean(relatedness),
  date = first(agg_date),
  n_arrivers =n()
)

# now you want to pull the year out of the date so you can do the join in the next section below.
meanrelatedness$date <- year(ymd(meanrelatedness$date)) # ymd converts your date column into a date format that the function year understands. Then function year pulls the year out of your date.



# Calculate relatedness of the entire clan for each giggler (you may need to do this by hand, directions in email)
# load dataset created
clanR <- read_xlsx("final relatedness.xlsx")

# Assign relatedness of clan to each giggler with a join by year and hyena_id
clanR$hyena <- tolower(clanR$hyena)

AllRelatedness <- left_join(meanrelatedness, clanR, by=c("recip" = "hyena", "date"="year"))




# Paired t-test
t.test(AllRelatedness$mean_relatedness, AllRelatedness$relatedness, paired=TRUE)

# Graph

boxplot(AllRelatedness$mean_relatedness, AllRelatedness$relatedness, ylab="Relatedness", col="grey", main="Relatedness of arrivers vs. Average clan relatedness", names= c("Arrivers","Clan"),cex.axis=1.5, cex.lab=1.5, cex.main=1.5)
stripchart(AllRelatedness$mean_relatedness, at=1, vertical=TRUE, pch=21, add=TRUE, method = "jitter", jitter=.2)
stripchart(AllRelatedness$relatedness, at=2, vertical=TRUE, pch=21, add=TRUE, method = "jitter", jitter=.1)
