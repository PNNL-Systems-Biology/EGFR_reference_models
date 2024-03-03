
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import tellurium as te
import math

r = te.loada('EGFR_sequential_fit_4e2.ant')
sim = r.simulate(0, 720, 7201, selections=['time', 'RSK_RAS_ratio'])
print(sim)
t = np.linspace(0, 720, 7201)

fig, ax = plt.subplots(ncols=1, nrows=1)

ax.plot(t, sim['RSK_RAS_ratio'], label='rsk_ras_ratio fit')


ax.legend()

plt.show()
