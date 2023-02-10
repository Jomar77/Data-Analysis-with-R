library(tidyverse)
library(palmerpenguins)

# Load the data
ggplot(data = penguins) +
  geom_smooth(mapping = aes(x =flipper_length_mm,y=body_mass_g)) +
  geom_point(aes(color=species))+
  facet_wrap(~species)