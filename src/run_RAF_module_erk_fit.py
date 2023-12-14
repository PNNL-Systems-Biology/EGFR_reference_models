
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import pandas as pd
import tellurium as te


ras_datafile = 'ras.txt'

ras_df = pd.read_csv(ras_datafile, delimiter=r"\s+")
ras_time = np.array(ras_df['Time'])
ras = np.array(ras_df['tRas'])

erk_datafile = 'braf_erk_7.txt'

erk_df = pd.read_csv(erk_datafile, delimiter=r"\s+")
erk_time = np.array(erk_df['Time'])
raf = np.array(erk_df['RASb_pRAF_d1433u_MEK'])
mek = np.array(erk_df['RAFa_ppMEK'])
erk = np.array(erk_df['ppERK'])

r = te.loada('RAF_activation_2022_erk_fit.ant')
# r.integrator.absolute_tolerance = 1e-12
# r.integrator.relative_tolerance = 1e-12
sim = r.simulate(0, 12, 1201, selections=['time', 'RASb_pRAF_d1433u_MEK', 'RAFa_ppMEK', 'ppERK'])
t = np.linspace(0, 12, 1201)

# plt.plot(t, sim['RAS'], label='tRas fit')
# plt.scatter(ras_time, ras, label='tRas data')

# plt.plot(t, sim['RASb_pRAF_d1433u_MEK'], label='RAF fit')
# plt.scatter(erk_time, raf, label='RAF data')

# plt.plot(t, sim['RAFa_ppMEK'], label='MEK fit')
# plt.scatter(erk_time, mek, label='MEK data')

plt.plot(t, sim['ppERK'], label='ERK fit')
plt.scatter(erk_time, erk, label='ERK data')
plt.title('RAF module')

plt.legend()
plt.show()
