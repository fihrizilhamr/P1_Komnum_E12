# import matplotlib for plotting and numpy for linspace
import matplotlib.pyplot as plt
import numpy as np

def xt(x1, x2):
    return ((x1 + x2) / 2)

def fx(x):
    return x ** 3 + x ** 2 - 3 * x - 3

# formatted print
def scanlines(i, x, y, z, fx, fy, fz):
    print(f" {i} |" + f"{x:+.07f}|" + f"{y:+.07f}|" + f"{z:+.07f}|" + f"{fx:+.8f}|" + f"{fy:+.08f}|" + f"{fz:+.08f}")

# utility
def fDigit(x):
    digitCount = 0
    while (x != 0):
        x = int(int(x) / 10)
        digitCount += 1
    return digitCount

# intialiaze the list
x1 = []
x2 = []
x3 = []
fx1 = []
fx2 = []
fx3 = []

# inserting the first x1 and x2 value
x1.append(int(1))
x2.append(int(2))
x3.append(xt(x1[0], x2[0]))
x = np.linspace(int(1),int(2),10)

fx1.append(fx(x1[0]))
fx2.append(fx(x2[0]))
fx3.append(fx(x3[0]))

i = 0

print(" I |    X1    |    X2    |    X3    |   f(x1)   |   f(x2)   |   f(x3)   ")
scanlines(i + 1, x1[i], x2[i], x3[i], fx1[i], fx2[i], fx3[i])

# while (fx3[i] != 0): #needle point accuracy
while (fx3[i - 1] > 0.00000001 or fx3[i - 1] < -0.00000001):  # accurate to 8 decimal
    # for j in range(0,31): #testbed
    if (fx3[i] < 0):
        x1.append(x3[i])
        x2.append(x2[i])
    if (fx3[i] > 0):
        x1.append(x1[i])
        x2.append(x3[i])
    i += 1

    fx1.append(fx(x1[i]))
    fx2.append(fx(x2[i]))
    x3.append(xt(x1[i], x2[i]))
    fx3.append(fx(x3[i]))

    scanlines(i + 1, x1[i], x2[i], x3[i], fx1[i], fx2[i], fx3[i])

# plot graph, using the first x1 and x2 as boundaries
plt.plot(x,fx(x))
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Graph')
plt.grid(True)
plt.show()
