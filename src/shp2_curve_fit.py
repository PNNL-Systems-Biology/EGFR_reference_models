
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import pandas as pd
import tellurium as te

shp2_datafile = 'shp2_input.txt'

data_df = pd.read_csv(shp2_datafile, delimiter=r"\s+")

time = np.array(data_df['Time'])
Shp2 = np.array(data_df['Shp2'])

print(time)
print(Shp2)

def lr5(x, a, b, c, d, s):
    return a + (d - a) / ((1 + (x/c) ** b) ** s)
popt, pcov = curve_fit(lr5, time, Shp2)

# def cubic(x, a, b, c, d):
#     return a + b * x + c * x ** 2 + d * x ** 3
# popt, pcov = curve_fit(cubic, time, Shp2, bounds = ([0, -10, -10, -10], [10, 10, 10, 10]))

# def quad(x, a, b, c):
#     return a + b * x + c * x ** 2
# popt, pcov = curve_fit(quad, time, Shp2, bounds = ([0, -100, -100], [100, 100, 100]))

# erk_df = pd.read_csv(erk_datafile, delimiter=r"\s+")
# erk_time = np.array(erk_df['Time'])
# print(erk_df)
# erk = np.array(erk_df['Rp'])

# r = te.loada('current_model.ant')
# sim = r.simulate(0, 10, 101, selections=['time', 'ppERK'])
# print(11, sim['ppERK'])

print(popt)
t = np.linspace(0, 10, 101)
print(t)
# quit()
# plt.plot(t, cubic(t, *popt), 'r-', c='blue', label='fit: a=%5.3f, b=%5.3f, c=%5.3f, d=%5.3f' % tuple(popt))
plt.plot(t, lr5(t, *popt), 'r-', c='blue', label='fit: a=%5.3f, b=%5.3f, c=%5.3f, d=%5.3f, s=%5.3f' % tuple(popt))
# plt.plot(t, quad(t, *popt), 'r-', c='blue', label='fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt))
# plt.plot(t, sim['ppERK'], c='orange')
plt.scatter(time, Shp2, c='blue')
# plt.scatter(erk_time, erk, c='orange')
plt.show()
