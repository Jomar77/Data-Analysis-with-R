library(tidyverse)
onlineta_city_hotels <- filter(bookings, 
                           (hotel=="City Hotel" & 
                             bookings$market_segment=="Online TA"))
