
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import tellurium as te
import math

r = te.loada('EGFR_sequential_fit_4f.ant')


aRSK_d = [0.22, 0.76, 0.82, 7.01, 20.89, 21.66, 22.41, 20.23, 30.0]

# for val in aRSK_d:
#     print(val/14.81)
# quit()

fig, ax = plt.subplots(ncols=1, nrows=1)
for val in aRSK_d:
    r.reset()
    r.scale_parameter = val / 14.81
    # print(r.aRSK_d, r.scale_parameter)
    sim = r.simulate(0, 720, 7201, selections=['time', 'aRSK'])
    # print(sim)
    t = np.linspace(0, 720, 7201)
    ax.plot(t, sim['aRSK'], label=str(val))
    ax.legend()
plt.show()
