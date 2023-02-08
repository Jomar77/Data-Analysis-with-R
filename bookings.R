bookings <- read.csv("bookings.csv")
trimmeddf <- bookings %>% select(hotel, is_canceled, lead_time)
head(trimmeddf)

example_df <- bookings_df %>% mutate(guests = sum(adults, children, babies, na.rm =TRUE) )
head(example_df)

example_df <- bookings %>% mutate(number_canceled = sum(is_canceled))
head(example_df)