
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import tellurium as te

egfr_datafile = 'egfr.txt'

egfr_df = pd.read_csv(egfr_datafile, delimiter=r"\s+")
egfr_time = np.array(egfr_df['Time'])
egfr = np.array(egfr_df['aRtot'])

r = te.loada('EGFR_module.ant')
# r.integrator.absolute_tolerance = 1e-12
# r.integrator.relative_tolerance = 1e-12
sim = r.simulate(0, 12, 1201, selections=['time', 'aRtot'])
t = np.linspace(0, 12, 1201)

# print(sim)

plt.plot(t, sim['aRtot'], c='red', label='aRtot fit')
plt.scatter(egfr_time, egfr, c='red', label='aRtot data')

plt.legend()
plt.show()
