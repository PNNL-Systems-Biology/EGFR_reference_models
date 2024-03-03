
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
# plt.plot(t, sim['aRtot'], label='active EGFR fit')
# plt.scatter(egfr_time, egfr, label='active EGFR data')
# plt.title('EGFR module')
fig, ax = plt.subplots(ncols=1, nrows=1, figsize=(12, 12))
# plt.figure(figsize=(12, 12))
# ax[0].plot(t, sim['aRtot'], label='ligand')
# plt.plot(t, sim['Egfr'], label='Egfr')
# plt.plot(t, sim['iEgfr'], label='iEgfr')
# ax[0].scatter(egfr_time, egfr, label='active EGFR data')
# ax[0].title.set_text('time series')

dose = [0.2, 0.4, 1.0, 2.5, 5.0, 10.0, 20.0, 100.0]
times = [10, 20, 30, 40, 50, 60, 70, 80]
response = [[1.639, 2.355, 1.899, 1.935, 1.790, 1.700, 0.781, 3.072],
            [1.943, 1.395, 1.749, 2.028, 2.039, 2.087, 1.108, 2.858],
            [2.935, 4.037, 5.768, 5.986, 7.527, 6.889, 7.812, 7.490],
            [9.543, 13.878, 18.940, 23.153, 27.694, 28.414, 34.901, 37.434],
            [13.263, 21.242, 31.053, 34.163, 37.691, 36.178, 47.017, 46.832],
            [12.110, 15.855, 28.133, 30.337, 29.640, 32.854, 31.818, 44.066],
            [18.130, 13.089, 24.388, 29.611, 36.226, 32.383, 37.782, 38.338],
            [20.861, 38.950, 38.886, 32.507, 32.372, 31.802, 30.657, 38.321]]

# dose = [2.5, 5.0, 10.0, 20.0, 100.0]
# times = [10, 20, 30, 40, 50, 60, 70, 80]
# response = [[9.543, 13.878, 18.940, 23.153, 27.694, 28.414, 34.901, 37.434],
#             [13.263, 21.242, 31.053, 34.163, 37.691, 36.178, 47.017, 46.832],
#             [12.110, 15.855, 28.133, 30.337, 29.640, 32.854, 31.818, 44.066],
#             [18.130, 13.089, 24.388, 29.611, 36.226, 32.383, 37.782, 38.338],
#             [20.861, 38.950, 38.886, 32.507, 32.372, 31.802, 30.657, 38.321]]

# dose = [0.0165, 0.165, 0.495, 1.65, 16.5]
# response = [1.659, 2.97, 13.58, 33.749, 54.0]

# dose = [0.0165, 0.495, 1.65, 16.5]
# response = [1.659, 13.58, 33.749, 54.0]

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

fit_response = []
for i in range(len(dose)):
    r.reset()
    r.Lig = dose[i]
    sim = r.simulate(0, 80, 801, selections=['time', 'pEgfr_Lig', 'Egfr', 'iEgfr'])
    # print(sim['aRtot'])
    fit_response = sim['pEgfr_Lig']
    sim_times = sim['time']
    # print(fit_response)
    color = next(ax._get_lines.prop_cycler)['color']
    ax.plot(sim_times, fit_response, color=color, label=dose[i])
    ax.scatter(times, response[i], color=color)
    # ax.title.set_text('dose response')
ax.legend()
plt.show()
