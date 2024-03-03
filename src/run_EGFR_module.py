
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import tellurium as te

egfr_datafile = 'egfr.txt'

egfr_df = pd.read_csv(egfr_datafile, delimiter=r"\s+")
egfr_time = np.array(egfr_df['Time'])
egfr = np.array(egfr_df['pEgfr_Lig'])

# r = te.loada('EGFR_module2.ant')
# r = te.loada('EGFR_module.ant')

# r = te.loada('EGFR_module_hsw_simplex.ant')
r = te.loada('EGFR_module_hsw.ant')
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
# r.integrator.absolute_tolerance = 1e-12
# r.integrator.relative_tolerance = 1e-12
# sim = r.simulate(0, 12, 1201, selections=['time', 'Lig', 'aRtot'])
sim = r.simulate(0, 720, 7201, selections=['time', 'pEgfr_Lig', 'Egfr', 'iEgfr'])
t = np.linspace(0, 720, 7201)

# print(r.steadyState())
# print(sim)
# quit()
plt.figure()
plt.plot(t, sim['pEgfr_Lig'], label='active EGFR fit')
plt.scatter(egfr_time, egfr, label='active EGFR data')
plt.title('EGFR module')
# fig, ax = plt.subplots(ncols=2, nrows=2, figsize=(12, 12))

# ax[0][0].plot(t, sim['pEgfr_Lig'], label='ligand')
# plt.plot(t, sim['Egfr'], label='Egfr')
# plt.plot(t, sim['iEgfr'], label='iEgfr')
# ax[0][0].scatter(egfr_time, egfr, label='active EGFR data')
# ax[0][0].title.set_text('time series')

# dose = [0.0165, 0.0495, 0.165, 0.495, 1.65, 4.95, 16.5]
# response = [1.659, 0.838, 2.97, 13.58, 33.749, 30.401, 54.0]
#
# # dose = [0.0165, 0.165, 0.495, 1.65, 16.5]
# # response = [1.659, 2.97, 13.58, 33.749, 54.0]
#
# # dose = [0.0165, 0.495, 1.65, 16.5]
# # response = [1.659, 13.58, 33.749, 54.0]
#
# t1 = np.linspace(0, 240, 2501)
# for i in range(len(dose)):
#     r.reset()
#     r.Lig = dose[i]
#     sim = r.simulate(0, 240, 2501, selections=['time', 'pEgfr_Lig', 'Egfr', 'iEgfr'])
#     ax[1][0].plot(t1, sim['pEgfr_Lig'], label=str(dose[i]))
#     ax[1][0].scatter(240, response[i])
#
# ax[1][0].title.set_text('dose response (time curves)')
# ax[1][0].legend(loc='upper center')
#
# fit_response = []
# for i in range(len(dose)):
#     r.reset()
#     r.Lig = dose[i]
#     sim = r.simulate(0, 240, 2501, selections=['time', 'pEgfr_Lig', 'Egfr', 'iEgfr'])
#     # print(sim['aRtot'])
#     fit_response.append(sim['pEgfr_Lig'][-1])
# print(fit_response)
# ax[0][1].plot(dose, fit_response, '-o')
# ax[0][1].scatter(dose, response, c='red')
# ax[0][1].title.set_text('dose response')
plt.legend()
plt.show()
