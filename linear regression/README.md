Contains two main files-
regressionAlgorithm.py & regressionApplication.py

both use the same implementation of a linear regression algorithm.  The former uses arbitrary numbers to demonstrate usage, while
the latter (regressionApplication.py) uses data that I took from the website: <https://trends.collegeboard.org/college-pricing/figures-tables/average-net-price-over-time-full-time-students-sector>
Using numbers from public four-year universities over the time span given.




Mathematical Intuition behind implementation:

-linear equation of slope-intercept:
y = mx + b

-the slope m of the best-fit line is defined by:
m = ((x_bar * y_bar) - xy_bar) / ((x_bar)²-(x_bar²))

-then the y intercept is defined by:
b = y_bar - m * x_bar

-the r^2 value is defined by:
r^2 = 1 - ((Squared Error of Regression Line) / (Squared Error of y Mean Line))

Note: The closer the r-squared value is to 1, the better the fit of the line.
