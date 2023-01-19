#make linear regression model using hr and salary data
model <- lm(hr ~ salary, data = hr_salary)
#make predictions using the model
predictions <- predict(model, hr_salary)
#plot the predictions
plot(hr_salary$salary, predictions, col = "red", pch = 20, cex = 2)
#add the actual data
points(hr_salary$salary, hr_salary$hr, col = "blue", pch = 20, cex = 2)
#add a legend
legend("topleft", legend = c("Predictions", "Actual"), col = c("red", "blue"), pch = 20, cex = 2)
