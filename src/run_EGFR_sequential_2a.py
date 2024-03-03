
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

l2_datafile = 'level2_.txt'

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
# sim = r.simulate(0, 12, 1201, selections=['time', 'Lig', 'aRtot'])
# sim = r.simulate(0, 720, 7201, selections=['time', 'aR_Grb2_ppGarem', 'aR_Grb2_ppGarem_pShp2', 'aR_Grb2_ppGab1',
#                                            'aR_Grb2_ppGab1_pShp2', 'aR_pShc1'])
# print(sim)
# t = np.linspace(0, 720, 7201)

# print(r.steadyState())
# print(sim)
# quit()
# plt.plot(t, sim['aRtot'], label='active EGFR fit')
# plt.scatter(egfr_time, egfr, label='active EGFR data')
# plt.title('EGFR module')

# fig, ax = plt.subplots(ncols=2, nrows=3, figsize=(16, 12))
#
# ax[0, 0].plot(t, sim['aR_Grb2_ppGarem'], label='Garem fit')
# ax[0, 0].scatter(l2_time, garem_fit, label='Garem fit data')
#
# ax[0, 1].plot(t, sim['aR_Grb2_ppGarem_pShp2'], label='Garem out')
# ax[0, 1].scatter(l2_time, garem_out, label='Garem out data')
#
# ax[1, 0].plot(t, sim['aR_Grb2_ppGab1'], label='Gab fit')
# ax[1, 0].scatter(l2_time, gab_fit, label='Gab fit data')
#
# ax[1, 1].plot(t, sim['aR_Grb2_ppGab1_pShp2'], label='Gab out')
# ax[1, 1].scatter(l2_time, gab_out, label='Gab out data')
#
# ax[2, 0].plot(t, sim['aR_pShc1'], label='Shc')
# ax[2, 0].scatter(l2_time, shc, label='Shc data data')
#
# # ax[0, 0].title.set_text('time series')
# ax[0, 0].legend()
# ax[1, 0].legend()
# ax[0, 1].legend()
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

fig, ax = plt.subplots(ncols=2, nrows=2, figsize=(16, 12))


dose = [0.0, 0.00495, 0.0165, 0.0495, 0.165, 0.495, 1.65, 4.95, 16.5]
times = [240]
# response1 = [[0.22], [0.28], [0.31], [0.33], [0.41], [0.52], [0.47], [0.47], [0.48]]
# response2 = [[0.51], [0.65], [0.72], [0.78], [0.95], [1.2], [1.1], [1.11], [1.13]]
# response3 = [[0.18], [0.19], [0.19], [0.29], [0.42], [0.51], [0.5], [0.46], [0.48]]
# response4 = [[0.41], [0.45], [0.45], [0.68], [0.98], [1.19], [1.17], [1.07], [1.11]]
# response5 = [[1.69], [1.76], [2.15], [2.53], [3.85], [6.01], [6.3], [5.92], [6.11]]

# # response1 = [0.22, 0.28, 0.31, 0.33, 0.41, 0.52, 0.47, 0.47, 0.48]
# response2 = [0.51, 0.65, 0.72, 0.78, 0.95, 1.2, 1.1, 1.11, 1.13]
# # response3 = [0.18, 0.19, 0.19, 0.29, 0.42, 0.51, 0.50, 0.46, 0.48]
# response4 = [0.41, 0.45, 0.45, 0.68, 0.98, 1.19, 1.17, 1.07, 1.11]
# response5 = [1.69, 1.76, 2.15, 2.53, 3.85, 6.01, 6.3, 5.92, 6.11]

# response2 = [0.726, 0.925, 1.027, 1.11, 1.361, 1.72, 1.567, 1.581, 1.612]
# response4 = [0.59, 0.65, 0.64, 0.97, 1.4, 1.7, 1.68, 1.53, 1.59]
# response5 = [1.69, 1.76, 2.15, 2.53, 3.85, 6.01, 6.3, 5.92, 6.11]

response2 = [0.22, 0.52, 0.67, 0.8, 1.18, 1.72, 1.49, 1.51, 1.56]
response4 = [0.0, 0.06, 0.05, 0.56, 1.23, 1.7, 1.66, 1.43, 1.53]
response5 = [0.0, 0.13, 0.66, 1.18, 2.97, 5.91, 6.3, 5.78, 6.05]

fit_response1 = []
fit_response2 = []
fit_response3 = []
fit_response4 = []
fit_response5 = []

fit_response = []
fit240 = []
for i in range(len(dose)):
    r.reset()
    r.Lig = dose[i]
    sim = r.simulate(0, 720, 7201, selections=['time', 'aR_Grb2_ppGarem', 'aR_Grb2_ppGarem_pShp2', 'aR_Grb2_ppGab1',
                                               'aR_Grb2_ppGab1_pShp2', 'aR_pShc1'])
#     fit240.append(sim[2400][1])
    print(sim['time'][2400])
#     fit_response1.append(sim['aR_Grb2_ppGarem'][2400])
    fit_response2.append(sim['aR_Grb2_ppGarem_pShp2'][2400])
    # fit_response3.append(sim['aR_Grb2_ppGab1'][2400])
    fit_response4.append(sim['aR_Grb2_ppGab1_pShp2'][2400])
    fit_response5.append(sim['aR_pShc1'][2400])
    # sim_times = sim['time']
print(fit_response2)
# color = next(ax[1, 0]._get_lines.prop_cycler)['color']

# ax[0, 0].set_xscale('log')
# ax[0, 0].scatter(dose, response1)
# ax[0, 0].scatter(dose, fit_response1)
# ax[0, 0].title.set_text('Garem fit')

ax[0, 0].set_xscale('log')
ax[0, 0].scatter(dose, response2, label='data')
ax[0, 0].scatter(dose, fit_response2, label='fit')
ax[0, 0].title.set_text('Garem out')

# ax[1, 0].set_xscale('log')
# ax[1, 0].scatter(dose, response3)
# ax[1, 0].scatter(dose, fit_response3)
# ax[1, 0].title.set_text('Gab fit')

ax[0, 1].set_xscale('log')
ax[0, 1].scatter(dose, response4, label='data')
ax[0, 1].scatter(dose, fit_response4, label='fit')
ax[0, 1].title.set_text('Gab out')

ax[1, 0].set_xscale('log')
ax[1, 0].scatter(dose, response5, label='data')
ax[1, 0].scatter(dose, fit_response5, label='fit')
ax[1, 0].title.set_text('Shc')
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

ax[0, 0].legend()
ax[0, 1].legend()
ax[1, 0].legend()

plt.show()
quit()

# dose1 = [0.0, 0.00495, 0.0165, 0.0495, 0.165, 0.495, 1.65, 4.95, 16.5]
# response1 = [0.22, 0.28, 0.31, 0.33, 0.41, 0.52, 0.47, 0.47, 0.48]
# response2 = [0.51, 0.65, 0.72, 0.78, 0.95, 1.2, 1.1, 1.11, 1.13]
# response3 = [0.18, 0.19, 0.19, 0.29, 0.42, 0.51, 0.50, 0.46, 0.48]
# response4 = [0.41, 0.45, 0.45, 0.68, 0.98, 1.19, 1.17, 1.07, 1.11]
# response5 = [1.69, 1.76, 2.15, 2.53, 3.85, 6.01, 6.3, 5.92, 6.11]
#
# fit1 = []
# fit2 = []
# fit3 = []
# fit4 = []
# fit5 = []

# print(fit240)
# ax[0, 1].set_xscale('log')
# ax[0, 1].scatter(dose1, response1)
# ax[0, 1].scatter(dose1, fit240)
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
