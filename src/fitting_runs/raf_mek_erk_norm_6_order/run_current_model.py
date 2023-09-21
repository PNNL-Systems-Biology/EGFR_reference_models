
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import pandas as pd
import tellurium as te

ras_datafile = 'ras_input_2.txt'
erk_datafile = 'erk.txt'
raf_datafile = 'raf.txt'
mek_datafile = 'mek.txt'
egfr_datafile = 'egfr.txt'

data_df = pd.read_csv(ras_datafile, delimiter=r"\s+")
time = np.array(data_df['Time'])
Rp = np.array(data_df['Rp'])


def cubic(x):
    return 8.06650728 * x - 0.891469156 * x ** 2 + 0.0265125689 * x ** 3


erk_df = pd.read_csv(erk_datafile, delimiter=r"\s+")
erk_time = np.array(erk_df['Time'])
erk = np.array(erk_df['Erk'])

raf_df = pd.read_csv(raf_datafile, delimiter=r"\s+")
raf_time = np.array(raf_df['Time'])
raf = np.array(raf_df['Raf'])

mek_df = pd.read_csv(mek_datafile, delimiter=r"\s+")
mek_time = np.array(raf_df['Time'])
mek = np.array(mek_df['Mek'])

# egfr_df = pd.read_csv(egfr_datafile, delimiter=r"\s+")
# egfr_time = np.array(egfr_df['Time'])
# egfr = np.array(egfr_df['aRtot'])

r = te.loada('current_model.ant')
# r = te.loada('current_model_5.ant')
r.integrator.absolute_tolerance = 1e-12
r.integrator.relative_tolerance = 1e-12
sim = r.simulate(0, 12, 1201, selections=['time', 'RAS', 'ppERK', 'RAFa_ppMEK', 'RASb_pRAF_d1433u_MEK'])
# sim = r.simulate(0, 12, 1201, selections=['time', 'aRtot'])
# r.plot()
# quit()
# print(11, sim['RASb_pRAF_d1433u_MEK'])

t = np.linspace(0, 12, 1201)
# print(t)
# # quit()
plt.plot(t, cubic(t), c='blue', label='RAS curve')
# plt.plot(t, sim['ppERK'], c='purple', label='RAS_out')
plt.plot(t, sim['ppERK'], c='orange', label='ERK fit')
plt.plot(t, sim['RAFa_ppMEK'], c='red', label='MEK fit')
plt.plot(t, sim['RASb_pRAF_d1433u_MEK'], c='green', label='RAFa trace')
plt.scatter(time, Rp, c='blue', label='RAS data')
plt.scatter(erk_time, erk, c='orange', label='ERK data')
plt.scatter(raf_time, raf, c='green', label='RAF data')
plt.scatter(mek_time, mek, c='red', label='MEK data')
print(sim)

# plt.plot(t, sim['aRtot'], c='red', label='aRtot fit')
# plt.scatter(egfr_time, egfr, c='red', label='aRtot data')

plt.legend()
plt.show()

# r = te.loada('RAF_activation_2022.ant')
# sim = r.simulate(0, 10, 1001, selections=['time', 'ppERK'])
# # sim = r.simulate(0, 10, 1001)
# print(sim)
# r.plot()
