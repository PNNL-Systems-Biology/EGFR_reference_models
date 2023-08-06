
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import pandas as pd
import tellurium as te

ras_datafile = 'ras_input_2.txt'
erk_datafile = 'erk.txt'

data_df = pd.read_csv(ras_datafile, delimiter=r"\s+")

time = np.array(data_df['Time'])
Rp = np.array(data_df['Rp'])

print(time)
print(Rp)

def lr5(x, a, b, c, d, s):
    return a + (d - a) / ((1 + (x/c)**b) ** s)

def cubic(x, a, b, c, d):
    return a + b * x + c * x ** 2 + d * x ** 3

popt, pcov = curve_fit(cubic, time, Rp, bounds = ([0, -100, -100, -100], [100, 100, 100, 100]))

erk_df = pd.read_csv(erk_datafile, delimiter=r"\s+")
erk_time = np.array(erk_df['Time'])
erk = np.array(erk_df['Rp'])

r = te.loada('current_model.ant')
sim = r.simulate(0, 10, 101, selections=['time', 'ppERK'])
print(11, sim['ppERK'])

print(popt)
t = np.linspace(0, 10, 101)
print(t)
# quit()
plt.plot(t, cubic(t, *popt), 'r-', c='blue', label='fit: a=%5.3f, b=%5.3f, c=%5.3f, d=%5.3f' % tuple(popt))
# plt.plot(t, sim['ppERK'], c='orange')
plt.scatter(time, Rp, c='blue')
# plt.scatter(erk_time, erk, c='orange')
plt.show()
