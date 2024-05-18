
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import tellurium as te
import math


r = te.loada('EGFR_sequential_fit_4e2.ant')
sim = r.simulate(0, 720, 7201, selections=['time', 'aR_Grb2_ppGarem_pShp2', 'aR_Grb2_ppGab1_pShp2',
                                           'aR_pShc1', 'aR_Grb2_ppGarem_pShp2', 'Grb2_SOS1', 'aR_Grb2_ppGab1_pShp2', 'Gab1', 'Grb2', 'pEgfr_Lig', 'aR_Grb2_Gab1', 'Grb2_Gab1', 'aR_pShc1', 'Ad1_Grb2_SOS1', 'Ad2_Grb2_SOS1', 'Ad3_Grb2_SOS1'])
print(sim['Gab1'])
Time = sim['time']

Garem = sim['Gab1']
Gab = sim['Grb2']
Shc1 = sim['Grb2_Gab1']

Garem1 = sim['Ad1_Grb2_SOS1']
Gab1 = sim['Ad2_Grb2_SOS1']
Shc11 = sim['Ad3_Grb2_SOS1']

Garem2 = sim['aR_Grb2_ppGarem_pShp2']
Gab2 = sim['aR_Grb2_ppGab1_pShp2']
Shc12 = sim['aR_pShc1']


fig, ax = plt.subplots(ncols=2, nrows=2,  figsize=(12, 8))

# ax[0, 0].plot(Time, Garem, label='Garem')
# ax[0, 1].plot(Time, Gab, label='Gab')
# ax[1, 0].plot(Time, Shc1, label='Shc')

# ax[0, 0].plot(Time, Garem2, label='Garem')
# ax[0, 1].plot(Time, Gab2, label='Gab')
# ax[1, 0].plot(Time, Shc12, label='Shc')

ax[0, 0].plot(Time, Garem1, label='aR_Grb2_ppGarem_pShp2')
ax[0, 1].plot(Time, Gab1, label='Ad2_Grb2_SOS1')
ax[1, 0].plot(Time, Shc11, label='Ad3_Grb2_SOS1')

ax[0, 0].legend()
ax[0, 1].legend()
ax[1, 0].legend()
plt.show()

