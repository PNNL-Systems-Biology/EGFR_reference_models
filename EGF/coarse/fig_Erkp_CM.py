
import tellurium as te
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

fig = plt.figure()
fig.suptitle('ERK')

from EGF_CM_erk_0 import model as r0
sim = r0.simulate(0, 7200,  7201, selections=['time', 'ppErk'])
time = []
values = []
for each in sim:
    time.append(each[0])
    values.append(each[1])

data = [[], [], []]
with open('egferkpSD.exp', 'r') as f:

    content = f.readlines()
    for i, each in enumerate(content):
        if i > 0:
            data[0].append(float(each.split()[0]))
            data[1].append(float(each.split()[1]))
            data[2].append(float(each.split()[2]))

plt.subplot(2, 4, 1)
plt.plot(time, values)
plt.errorbar(data[0], data[1], yerr=data[2], capsize=10, marker='o')
plt.title('L=0.0165')
plt.xlabel('Time (s)')

# ----------------------------------------------------------------------

from EGF_CM_erk_1 import model as r1

sim = r1.simulate(0, 7200,  7201, selections=['time', 'ppErk'])
time = []
values = []
for each in sim:
    time.append(each[0])
    values.append(each[1])
print(values[-1])
data = [[], [], []]
with open('egferkpSD1.exp', 'r') as f:

    content = f.readlines()
    for i, each in enumerate(content):
        if i > 0:
            data[0].append(float(each.split()[0]))
            data[1].append(float(each.split()[1]))
            data[2].append(float(each.split()[2]))

plt.subplot(2, 4, 2)
plt.plot(time, values)
plt.errorbar(data[0], data[1], yerr=data[2], capsize=10, marker='o')
plt.title('L=0.0496')
plt.xlabel('Time (s)')

# ----------------------------------------------------------------------

from EGF_CM_erk_2 import model as r2

sim = r2.simulate(0, 7200,  7201, selections=['time', 'ppErk'])
time = []
values = []
for each in sim:
    time.append(each[0])
    values.append(each[1])
print(values[-1])
data = [[], [], []]
with open('egferkpSD2.exp', 'r') as f:

    content = f.readlines()
    for i, each in enumerate(content):
        if i > 0:
            data[0].append(float(each.split()[0]))
            data[1].append(float(each.split()[1]))
            data[2].append(float(each.split()[2]))

plt.subplot(2, 4, 3)
plt.plot(time, values)
plt.errorbar(data[0], data[1], yerr=data[2], capsize=10, marker='o')
plt.title('L=0.1654')
plt.xlabel('Time (s)')

# ----------------------------------------------------------------------

from EGF_CM_erk_3 import model as r3

sim = r3.simulate(0, 7200,  7201, selections=['time', 'ppErk'])
time = []
values = []
for each in sim:
    time.append(each[0])
    values.append(each[1])
print(values[-1])
data = [[], [], []]
with open('egferkpSD3.exp', 'r') as f:

    content = f.readlines()
    for i, each in enumerate(content):

        if i > 0:
            data[0].append(float(each.split()[0]))
            data[1].append(float(each.split()[1]))
            data[2].append(float(each.split()[2]))

plt.subplot(2, 4, 4)
plt.plot(time, values)
plt.errorbar(data[0], data[1], yerr=data[2], capsize=10, marker='o')
plt.title('L=0.4963')
plt.xlabel('Time (s)')

# ----------------------------------------------------------------------

from EGF_CM_erk_4 import model as r4

sim = r4.simulate(0, 7200,  7201, selections=['time', 'ppErk'])
time = []
values = []
for each in sim:
    time.append(each[0])
    values.append(each[1])
print(values[-1])
data = [[], [], []]
with open('egferkpSD4.exp', 'r') as f:

    content = f.readlines()
    for i, each in enumerate(content):
        if i > 0:
            data[0].append(float(each.split()[0]))
            data[1].append(float(each.split()[1]))
            data[2].append(float(each.split()[2]))

plt.subplot(2, 4, 5)
plt.plot(time, values)
plt.errorbar(data[0], data[1], yerr=data[2], capsize=10, marker='o')
plt.title('L=1.6543')
plt.xlabel('Time (s)')

# ----------------------------------------------------------------------

from EGF_CM_erk_5 import model as r5

sim = r5.simulate(0, 7200,  7201, selections=['time', 'ppErk'])
time = []
values = []
for each in sim:
    time.append(each[0])
    values.append(each[1])
print(values[-1])
data = [[], [], []]
with open('egferkpSD5.exp', 'r') as f:

    content = f.readlines()
    for i, each in enumerate(content):
        if i > 0:
            data[0].append(float(each.split()[0]))
            data[1].append(float(each.split()[1]))
            data[2].append(float(each.split()[2]))

plt.subplot(2, 4, 6)
plt.plot(time, values)
plt.errorbar(data[0], data[1], yerr=data[2], capsize=10, marker='o')
plt.title('L=4.9629')
plt.xlabel('Time (s)')

# ----------------------------------------------------------------------

from EGF_CM_erk_6 import model as r6

sim = r6.simulate(0, 7200,  7201, selections=['time', 'ppErk'])
time = []
values = []
for each in sim:
    time.append(each[0])
    values.append(each[1])
print(values[-1])
data = [[], [], []]
with open('egferkpSD6.exp', 'r') as f:
    content = f.readlines()
    for i, each in enumerate(content):
        if i > 0:
            data[0].append(float(each.split()[0]))
            data[1].append(float(each.split()[1]))
            data[2].append(float(each.split()[2]))

plt.subplot(2, 4, 7)
plt.plot(time, values)
plt.errorbar(data[0], data[1], yerr=data[2], capsize=10, marker='o')
plt.title('L=16.543')
plt.xlabel('Time (s)')

# ----------------------------------------------------------------------

# # from EGF_pt_erk_only_7 import model as r7
# # from EGF_sa_erkp_7 import model as r7
# from EGF_erkp_0 import model as r0
#
# sim = r7.simulate(0, 7200,  7201, selections=['time', 'ppErk'])
# time = []
# values = []
# for each in sim:
#     time.append(each[0])
#     values.append(each[1])
#
# data = [[], [], []]
# with open('egferkpSD7.exp', 'r') as f:
#
#     content = f.readlines()
#     for i, each in enumerate(content):
#         # print(each[:-1])
#         if i > 0:
#             data[0].append(float(each.split()[0]))
#             data[1].append(float(each.split()[1]))
#             data[2].append(float(each.split()[2]))
#
# plt.subplot(3, 4, 8)
# plt.plot(time, values)
# plt.errorbar(data[0], data[1], yerr=data[2], capsize=10, marker='o')
# plt.title('L=0.0')
#
# # ----------------------------------------------------------------------
#
# # from EGF_pt_erk_only_8 import model as r8
# # from EGF_sa_erkp_8 import model as r8
# from EGF_erkp_0 import model as r0
#
# sim = r8.simulate(0, 7200,  7201, selections=['time', 'ppErk'])
# time = []
# values = []
# for each in sim:
#     time.append(each[0])
#     values.append(each[1])
#
# data = [[], [], []]
# with open('egferkpSD8.exp', 'r') as f:
#
#     content = f.readlines()
#     for i, each in enumerate(content):
#         # print(each[:-1])
#         if i > 0:
#             data[0].append(float(each.split()[0]))
#             data[1].append(float(each.split()[1]))
#             data[2].append(float(each.split()[2]))
#
# plt.subplot(3, 4, 9)
# plt.plot(time, values)
# plt.errorbar(data[0], data[1], yerr=data[2], capsize=10, marker='o')
# plt.title('L=0.0017')
#
# # ----------------------------------------------------------------------
#
# # from EGF_pt_erk_only_9 import model as r9
# # from EGF_sa_erkp_9 import model as r9
# from EGF_erkp_0 import model as r0
#
# sim = r9.simulate(0, 7200,  7201, selections=['time', 'ppErk'])
# time = []
# values = []
# for each in sim:
#     time.append(each[0])
#     values.append(each[1])
#
# data = [[], [], []]
# with open('egferkpSD9.exp', 'r') as f:
#
#     content = f.readlines()
#     for i, each in enumerate(content):
#         # print(each[:-1])
#         if i > 0:
#             data[0].append(float(each.split()[0]))
#             data[1].append(float(each.split()[1]))
#             data[2].append(float(each.split()[2]))
#
# plt.subplot(3, 4, 10)
# plt.plot(time, values)
# plt.errorbar(data[0], data[1], yerr=data[2], capsize=10, marker='o')
# plt.title('L=0.005')
#
# # ----------------------------------------------------------------------
# plt.tight_layout()
plt.show()
