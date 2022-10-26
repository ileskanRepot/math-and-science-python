import numpy as np
import matplotlib.pyplot as plt
def h(x):
    return x**3 - x

def g(x):
    return x**2

x = np.linspace ( start = -2
                , stop = 2
                , num = 51
                )
y = h(x)
plt.plot(x, h(x))



plt.plot( x
        , g(x)
        , 'r-'
        )

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend( [ 'h(x) = x^3 - x'
            , 'g(x) = x^2'
            ] )
plt.show()
