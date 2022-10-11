from math import cos, exp

def f(x): return (6 * exp(-x/6) * cos(x) - 1)

diff = 10E-7
x_0 = 7
x_1 = 100
ka = (x_0 + x_1)/2

if (f(x_0) * f(x_1)) > 0:
    print("Pick better starting values")
    exit

while ka - x_0 > diff:
    if (f(x_0) * f(ka)) > 0:
        x_0 = ka
    else:
        x_1 = ka
    ka = (x_0 + x_1)/2
print(x_0,f(x_0))
print(x_1,f(x_1))
