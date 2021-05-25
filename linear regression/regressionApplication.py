from statistics import mean
from matplotlib import pyplot as plt
from matplotlib import style
import pandas as pd
import numpy as np

# Load Tuition Data from Spreadsheet
dataset = pd.read_csv('TuitionData.csv')
x_values = np.array(dataset['Year'][0:9], dtype=np.float64)
y_values = np.array(dataset['Tuition'][0:9], dtype=np.float64)


# algorthm to calculate best-fit-line linear equation:
def best_fit_line(x_values,y_values):
    m = (((mean(x_values) * mean(y_values)) - mean(x_values * y_values)) /
         ((mean(x_values) * mean(x_values)) - mean(x_values * x_values)))
    b = mean(y_values) - m * mean(x_values)
    return m,b


# output linear eqution of best fit from input data:
m, b = best_fit_line(x_values, y_values)
print("Regression Equation of Best Fit Line: " + "y = " + str(round(m,3)) + "x + " + str(round(b,3)))


# Prediction Making
x_prediction = 2020
y_prediction = (m*x_prediction)+b
print("predicted Tuition (Year, Tuition): (" + str(round(x_prediction,2)) + ", $" + str(round(y_prediction,2)) + ")")



# R Squared value
regression_line = [(m*x)+b for x in x_values]

def squared_error(ys_orig, ys_line):
    return sum((ys_line - ys_orig) * (ys_line - ys_orig)) # helper function to return the sum of the distances between the two y values squared

def r_squared_value(ys_orig,ys_line):
    squared_error_regr = squared_error(ys_orig, ys_line) # squared error of regression line
    y_mean_line = [mean(ys_orig) for y in ys_orig] # horizontal line (mean of y values)
    squared_error_y_mean = squared_error(ys_orig, y_mean_line) # squared error of the y mean line
    return 1 - (squared_error_regr/squared_error_y_mean)

r_squared = r_squared_value(y_values, regression_line)
print("r^2 value: " + str(r_squared))


# Plotting of results:
style.use('seaborn')
plt.title('Linear Regression of Tuition')
plt.scatter(x_values, y_values,color='blue',label='data')
plt.scatter(x_prediction, y_prediction, color='red', label="predicted")
plt.plot(x_values, regression_line, color='black', label='regression line')
plt.legend(loc=4)
plt.show()
plt.savefig("graphtuition.png")





