
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import pandas as pd
import tellurium as te

garem_datafile = 'gab.txt'

gab_df = pd.read_csv(garem_datafile, delimiter=r"\s+")
gab_time = np.array(gab_df['Time'])
gab = np.array(gab_df['aR_Grb2_ppGab1'])

r = te.loada('GAB_module_1.ant')
# r.integrator.absolute_tolerance = 1e-12
# r.integrator.relative_tolerance = 1e-12
sim = r.simulate(0, 480, 4801, selections=['time', 'pEgfr_Lig', 'aR_Grb2_ppGab1', 'aR_Grb2_ppGab1_pShp2', 'Shp2'])
t = np.linspace(0, 488, 4801)

plt.plot(t, sim['aR_Grb2_ppGab1'], label='gab-complex fit')
plt.plot(t, sim['aR_Grb2_ppGab1_pShp2'], label='gab-output')
# plt.plot(t, sim['Shp2'], label='Shp2-output')
plt.scatter(gab_time, gab, label='gab-complex data')
plt.title('GAB1 module')
# plt.plot(t, sim['aRtot'], label='aRtot')
# plt.plot(t, sim['Shp2'], label='Shp2')
# plt.plot(t, sim['Gab1'], label='Gab1')
# plt.plot(t, sim['Grb2_Gab1'], label='Grb2_Gab1')
# plt.plot(t, sim['Grb2_Gab1'], label='Grb2_Gab1')

plt.legend()
plt.show()
