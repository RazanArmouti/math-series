
""" 
The Fibonacci Sequence is the series of numbers:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
starting with integer 0 and 1. The next number is found by adding up the two numbers before it.

"""
def fibonacci(n):
    if type(n)!=int:
       return "The value must be integer"
    elif n < 0:
       return "The value must be positive"
    elif n == 0:
       return 0
    elif n == 1 or n == 2:
       return 1 
    else:
       return fibonacci(n-1) + fibonacci(n-2)
    
"""
Lucas sequence has the same recursive relationship as the Fibonacci sequence, 
2, 1, 3, 4, 7, 11, 18, 29, 47, 76, 123, ....
where each term is the sum of the two previous terms, 
but with different starting values 2,1

"""

def lucas(n):
    if type(n)!=int:
      return "The value must be integer"
    elif n < 0:
      return "The value must be positive"
    elif n == 0:
      return 2
    elif n == 1:
      return 1
    else:
      return lucas(n-1) + lucas(n-2)

"""
  sum_series is a function  with one required parameter and two optional parameters. 
  The required parameter will determine which element in the series to print.
  The two optional parameters will have default values of 0 and 1 and
  will determine the first two values for the series to be produced.
"""
def sum_series(n,val1=0, val2=1):
    if type(n)!=int:
        return "The value must be integer"
    if n < 0 : 
        return "The value must be positive"
    elif(val1==0 and val2==1):
        return fibonacci(n)
    elif( val1==2 and val2==1):
        return lucas(n)
    else: 
        if n==0:
            return val1
        elif n==1:
            return val2
        else:
            return sum_series(n-1,val1,val2)+sum_series(n-2,val1,val2)
