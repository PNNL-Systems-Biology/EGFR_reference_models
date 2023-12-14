
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import pandas as pd
import tellurium as te

# sos_input_datafile = 'sos_input.txt'

# sos_input_df = pd.read_csv(sos_input_datafile, delimiter=r"\s+")
# sos_input_time = np.array(sos_input_df['Time'])
# sos_input = np.array(sos_input_df['aAdptrTot'])

ras_datafile = 'ras.txt'

ras_df = pd.read_csv(ras_datafile, delimiter=r"\s+")
ras_time = np.array(ras_df['Time'])
ras = np.array(ras_df['tRas'])

r = te.loada('SOS_module2.ant')
# r.integrator.absolute_tolerance = 1e-12
# r.integrator.relative_tolerance = 1e-12
sim = r.simulate(0, 10, 1201, selections=['time', 'aAdptrTot', 'Grb2_pSOS1', 'Grb2_ipSOS1', 'aSOS', 'dRas', 'tRas'])
t = np.linspace(0, 10, 1201)

plt.plot(t, sim['tRas'], label='tRas fit')
plt.scatter(ras_time, ras, label='tRas data')
# plt.plot(t, sim['aAdptrTot'], label='agg input fit')
# plt.scatter(sos_input_time, sos_input, label='agg input data')
# plt.plot(t, sim['aRtot'], label='aRtot')
# plt.plot(t, sim['Shp2'], label='Shp2')
# plt.plot(t, sim['Gab1'], label='Gab1')
# plt.plot(t, sim['Grb2_Gab1'], label='Grb2_Gab1')
# plt.plot(t, sim['Grb2_Gab1'], label='Grb2_Gab1')
plt.title('SOS module')

plt.legend()
plt.show()
