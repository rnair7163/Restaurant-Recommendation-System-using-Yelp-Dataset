data <- read.csv("/Users/rahulnair/desktop/MS/Data_Preparation_and_Analysis/Recommendation_System_for_yelp/EDA/Business_in_Illinois.csv", header = T)
library(ggplot2)
library(mapproj)
library(maps)
maps <- map_data("county")
ggplot(maps, aes(x=long, y=lat))  +
  borders("state") +
  coord_map() +
  geom_point(data=data, aes(x=data$longitude, y=data$latitude), color="orange")

map('state', 'illinois')
points(data$longitude, data$latitude, col = 'blue', cex=.6)
?map_data
