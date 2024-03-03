
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import tellurium as te
import math

# egfr_datafile = 'egfr.txt'
# 
# egfr_df = pd.read_csv(egfr_datafile, delimiter=r"\s+")
# egfr_time = np.array(egfr_df['Time'])
# egfr = np.array(egfr_df['aRtot'])

l2_datafile = 'level2a_.txt'

l2_df = pd.read_csv(l2_datafile, delimiter=r"\s+")
l2_time = np.array(l2_df['Time'])
# garem_fit = np.array(l2_df['aR_Grb2_ppGarem'])
garem_out = np.array(l2_df['aR_Grb2_ppGarem_pShp2'])
# gab_fit = np.array(l2_df['aR_Grb2_ppGab1'])
gab_out = np.array(l2_df['aR_Grb2_ppGab1_pShp2'])
shc = np.array(l2_df['aR_pShc1'])

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
# r = te.loada('EGFR_sequential_fit_egfr.ant')
r = te.loada('EGFR_sequential_fit_2.ant')

# r.integrator.absolute_tolerance = 1e-12
# r.integrator.relative_tolerance = 1e-12
# sim = r.simulate(0, 720, 7201, selections=['time', 'pEgfr_Lig', 'ipEgfr_Lig'])
sim = r.simulate(0, 720, 7201, selections=['time', 'aR_Grb2_ppGarem', 'aR_Grb2_ppGarem_pShp2', 'aR_Grb2_ppGab1',
                                           'aR_Grb2_ppGab1_pShp2', 'aR_pShc1'])

# r.plot()
# quit()
# print(sim)
t = np.linspace(0, 720, 7201)

# print(r.steadyState())
# print(sim)
# quit()
# plt.plot(t, sim['aRtot'], label='active EGFR fit')
# plt.scatter(egfr_time, egfr, label='active EGFR data')
# plt.title('EGFR module')

fig, ax = plt.subplots(ncols=2, nrows=2, figsize=(16, 12))

# ax[0, 0].plot(t, sim['aR_Grb2_ppGarem'], label='Garem fit')
# ax[0, 0].scatter(l2_time, garem_fit, label='Garem fit data')

ax[0, 0].plot(t, sim['aR_Grb2_ppGarem_pShp2'], label='Garem out')
ax[0, 0].scatter(l2_time, garem_out, label='Garem out data')

# ax[1, 0].plot(t, sim['aR_Grb2_ppGab1'], label='Gab fit')
# ax[1, 0].scatter(l2_time, gab_fit, label='Gab fit data')

ax[0, 1].plot(t, sim['aR_Grb2_ppGab1_pShp2'], label='Gab out')
ax[0, 1].scatter(l2_time, gab_out, label='Gab out data')

ax[1, 0].plot(t, sim['aR_pShc1'], label='Shc')
ax[1, 0].scatter(l2_time, shc, label='Shc data data')

# ax[0, 0].title.set_text('time series')
ax[0, 0].legend()
ax[1, 0].legend()
ax[0, 1].legend()
# ax[1, 1].legend()
# ax[2, 0].legend()

# plt.plot(t, sim['aR_Grb2_ppGarem'], label='Garem fit')
# plt.scatter(l2_time, garem_fit, label='Garem fit data')
#
# plt.plot(t, sim['aR_Grb2_ppGarem_pShp2'], label='Garem out')
# plt.scatter(l2_time, garem_out, label='Garem out data')
#
# plt.plot(t, sim['aR_Grb2_ppGab1'], label='Gab fit')
# plt.scatter(l2_time, gab_fit, label='Gab fit data')
#
# plt.plot(t, sim['aR_Grb2_ppGab1_pShp2'], label='Gab out')
# plt.scatter(l2_time, gab_out, label='Gab out data')
#
# plt.plot(t, sim['aR_pShc1'], label='Shc')
# plt.scatter(l2_time, shc, label='Shc data data')
#
# plt.title('time series')
# plt.legend()

# dose = [0.0, 0.00495, 0.0165, 0.0495, 0.165, 0.495, 1.65, 4.95, 16.5]
# times = [240]
# response1 = [[0.22], [0.28], [0.31], [0.33], [0.41], [0.52], [0.47], [0.47], [0.48]]
# response2 = [[0.51], [0.65], [0.72], [0.78], [0.95], [1.2], [1.1], [1.11], [1.13]]
# response3 = [[0.18], [0.19], [0.19], [0.29], [0.42], [0.51], [0.5], [0.46], [0.48]]
# response4 = [[0.41], [0.45], [0.45], [0.68], [0.98], [1.19], [1.17], [1.07], [1.11]]
# response5 = [[1.69], [1.76], [2.15], [2.53], [3.85], [6.01], [6.3], [5.92], [6.11]]
#
# fit_response = []
# fit240 = []
# for i in range(len(dose)):
#     r.reset()
#     r.Lig = dose[i]
#     sim = r.simulate(0, 720, 7201, selections=['time', 'aR_Grb2_ppGarem', 'aR_Grb2_ppGarem_pShp2', 'aR_Grb2_ppGab1',
#                                                'aR_Grb2_ppGab1_pShp2', 'aR_pShc1'])
#     fit240.append(sim[2400][1])
#     # print(sim['aRtot'])
#     fit_response1 = sim['aR_Grb2_ppGarem']
#     fit_response2 = sim['aR_Grb2_ppGarem_pShp2']
#     fit_response3 = sim['aR_Grb2_ppGab1']
#     fit_response4 = sim['aR_Grb2_ppGab1_pShp2']
#     fit_response5 = sim['aR_pShc1']
#     sim_times = sim['time']
#     # print(fit_response)
#     color = next(ax[1, 0]._get_lines.prop_cycler)['color']
#     ax[1, 0].plot(sim_times, fit_response1, color=color, label=dose[i])
#     ax[1, 0].scatter(times, response1[i], color=color)
#
#     ax[1, 0].plot(sim_times, fit_response2, color=color, label=dose[i])
#     ax[1, 0].scatter(times, response2[i], color=color)
#
#     ax[1, 0].plot(sim_times, fit_response3, color=color, label=dose[i])
#     ax[1, 0].scatter(times, response3[i], color=color)
#
#     ax[1, 0].plot(sim_times, fit_response4, color=color, label=dose[i])
#     ax[1, 0].scatter(times, response4[i], color=color)
#
#     ax[1, 0].plot(sim_times, fit_response5, color=color, label=dose[i])
#     ax[1, 0].scatter(times, response5[i], color=color)
#
#     ax[1, 0].title.set_text('dose response (time series)')
# # ax[1, 0].legend()

plt.show()
quit()

dose1 = [0.0, 0.00495, 0.0165, 0.0495, 0.165, 0.495, 1.65, 4.95, 16.5]
response1 = [0.22, 0.28, 0.31, 0.33, 0.41, 0.52, 0.47, 0.47, 0.48]
response2 = [0.51, 0.65, 0.72, 0.78, 0.95, 1.2, 1.1, 1.11, 1.13]
response3 = [0.18, 0.19, 0.19, 0.29, 0.42, 0.51, 0.50, 0.46, 0.48]
response4 = [0.41, 0.45, 0.45, 0.68, 0.98, 1.19, 1.17, 1.07, 1.11]
response5 = [1.69, 1.76, 2.15, 2.53, 3.85, 6.01, 6.3, 5.92, 6.11]

fit1 = []
fit2 = []
fit3 = []
fit4 = []
fit5 = []

print(fit240)
ax[0, 1].set_xscale('log')
ax[0, 1].scatter(dose1, response1)
ax[0, 1].scatter(dose1, fit240)
# t1 = np.linspace(0, 240, 2501)
# for i in range(len(dose)):
#     r.reset()
#     r.Lig = dose[i]
#     sim = r.simulate(0, 240, 2501, selections=['time', 'aRtot', 'Egfr', 'iEgfr'])
#     ax[1][0].plot(t1, sim['aRtot'], label=str(dose[i]))
#     ax[1][0].scatter(240, response[i])
#
# ax[1][0].title.set_text('dose response (time curves)')
# ax[1][0].legend(loc='upper center')
ax[0, 1].title.set_text('dose response')

plt.show()
