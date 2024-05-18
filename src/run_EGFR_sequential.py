
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
# r = te.loada('EGFR_sequential_fit_egfr.ant')
# r = te.loada('EGFR_sequential_fit_full.ant')
# r = te.loada('EGFR_1_4.ant')
# r = te.loada('EGFR_4_HSW.ant')
r = te.loada('EGFR_sequential_fit_4_HSW_0.ant')

# r.integrator.absolute_tolerance = 1e-12
# r.integrator.relative_tolerance = 1e-12
# sim = r.simulate(0, 12, 1201, selections=['time', 'Lig', 'aRtot'])
# sim = r.simulate(0, 720, 7201, selections=['time', 'aRtot', 'pEGFRtot', 'pEgfr_Lig', 'ipEgfr_Lig'])
sim = r.simulate(0, 720, 7201, selections=['time', 'aRtot', 'pEgfr_Lig', 'ipEgfr_Lig'])
t = np.linspace(0, 720, 7201)
r.plot()
print(sim)
quit()
# print(r.steadyState())
# print(sim)
# quit()
# plt.plot(t, sim['aRtot'], label='active EGFR fit')
# plt.scatter(egfr_time, egfr, label='active EGFR data')
# plt.title('EGFR module')
fig, ax = plt.subplots(ncols=2, nrows=2, figsize=(16, 12))
# plt.figure(figsize=(12, 12))
ax[0, 0].plot(t, sim['aRtot'], label='ligand')
# plt.plot(t, sim['Egfr'], label='Egfr')
# plt.plot(t, sim['iEgfr'], label='iEgfr')
ax[0, 0].scatter(egfr_time, egfr, label='active EGFR data')
ax[0, 0].title.set_text('time series')

dose = [0.0, 0.00495, 0.0165, 0.0495, 0.165, 0.495, 1.65, 4.95, 16.5]
times = [240]
response = [[1.14],
            [0.01],
            [2.91],
            [3.22],
            [10.41],
            [19.8],
            [25.91],
            [24.81],
            [33.14]]

fit_response = []
fit240 = []
for i in range(len(dose)):
    r.reset()
    r.Lig = dose[i]
    sim = r.simulate(0, 720, 7201, selections=['time', 'aRtot'])
    fit240.append(sim[2400][1])
    # print(sim['aRtot'])
    fit_response = sim['aRtot']
    sim_times = sim['time']
    # print(fit_response)
    color = next(ax[1, 0]._get_lines.prop_cycler)['color']
    ax[1, 0].plot(sim_times, fit_response, color=color, label=dose[i])
    ax[1, 0].scatter(times, response[i], color=color)
    ax[1, 0].title.set_text('dose response (time series)')
ax[1, 0].legend()

dose1 = [0.0, 0.00495, 0.0165, 0.0495, 0.165, 0.495, 1.65, 4.95, 16.5]
response1 = [1.14, 0.01, 2.91, 3.22, 10.41, 19.8, 25.91, 24.81, 33.14]
for each in fit240:
    print(each)
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
