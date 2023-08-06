
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import pandas as pd
import tellurium as te

ras_datafile = 'ras_input.txt'
erk_datafile = 'erk.txt'

data_df = pd.read_csv(ras_datafile, delimiter=r"\s+")

time = np.array(data_df['Time'])
Rp = np.array(data_df['Rp'])


def cubic(x):
    return 12.69798 * x - 1.9101 * x ** 2 + 0.08355 * x ** 3


erk_df = pd.read_csv(erk_datafile, delimiter=r"\s+")
erk_time = np.array(erk_df['Time'])
erk = np.array(erk_df['Rp'])

r = te.loada('current_model.ant')
r.integrator.absolute_tolerance = 1e-12
r.integrator.relative_tolerance = 1e-12
sim = r.simulate(0, 10, 1001, selections=['time', 'RAS', 'ppERK', 'RASb_pRAF_d1433u_MEK'])
print(11, sim['RASb_pRAF_d1433u_MEK'])

t = np.linspace(0, 10, 1001)
print(t)
# quit()
# plt.plot(t, cubic(t), c='blue', label='RAS curve')
# plt.plot(t, sim['ppERK'], c='purple', label='RAS_out')
# plt.plot(t, sim['ppERK'], c='orange', label='ERK fit')
plt.plot(t, sim['RASb_pRAF_d1433u_MEK'], c='green', label='RAFa trace')
# plt.scatter(time, Rp, c='blue', label='RAS data')
# plt.scatter(erk_time, erk, c='orange', label='ERK data')
plt.legend()
plt.show()

# r = te.loada('RAF_activation_2022.ant')
# sim = r.simulate(0, 10, 1001, selections=['time', 'ppERK'])
# # sim = r.simulate(0, 10, 1001)
# print(sim)
# r.plot()
