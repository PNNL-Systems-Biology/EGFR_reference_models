
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import tellurium as te


r = te.loada('comp1.ant')
# sim = r.simulate(0, 2, 201, selections=['time', 'A', 'B', 'C'])
sim = r.simulate(0, 2, 201, selections=['time', 'A'])
r.plot()


# plt.plot(t, sim['aRtot'], label='active EGFR fit')
# plt.scatter(egfr_time, egfr, label='active EGFR data')
# plt.title('EGFR module')
#
# plt.legend(loc='lower right')
# plt.show()
