
import tellurium as te
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

fig = plt.figure()
fig.suptitle('RAS')

from EGF_ras123_0 import r as r0

sim = r0.simulate(0, 600,  601, selections=['time', 'tRas'])
time = []
values = []
for each in sim:
    time.append(each[0])
    values.append(each[1])

data = [[], [], []]
with open('RasSD1.exp', 'r') as f:

    content = f.readlines()
    for i, each in enumerate(content):
        if i > 0:
            data[0].append(float(each.split()[0]))
            data[1].append(float(each.split()[1]))
            data[2].append(float(each.split()[2]))

plt.subplot(2, 3, 1)
plt.plot(time, values)
plt.errorbar(data[0], data[1], yerr=data[2], capsize=10, marker='o')
plt.xlabel('Time (s)')
plt.title('E=0.0165')

# ----------------------------------------------------------------------

from EGF_ras123_1 import r as r1

sim = r1.simulate(0, 600,  601, selections=['time', 'tRas'])
time = []
values = []
for each in sim:
    time.append(each[0])
    values.append(each[1])

data = [[], [], []]
with open('RasSD2.exp', 'r') as f:

    content = f.readlines()
    for i, each in enumerate(content):
        if i > 0:
            data[0].append(float(each.split()[0]))
            data[1].append(float(each.split()[1]))
            data[2].append(float(each.split()[2]))

plt.subplot(2, 3, 2)
plt.plot(time, values)
plt.errorbar(data[0], data[1], yerr=data[2], capsize=10, marker='o')
plt.xlabel('Time (s)')
plt.title('E=0.0165')

# ----------------------------------------------------------------------

from EGF_ras123_2 import r as r2

sim = r2.simulate(0, 600,  601, selections=['time', 'tRas'])
time = []
values = []
for each in sim:
    time.append(each[0])
    values.append(each[1])

data = [[], [], []]
with open('RasSD3.exp', 'r') as f:

    content = f.readlines()
    for i, each in enumerate(content):
        if i > 0:
            data[0].append(float(each.split()[0]))
            data[1].append(float(each.split()[1]))
            data[2].append(float(each.split()[2]))

plt.subplot(2, 3, 3)
plt.plot(time, values)
plt.errorbar(data[0], data[1], yerr=data[2], capsize=10, marker='o')
plt.xlabel('Time (s)')
plt.title('E=0.0165')

# ----------------------------------------------------------------------

from EGF_ras4_0 import r as r40
from EGF_ras4_1 import r as r41
from EGF_ras4_2 import r as r42
from EGF_ras4_3 import r as r43
from EGF_ras4_4 import r as r44
from EGF_ras4_5 import r as r45

sims = [r40, r41, r42, r43, r44, r45]
tRas = []
for each in sims:
    sim = each.simulate(0, 360, 361, selections=['time', 'tRas'])
    tRas.append(sim[-1][1])

egf = [0, 0.00165, 0.005, 0.0165, 0.05, 0.5]
data_sets = ['RasSD4.exp', 'RasSD42.exp', 'RasSD43.exp',
             'RasSD44.exp', 'RasSD45.exp', 'RasSD46.exp']
data = [[], [], []]
for each in data_sets:
    with open(each, 'r') as f:
        content = f.readlines()
        for i, item in enumerate(content):
            if i > 0:
                data[0].append(float(item.split()[0]))
                data[1].append(float(item.split()[1]))
                data[2].append(float(item.split()[2]))

plt.subplot(2, 3, 4)
plt.plot(egf, tRas)
plt.errorbar(egf, data[1], yerr=data[2], capsize=10, marker='o')
plt.xlabel('EGF (nM)')
plt.title('Time=6min')

# ----------------------------------------------------------------------

from EGF_ras5_0 import r as r50
from EGF_ras5_1 import r as r51
from EGF_ras5_2 import r as r52
from EGF_ras5_3 import r as r53
from EGF_ras5_4 import r as r54
from EGF_ras5_5 import r as r55

sims = [r50, r51, r52, r53, r54, r55]
tRas = []
for each in sims:
    sim = each.simulate(0, 360, 361, selections=['time', 'tRas'])
    tRas.append(sim[-1][1])

egf = [0, 0.0165, 0.05, 0.165, 1.65, 16.5]
data_sets = ['RasSD5.exp', 'RasSD52.exp', 'RasSD53.exp',
             'RasSD54.exp', 'RasSD55.exp', 'RasSD56.exp']
data = [[], [], []]
for each in data_sets:
    with open(each, 'r') as f:
        content = f.readlines()
        for i, item in enumerate(content):
            if i > 0:
                data[0].append(float(item.split()[0]))
                data[1].append(float(item.split()[1]))
                data[2].append(float(item.split()[2]))

plt.subplot(2, 3, 5)
plt.plot(egf, tRas)
plt.errorbar(egf, data[1], yerr=data[2], capsize=10, marker='o')
plt.xlabel('EGF (nM)')
plt.title('Time=6min')

# ----------------------------------------------------------------------
plt.tight_layout()
plt.show()
