
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import tellurium as te
import math

egfr_datafile = 'egfr.txt'

egfr_df = pd.read_csv(egfr_datafile, delimiter=r"\s+")
egfr_time = np.array(egfr_df['Time'])
egfr = np.array(egfr_df['aRtot'])

# r = te.loada('EGFR_module2.ant')
# r = te.loada('EGFR_module.ant')
# r = te.loada('EGFR_module_hsw_simplex.ant')
# r = te.loada('EGFR_module_hsw.ant')
# r = te.loada('EGFR_module_hsw_0.ant')
# r = te.loada('EGFR_module_hsw_1.ant')
# r = te.loada('EGFR_module_hsw_2.ant')
# r = te.loada('EGFR_module_hsw_3.ant')
# r = te.loada('EGFR_module_hsw_4.ant')
# r = te.loada('EGFR_module_hsw_5.ant')
# r = te.loada('EGFR_module_hsw_6.ant')
# r = te.loada('EGFR_module_hsw_best.ant')
# r = te.loada('EGFR_module_hsw_simplex_oiv_kin_dose.ant')
# r = te.loada('EGFR_module_hsw_simplex_niv_kin_dose.ant')
# r = te.loada('EGFR_module_hsw_de_2fold_oiv_kin_dose.ant')
# r = te.loada('EGFR_module_hsw_nocomp.ant')
r = te.loada('EGFR_sequential_fit_egfr.ant')

# r.integrator.absolute_tolerance = 1e-12
# r.integrator.relative_tolerance = 1e-12
# sim = r.simulate(0, 12, 1201, selections=['time', 'Lig', 'aRtot'])
sim = r.simulate(0, 720, 7201, selections=['time', 'aRtot', 'pEgfr_Lig', 'ipEgfr_Lig'])
t = np.linspace(0, 720, 7201)

# print(r.steadyState())
# print(sim)
# quit()
# plt.plot(t, sim['aRtot'], label='active EGFR fit')
# plt.scatter(egfr_time, egfr, label='active EGFR data')
# plt.title('EGFR module')
fig, ax = plt.subplots(ncols=1, nrows=1)
# plt.figure(figsize=(12, 12))
ax.plot(t, sim['aRtot'], label='ligand')
ax.plot(t, sim['pEgfr_Lig'], label='pEgfr_Lig')
ax.plot(t, sim['ipEgfr_Lig'], label='ipEgfr_Lig')
# plt.plot(t, sim['Egfr'], label='Egfr')
# plt.plot(t, sim['iEgfr'], label='iEgfr')
ax.scatter(egfr_time, egfr, label='active EGFR data')
ax.title.set_text('time series')
plt.legend()
plt.show()
