library('ggplot2')
library('palmerpenguins')

p <- ggplot(data = penguins) + geom_point(mapping = aes(x = flipper_length_mm, y = body_mass_g, color = species)) +
  labs(title = "Penguin Flipper Length vs. Body Mass",
       subtitle = "Flipper length is a good indicator of body mass",
         caption = "Data from Palmer Station, Antarctica",
       x = "Flipper Length (mm)",
       y = "Body Mass (g)") 
        annotate("text", x = 200, y = 6000, label = "Source: https://allisonhorst.github.io/palmerpenguins")


p + annotate("text", x = 200, y = 6000, label = "Source: https://allisonhorst.github.io/palmerpenguins")
