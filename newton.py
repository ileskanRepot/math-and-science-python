from math import cos, exp
diff = 10E-15
x_0 = 4
x_latest = 0
steps = 0

def f(x): 
    return 6 * exp(-x/6) * cos(x)-1

def Df(x): 
    return (f(x+diff) - f(x))/diff

if abs(Df(x_0)) < 0.001:
    print("Pick better starting value")
    exit

while abs(x_0 - x_latest) > diff:
    steps += 1
    x_latest = x_0
    x_0 -= f(x_0)/Df(x_0)

print(x_0)
print(steps)
