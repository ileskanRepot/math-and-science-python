from math import pi, sin, exp, log
start = 2.2
end = 5.5
scale = 24
step = (end - start)/scale

def f(x): return exp(x)/log(x)

cur = f(start)
print("1",cur)

for i in range(1,int(scale)):
    if i%2 == 1:
        val = 4*f(start+(i * step))
    else:
        val = 2*f(start+(i * step))
    cur += val
    print(start+i*step,val)

cur += f(end)
cur *= ((end-start)/scale)/3 

print(cur)

