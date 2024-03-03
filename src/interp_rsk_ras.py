import numpy as np
from scipy.interpolate import CubicSpline
from scipy import interpolate
import matplotlib.pyplot as plt

# calculate 5 natural cubic spline polynomials for 6 points
# (x,y) = (0,12) (1,14) (2,22) (3,39) (4,58) (5,77)
x = np.array([0, 120, 240, 480, 720])
y = np.array([0.740740740740741, 0.186266857362294, 0.676454228548988,
              1.45831443244151, 1.5075424370793])

# calculate natural cubic spline polynomials
cs = CubicSpline(x, y, bc_type='natural')
# cs = interpolate.interp1d(x, y, fill_value='extrapolate')

# show values of interpolation function at x=1.25
# print('S(1.25) = ', cs(1.25))

## Aditional - find polynomial coefficients for different x regions

# if you want to print polynomial coefficients in form
# S0(0<=x<=1) = a0 + b0(x-x0) + c0(x-x0)^2 + d0(x-x0)^3
# S1(1< x<=2) = a1 + b1(x-x1) + c1(x-x1)^2 + d1(x-x1)^3
# ...
# S4(4< x<=5) = a4 + b4(x-x4) + c5(x-x4)^2 + d5(x-x4)^3
# x0 = 0; x1 = 1; x4 = 4; (start of x region interval)

# show values of a0, b0, c0, d0, a1, b1, c1, d1 ...
# cs.c

# Polynomial coefficients for 0 <= x <= 1
a0 = cs.c.item(3, 0)
b0 = cs.c.item(2, 0)
c0 = cs.c.item(1, 0)
d0 = cs.c.item(0, 0)

# Polynomial coefficients for 1 < x <= 2
a1 = cs.c.item(3, 1)
b1 = cs.c.item(2, 1)
c1 = cs.c.item(1, 1)
d1 = cs.c.item(0, 1)

# Polynomial coefficients for 1 < x <= 2
a2 = cs.c.item(3, 2)
b2 = cs.c.item(2, 2)
c2 = cs.c.item(1, 2)
d2 = cs.c.item(0, 2)

# Polynomial coefficients for 1 < x <= 2
a3 = cs.c.item(3, 3)
b3 = cs.c.item(2, 3)
c3 = cs.c.item(1, 3)
d3 = cs.c.item(0, 3)

# Polynomial coefficients for 4 < x <= 5
# a4 = cs.c.item(3, 4)
# b4 = cs.c.item(2, 4)
# c4 = cs.c.item(1, 4)
# d4 = cs.c.item(0, 4)

# Print polynomial equations for different x regions
print('S0(0<=x<=2) = ', a0, ' + ', b0, '(x-0) + ', c0, '(x-0)^2  + ', d0, '(x-0)^3')
print('S1(1< x<=4) = ', a1, ' + ', b1, '(x-2) + ', c1, '(x-2)^2  + ', d1, '(x-2)^3')
print('S2(2< x<=6) = ', a2, ' + ', b2, '(x-4) + ', c2, '(x-4)^2  + ', d2, '(x-4)^3')
print('S3(3< x<=8) = ', a3, ' + ', b3, '(x-6) + ', c3, '(x-6)^2  + ', d3, '(x-6)^3')

# So we can calculate S(1.25) by using equation S1(1< x<=2)
# print('S(1.25) = ', a1 + b1*0.25 + c1*(0.25**2) + d1*(0.25**3))
print()
xs = np.arange(0, 721, .1)
print((cs(xs[-1])-cs(xs[-2]))/(xs[-1]-xs[-2]))
xs = np.arange(0, 720, .1)
fig, ax = plt.subplots(figsize=(6.5, 4))
ax.plot(x, y, 'o', label='data')
ax.plot(xs, cs(xs), label="S")
ax.set_xlim(-0.5, 730)
ax.legend(loc='lower left', ncol=2)
plt.show()