
import tellurium as te
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

fig = plt.figure()
fig.suptitle('Receptor')

from EGF_rp_0 import r as r0

sim = r0.simulate(0, 80, 81, selections=['time', 'Rp'])
time = []
values = []
for each in sim:
    time.append(each[0])
    values.append(each[1])

data = [[], [], []]
with open('egfrpSD.exp', 'r') as f:

    content = f.readlines()
    for i, each in enumerate(content):
        if i > 0:
            data[0].append(float(each.split()[0]))
            data[1].append(float(each.split()[1]))
            data[2].append(float(each.split()[2]))

plt.subplot(2, 4, 1)
plt.plot(time, values)
plt.errorbar(data[0], data[1], yerr=data[2], capsize=10, marker='o')
plt.title('E=0.2')
plt.xlabel('Time (s)')


# ----------------------------------------------------------------------

from EGF_rp_1 import r as r1

sim = r1.simulate(0, 80, 81, selections=['time', 'Rp'])
time = []
values = []
for each in sim:
    time.append(each[0])
    values.append(each[1])

data = [[], [], []]
with open('egfrpSD1.exp', 'r') as f:

    content = f.readlines()
    for i, each in enumerate(content):
        if i > 0:
            data[0].append(float(each.split()[0]))
            data[1].append(float(each.split()[1]))
            data[2].append(float(each.split()[2]))

plt.subplot(2, 4, 2)
plt.plot(time, values)
plt.errorbar(data[0], data[1], yerr=data[2], capsize=10, marker='o')
plt.title('E=0.4')
plt.xlabel('Time (s)')

# ----------------------------------------------------------------------

from EGF_rp_2 import r as r2

sim = r2.simulate(0, 80, 81, selections=['time', 'Rp'])
time = []
values = []
for each in sim:
    time.append(each[0])
    values.append(each[1])

data = [[], [], []]
with open('egfrpSD2.exp', 'r') as f:

    content = f.readlines()
    for i, each in enumerate(content):
        if i > 0:
            data[0].append(float(each.split()[0]))
            data[1].append(float(each.split()[1]))
            data[2].append(float(each.split()[2]))

plt.subplot(2, 4, 3)
plt.plot(time, values)
plt.errorbar(data[0], data[1], yerr=data[2], capsize=10, marker='o')
plt.title('E=1.0')
plt.xlabel('Time (s)')

# ----------------------------------------------------------------------

from EGF_rp_3 import r as r3

sim = r3.simulate(0, 80, 81, selections=['time', 'Rp'])
time = []
values = []
for each in sim:
    time.append(each[0])
    values.append(each[1])

data = [[], [], []]
with open('egfrpSD3.exp', 'r') as f:

    content = f.readlines()
    for i, each in enumerate(content):

        if i > 0:
            data[0].append(float(each.split()[0]))
            data[1].append(float(each.split()[1]))
            data[2].append(float(each.split()[2]))

plt.subplot(2, 4, 4)
plt.plot(time, values)
plt.errorbar(data[0], data[1], yerr=data[2], capsize=10, marker='o')
plt.title('E=2.5')
plt.xlabel('Time (s)')

# ----------------------------------------------------------------------

from EGF_rp_4 import r as r4

sim = r4.simulate(0, 80, 81, selections=['time', 'Rp'])
time = []
values = []
for each in sim:
    time.append(each[0])
    values.append(each[1])

data = [[], [], []]
with open('egfrpSD4.exp', 'r') as f:

    content = f.readlines()
    for i, each in enumerate(content):
        if i > 0:
            data[0].append(float(each.split()[0]))
            data[1].append(float(each.split()[1]))
            data[2].append(float(each.split()[2]))

plt.subplot(2, 4, 5)
plt.plot(time, values)
plt.errorbar(data[0], data[1], yerr=data[2], capsize=10, marker='o')
plt.title('E=5.0')
plt.xlabel('Time (s)')

# ----------------------------------------------------------------------

from EGF_rp_5 import r as r5
#
sim = r5.simulate(0, 80, 81, selections=['time', 'Rp'])
time = []
values = []
for each in sim:
    time.append(each[0])
    values.append(each[1])

data = [[], [], []]
with open('egfrpSD5.exp', 'r') as f:

    content = f.readlines()
    for i, each in enumerate(content):
        if i > 0:
            data[0].append(float(each.split()[0]))
            data[1].append(float(each.split()[1]))
            data[2].append(float(each.split()[2]))

plt.subplot(2, 4, 6)
plt.plot(time, values)
plt.errorbar(data[0], data[1], yerr=data[2], capsize=10, marker='o')
plt.title('E=10.0')
plt.xlabel('Time (s)')

# ----------------------------------------------------------------------

from EGF_rp_6 import r as r6

sim = r6.simulate(0, 80, 81, selections=['time', 'Rp'])
time = []
values = []
for each in sim:
    time.append(each[0])
    values.append(each[1])

data = [[], [], []]
with open('egfrpSD6.exp', 'r') as f:
    content = f.readlines()
    for i, each in enumerate(content):
        if i > 0:
            data[0].append(float(each.split()[0]))
            data[1].append(float(each.split()[1]))
            data[2].append(float(each.split()[2]))

plt.subplot(2, 4, 7)
plt.plot(time, values)
plt.errorbar(data[0], data[1], yerr=data[2], capsize=10, marker='o')
plt.title('E=20.0')
plt.xlabel('Time (s)')

# ----------------------------------------------------------------------

from EGF_rp_7 import r as r7

sim = r7.simulate(0, 80, 81, selections=['time', 'Rp'])
time = []
values = []
for each in sim:
    time.append(each[0])
    values.append(each[1])

data = [[], [], []]
with open('egfrpSD7.exp', 'r') as f:

    content = f.readlines()
    for i, each in enumerate(content):
        if i > 0:
            data[0].append(float(each.split()[0]))
            data[1].append(float(each.split()[1]))
            data[2].append(float(each.split()[2]))

plt.subplot(2, 4, 8)
plt.plot(time, values)
plt.errorbar(data[0], data[1], yerr=data[2], capsize=10, marker='o')
plt.title('E=100.0')
plt.xlabel('Time (s)')

# ----------------------------------------------------------------------

plt.show()