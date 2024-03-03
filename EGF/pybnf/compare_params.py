
import glob
import os
import pandas as pd
import math
from copy import deepcopy
import matplotlib.pyplot as plt

os.chdir("/home/michael/PycharmProjects/EGF/pybnf/output_mh_run/Results/")
# os.chdir("/home/michael/PycharmProjects/EGF/pybnf/output_pt_run/Results/")
# os.chdir("/home/michael/PycharmProjects/EGF/pybnf/output_pt_receptor_only/Results/")

with open('sorted_params_final.txt') as f:
    content = f.readlines()

params = None
values = []
for i in range(2):
    if i == 0:
        params = content[i].split()[2:]
    else:
        values.append(content[i].split()[1:])

os.chdir("/home/michael/PycharmProjects/EGF/pybnf/output_pt_ERK_only/Results/")
with open('sorted_params_final.txt') as f:
    content = f.readlines()

for i in range(2):
    if i == 0:
        pass
    else:
        values.append(content[i].split()[1:])

# print(params)
for i, each in enumerate(values):
    for j, item in enumerate(each):
        values[i][j] = float(values[i][j])
# print(values[0])
# print(values[1])

for i, each in enumerate(params):
    print(each, values[0][i], values[1][i])


quit()

# =============================================================================


os.chdir("/home/michael/PycharmProjects/EGF/pybnf/")


# rp_E = [0.2, 0.4, 1.0, 2.5, 5.0, 10.0, 20.0, 100.0]
# rp_E_models = []
# for item in rp_E:
#
#     with open('EGF.py') as f:
#         content = f.readlines()
#     new_model = ''
#     for i, each in enumerate(content):
#         if len(each.split()) > 2 and each.split()[1] == 'E' and 'var' in each:
#             line_split = each.split()
#             line_split[3] = str(item) + ';'
#             content[i] = '  ' + ' '.join(line_split) + '\n'
#             new_model += content[i]
#         elif len(each.split()) > 2 and each.split()[0] in params and each.split()[1] == '=':
#             line_split = each.split()
#             line_split[2] = values[0][params.index(line_split[0])] + ';'
#             content[i] = '  ' + ' '.join(line_split) + '\n'
#             new_model += content[i]
#         else:
#             new_model += content[i]
#     rp_E_models.append(new_model)
#
# for i, each in enumerate(rp_E):
#
#     f = open('EGF_mh_rp_' + str(i) + '.py', 'w')
#     f.write(rp_E_models[i])


# ---------------------------------------------------------------

erkp_E = [0.0, 0.0017, 0.005, 0.0165, 0.0496, 0.1654, 0.4963, 1.6543,  4.9629, 16.543]
erkp_E_models = []
for item in erkp_E:

    with open('EGF.py') as f:
        content = f.readlines()
    new_model = ''
    for i, each in enumerate(content):
        if len(each.split()) > 2 and each.split()[1] == 'E' and 'var' in each:
            line_split = each.split()
            line_split[3] = str(item) + ';'
            content[i] = '  ' + ' '.join(line_split) + '\n'
            new_model += content[i]
        elif len(each.split()) > 2 and each.split()[0] in params and each.split()[1] == '=':
            line_split = each.split()
            line_split[2] = values[0][params.index(line_split[0])] + ';'
            content[i] = '  ' + ' '.join(line_split) + '\n'
            new_model += content[i]
        else:
            new_model += content[i]
    erkp_E_models.append(new_model)

for i, each in enumerate(erkp_E):

    f = open('EGF_pt_erk_only_' + str(i) + '.py', 'w')
    f.write(erkp_E_models[i])
