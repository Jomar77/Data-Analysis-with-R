library(tidyverse)
library(ggplot2)
library(palmerpenguins)

ggplot(data=penguins2)+geom_point(mapping = aes(x=flipper_length_mm, y=body_mass_g, color=species,size=species,shape=species))
ggplot(data=penguins2)+geom_point(mapping = aes(x=flipper_length_mm, y=body_mass_g, alpha=species), color=("purple"))

  ggplot(data=penguins2)+geom_point(mapping = aes(x=bill_length_mm, y=bill_depth_mm))

glimpse(penguins2)
