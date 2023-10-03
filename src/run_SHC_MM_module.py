
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import pandas as pd
import tellurium as te

shc_datafile = 'shc.txt'
egfr_datafile = 'egfr.txt'

# egfr_df = pd.read_csv(egfr_datafile, delimiter=r"\s+")
# egfr_time = np.array(egfr_df['Time'])
# egfr = np.array(egfr_df['aRtot'])

shc_df = pd.read_csv(shc_datafile, delimiter=r"\s+")
shc_time = np.array(shc_df['Time'])
shc = np.array(shc_df['pShc1'])

r = te.loada('SHC_MM_module.ant')
r.integrator.absolute_tolerance = 1e-12
r.integrator.relative_tolerance = 1e-12
sim = r.simulate(0, 8, 801, selections=['time', 'aRtot', 'pShc1'])
t = np.linspace(0, 8, 801)

plt.plot(t, sim['pShc1'], label='shc-complex fit')
plt.scatter(shc_time, shc, label='shc-complex data')
plt.title('SHC1 module')
# plt.plot(t, sim['aRtot'], c='red', label='egfr fit')
# plt.scatter(egfr_time, egfr, c='red', label='egfr data')
# plt.plot(t, sim['aRtot'], label='aRtot')
# plt.plot(t, sim['Shp2'], label='Shp2')
# plt.plot(t, sim['shc1'], label='shc1')
# plt.plot(t, sim['Grb2_shc1'], label='Grb2_shc1')
# plt.plot(t, sim['Grb2_shc1'], label='Grb2_shc1')

plt.legend()
plt.show()
