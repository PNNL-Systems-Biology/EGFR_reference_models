
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import tellurium as te

egfr_datafile = 'egfr.txt'
egfr_df = pd.read_csv(egfr_datafile, delimiter=r"\s+")
egfr_time = np.array(egfr_df['Time'])
egfr = np.array(egfr_df['aRtot'])

garem_datafile = 'garem.txt'
garem_df = pd.read_csv(garem_datafile, delimiter=r"\s+")
garem_time = np.array(garem_df['Time'])
garem = np.array(garem_df['Grb2_ppGarem_pShp2'])

shc_datafile = 'shc.txt'
shc_df = pd.read_csv(shc_datafile, delimiter=r"\s+")
shc_time = np.array(shc_df['Time'])
shc = np.array(shc_df['pShc1'])
#
garem_datafile = 'gab.txt'
gab_df = pd.read_csv(garem_datafile, delimiter=r"\s+")
gab_time = np.array(gab_df['Time'])
gab = np.array(gab_df['Grb2_ppGab1_pShp2'])
#
ras_datafile = 'ras.txt'
ras_df = pd.read_csv(ras_datafile, delimiter=r"\s+")
ras_time = np.array(ras_df['Time'])
ras = np.array(ras_df['tRas'])

# erk_datafile = 'braf_erk_7.txt'
# erk_df = pd.read_csv(erk_datafile, delimiter=r"\s+")
# erk_time = np.array(erk_df['Time'])
# erk = np.array(erk_df['ppERK'])

r = te.loada('EGFR_combined.ant')

# sim = r.simulate(0, 8, 81)
# sim = r.simulate(0, 8, 801, ['time', 'EGFR_aRtot', 'GAREM_Grb2_ppGarem_pShp2', 'SHC_pShc1', 'GAB_Grb2_ppGab1_pShp2', 'SOS_tRas', 'RAF_ppERK'])
# sim = r.simulate(0, 8, 801, ['time', 'EGFR_aRtot', 'GAREM_Grb2_ppGarem_pShp2', 'SHC_pShc1', 'GAB_Grb2_ppGab1_pShp2', 'SOS_tRas'])
sim = r.simulate(0, 8, 801, ['time', 'aRtot', 'Grb2_ppGarem_pShp2', 'pShc1', 'Grb2_ppGab1_pShp2', 'tRas'])
t = np.linspace(0, 8, 801)
print(sim)

plt.figure(figsize=(12, 8))

plt.plot(t, sim['aRtot'], label='active EGFR fit')
plt.scatter(egfr_time, egfr, label='active EGFR data')

plt.plot(t, sim['Grb2_ppGarem_pShp2'], label='garem-complex fit')
plt.scatter(garem_time, garem, label='garem-complex data')

plt.plot(t, sim['pShc1'], label='shc-complex fit')
plt.scatter(shc_time, shc, label='shc-complex data')
#
plt.plot(t, sim['Grb2_ppGab1_pShp2'], label='gab-complex fit')
plt.scatter(gab_time, gab, label='gab-complex data')
#
plt.plot(t, sim['tRas'], label='tRas fit')
plt.scatter(ras_time, ras, label='tRas data')

# plt.plot(t, sim['RAF_ppERK'], label='ERK fit')
# plt.scatter(erk_time, erk, label='ERK data')

# plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.legend(loc='upper left')
plt.show()
# plt.savefig('egfr_combined_model')
