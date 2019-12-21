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
h = (b - a) / n
for i in range(n):
    s += h * f1(a + h * i)
print("integral of x^2 from 0 to 3 is", s, "by rectangles")
s = (b - a) / 6 * (f1(a) + 4 * f1((a + b) / 2) + f1(b))
print("integral of x^2 from 0 to 3 is", s, "by Simpson's method")
s = 0
for i in range(n):
    s += h * f1(a + h * i + h / 2)
print("integral of x^2 from 0 to 3 is", s, "by trapezes")
s = (f1(b + 1 / n) - f1(b)) * n

s = 0
a = 0
b = math.pi / 2
h = (b - a) / n
for i in range(n):
    s += h * f2(a + h * i)
print("integral of sin(x) from 0 to pi/3 is", s, "by rectangles")
s = (b - a) / 6 * (f2(a) + 4 * f2((a + b) / 2) + f2(b))
print("integral of sin(x) from 0 to pi/3 is", s, "by Simpson's method")
s = 0
for i in range(n):
    s += h * f2(a + h * i + h / 2)
print("integral of sin(x) from 0 to pi/3 is", s, "by trapezes")
s = (f2(b + 1 / n) - f2(b)) * n

s = 0
a = 1
b = math.e
h = (b - a) / n
for i in range(n):
    s += h * f3(a + h * i)
print("integral of ln(x) from 1 to e is", s, "by rectangles")
s = (b - a) / 6 * (f3(a) + 4 * f3((a + b) / 2) + f3(b))
print("integral of ln(x) from 1 to e is", s, "by Simpson's method")
s = 0
for i in range(n):
    s += h * f3(a + h * i + h / 2)
print("integral of ln(x) from 1 to e is", s, "by trapezes")
s = (f3(a + 1 / n) - f3(a)) * n
