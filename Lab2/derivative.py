"""
derivative(f, x, h): Computes the numerical derivative of f at point x using step size h.
solve(f, x0, h): Uses Newton-Raphsons method to find a root of f starting from initial guess x0 with step size h.
"""
import math
def derivative(f, x, h):
  return (f(x + h) - f(x - h)) / (2 * h)

print(derivative(math.sin, math.pi / 2, 0.0001)) # should be close to 0
print(derivative(math.sin, math.pi, 0.0001)) # should be close to -1
print(derivative(math.sin, math.pi * 3 / 2, 0.0001)) # should be close to 0

def solve(f, x0, h):
  x1 = x0 - (f(x0) / derivative(f, x0, h)) # First iteration
  while abs(x1 - x0) > h:
    x0 = x1
    x1 = x0 - (f(x0) / derivative(f, x0, h)) # Next iteration
  return x1

def testfunc(x):
  return math.exp2(x) - 1

def testfunc2(x):
  return x - math.exp(-x)