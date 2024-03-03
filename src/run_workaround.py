
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import pandas as pd
import tellurium as te

r = te.loada('workaround.ant')
sim = r.simulate(0, 10, 101, selections=['time', 'C', 'Z', 'A', 'D', 'X', 'Y'])
t = np.linspace(0, 10, 101)

plt.plot(t, sim['C'], label='C')
plt.plot(t, sim['Z'], label='Z')
plt.plot(t, sim['A'], label='A')
plt.plot(t, sim['D'], label='D')
plt.plot(t, sim['X'], label='X')
plt.plot(t, sim['Y'], label='Y')

plt.legend()
plt.show()
