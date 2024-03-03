
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import pandas as pd
import tellurium as te

garem_datafile = 'garem.txt'

garem_df = pd.read_csv(garem_datafile, delimiter=r"\s+")
garem_time = np.array(garem_df['Time'])
garem = np.array(garem_df['aR_Grb2_ppGarem'])

r = te.loada('GAREM_module_1.ant')
# r.integrator.absolute_tolerance = 1e-12
# r.integrator.relative_tolerance = 1e-12
sim = r.simulate(0, 480, 4801, selections=['time', 'Shp2', 'pEgfr_Lig', 'aR_Grb2_ppGarem', 'aR_Grb2_ppGarem_pShp2'])
t = np.linspace(0, 480, 4801)

# plt.plot(t, sim['pEgfr_Lig'], label='pEgfr_Lig fit')
plt.plot(t, sim['aR_Grb2_ppGarem'], label='garem-complex fit')
plt.plot(t, sim['aR_Grb2_ppGarem_pShp2'], label='garem-output fit')
plt.scatter(garem_time, garem, label='garem-complex data')
plt.title('GAREM module')

plt.legend()
plt.show()
