
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import tellurium as te


r = te.loada('comp2.ant')
sim = r.simulate(0, 12, 1201, selections=['time', 'A', 'B', 'C'])
r.plot()


# plt.plot(t, sim['aRtot'], label='active EGFR fit')
# plt.scatter(egfr_time, egfr, label='active EGFR data')
# plt.title('EGFR module')
#
# plt.legend(loc='lower right')
# plt.show()
