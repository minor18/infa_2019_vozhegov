import math
n = int(input())

def f1(x):
    return x**2


def f2(x):
    return math.sin(x)


def f3(x):
    return math.log(x)

s = 0
a = 0
b = 3
s = (f1(b + 1 / n) - f1(b)) * n
print("derivative of x^2 in 3 is", s, "by definition")
s1 = (f1(b + 1 / n + 1 / n) - f1(b + 1 / n)) * n
s = (s1 - s) * n
print("second derivative of x^2 in 3 is", s, "by definition")

s = 0
a = 0
b = math.pi / 2
print("derivative of sin(x) in pi/3 is", s, "by definition")
s1 = (f2(b + 1 / n + 1 / n) - f2(b + 1 / n)) * n
s = (s1 - s) * n
print("second derivative of sin(x) in pi/3 is", s, "by definition")

s = 0
a = 1
b = math.e
print("derivative of ln(x) in 1 is", s, "by definition")
s1 = (f3(a + 1 / n + 1 / n) - f3(a + 1 / n)) * n
s = (s1 - s) * n
print("second derivative of ln(x) in 1 is", s, "by definition")
