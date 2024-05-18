
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import tellurium as te
import math

# r = te.loada('EGFR_sequential_fit_4e.ant')
# r = te.loada('EGFR_sequential_fit_4e2.ant')
r = te.loada('EGFR_sequential_fit_4f.ant')


dose = [0.0, 0.00495, 0.0165, 0.0495, 0.165, 0.495, 1.65, 4.95, 16.5]
aRSK = [0.22, 0.76, 0.82, 7.01, 20.89, 21.66, 22.41, 20.23, 30.0]
scale = [0.014854827819041188, 0.05131667792032411, 0.05536799459824442, 0.47332883187035785, 1.4105334233625928,
         1.462525320729237, 1.513166779203241, 1.3659689399054693, 2.025658338960162]

# for val in aRSK_d:
#     print(val/14.81)
# quit()

fig, ax = plt.subplots(ncols=1, nrows=1)
for i, val in enumerate(aRSK):
    r.reset()
    r.Lig = dose[i]
    # r.aRSK = aRSK[i]
    r.scale_parameter = scale[i]
    # print(r.aRSK_d, r.scale_parameter)
    sim = r.simulate(0, 720, 7201, selections=['time', 'Lig', 'pSOS1', 'total_SOS', 'aRSK'])
    print(sim)
    t = np.linspace(0, 720, 7201)
    # ax.plot(t, sim['total_SOS'], label='Lig=' + str(dose[i]) + ', ' + 'aRSK=' + str(val))
    ax.plot(t, sim['total_SOS'], label='Lig=' + str(dose[i]))
ax.legend(loc='lower right')
plt.axvline(x=240)
plt.title('Total mass in SOS1 cycle')
plt.show()
