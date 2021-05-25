# someFunctions.py    Defining a few sample functions in Python for applicable use
# P.K. Rhee

# CtoF: number -> number
#   consumes: a temperature in Celsius
#   produces: a temperature in Fahrenheit

import math;

def CtoF(cTemp):
    return (cTemp / 5.0) * 9 + 32

def distance(x1,y1,x2,y2):
    return math.sqrt( square(x2-x1) + square(y2-y1) )


#  squared: number -> number
#  consumes: a number x
#  returns: the square of that number
def square(x):
    return x * x;

# mortgage: number -> number
# consumes: the long amount 'a', interest rate 'r', and loan terms 't', where 'c=r/1200'
# returns: the monthly mortgage 'm'
def mortgage(a,r,t)
    c=r/1200
    m = (((a * c * (1+c)**2))/( ((1+c)**t)) * 1))
    return m;