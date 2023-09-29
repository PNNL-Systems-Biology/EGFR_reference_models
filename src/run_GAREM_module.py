
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import pandas as pd
import tellurium as te

garem_datafile = 'garem.txt'

garem_df = pd.read_csv(garem_datafile, delimiter=r"\s+")
garem_time = np.array(garem_df['Time'])
garem = np.array(garem_df['Grb2_ppGarem_pShp2'])

r = te.loada('current_model.ant')
# r.integrator.absolute_tolerance = 1e-12
# r.integrator.relative_tolerance = 1e-12
sim = r.simulate(0, 8, 801, selections=['time', 'aRtot', 'Shp2', 'Grb2_ppGarem_pShp2'])
t = np.linspace(0, 8, 801)

plt.plot(t, sim['Grb2_ppGarem_pShp2'], c='red', label='garem-complex fit')
plt.scatter(garem_time, garem, c='red', label='garem-complex data')

plt.legend()
plt.show()
