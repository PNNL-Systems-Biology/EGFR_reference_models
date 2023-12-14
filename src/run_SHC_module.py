
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import pandas as pd
import tellurium as te

shc_datafile = 'shc.txt'
egfr_datafile = 'egfr_trunc.txt'
mtor_datafile = 'mTor.txt'

egfr_df = pd.read_csv(egfr_datafile, delimiter=r"\s+")
egfr_time = np.array(egfr_df['Time'])
egfr = np.array(egfr_df['aRtot'])

mtor_df = pd.read_csv(mtor_datafile, delimiter=r"\s+")
mtor_time = np.array(mtor_df['Time'])
mtor = np.array(mtor_df['mTor'])
print(mtor)

shc_df = pd.read_csv(shc_datafile, delimiter=r"\s+")
shc_time = np.array(shc_df['Time'])
shc = np.array(shc_df['pShc1'])

r = te.loada('SHC_MM_module.ant')
r.integrator.absolute_tolerance = 1e-12
r.integrator.relative_tolerance = 1e-12
sim = r.simulate(0, 8, 81, selections=['time', 'aRtot', 'mTor', 'pShc1', 'ShcTot'])
t = np.linspace(0, 8, 81)

plt.plot(t, sim['ShcTot'], c='red', label='shc-complex fit')
plt.scatter(shc_time, shc, c='red', label='shc-complex data')
# plt.plot(t, sim['aRtot'], c='blue', label='aRtot fit')
# plt.scatter(egfr_time, egfr, c='blue', label='aRtot data')
# plt.plot(t, sim['mTor'], c='green', label='mTor fit')
# plt.scatter(mtor_time, mtor, c='green', label='mTor data')
# plt.plot(t, sim['aRtot'], label='aRtot')
# plt.plot(t, sim['Shp2'], label='Shp2')
# plt.plot(t, sim['shc1'], label='shc1')
# plt.plot(t, sim['Grb2_shc1'], label='Grb2_shc1')
# plt.plot(t, sim['Grb2_shc1'], label='Grb2_shc1')

plt.legend()
plt.show()
