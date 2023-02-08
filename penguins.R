penguins %>%
  select(-species)

penguins %>%
  rename(island_new=island)
rename_with(penguins,tolower)  
clean_names(penguins)
