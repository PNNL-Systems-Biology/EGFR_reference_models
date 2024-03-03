
import glob
import os
import pandas as pd
import math
from copy import deepcopy
import matplotlib.pyplot as plt

os.chdir("/home/michael/PycharmProjects/EGF/pybnf/output/Results/")
# os.chdir("/home/michael/PycharmProjects/EGF/pybnf/output_mh_6/Results/")
# os.chdir("/home/michael/PycharmProjects/EGF/pybnf/output_mh_8/Results/")
# os.chdir("/home/michael/PycharmProjects/EGF/pybnf/output_mh_9/Results/")
# os.chdir("/home/michael/PycharmProjects/EGF/pybnf/output_mh_9.2.1/Results/")
# os.chdir("/home/michael/PycharmProjects/EGF/pybnf/output_mh_9.2.2/Results/")
# os.chdir("/home/michael/PycharmProjects/EGF/pybnf/output_mh_9.2.3/Results/")
# os.chdir("/home/michael/PycharmProjects/EGF/pybnf/output_mh_10/Results/")
# os.chdir("/home/michael/PycharmProjects/EGF/pybnf/output_mh_6_sd_1/Results/")
# os.chdir("/home/michael/PycharmProjects/EGF/pybnf/output_mh_6_sos/Results/")
# os.chdir("/home/michael/PycharmProjects/EGF/pybnf/output_mh_m0_sd2/Results/")
# os.chdir("/home/michael/PycharmProjects/EGF/pybnf/output_mh_11.3.0/Results/")
# os.chdir("/home/michael/PycharmProjects/EGF/pybnf/output_mh_12.3/Results/")
# os.chdir("/home/michael/PycharmProjects/EGF/pybnf/")
# os.chdir("/home/michael/PycharmProjects/EGF/pybnf/output_16/Results")
# os.chdir("/home/michael/PycharmProjects/EGF/pybnf/output_chi_15/Results")

# with open('sorted_params_76.txt') as f:
with open('sorted_params_refine_final.txt') as f:
# with open('sorted_params_99.txt') as f:
# with open('LL_point_2.txt') as f:
# with open('LL_point_3.txt') as f:
# with open('LL_point_4.txt') as f:

    content = f.readlines()

params = None
values = []
for i in range(2):
    if i == 0:
        params = content[i].split()[2:]
    else:
        values.append(content[i].split()[1:])

os.chdir("/home/michael/PycharmProjects/EGF/pybnf/")


# rp_E = [0.0331, 0.0662, 0.1654, 0.4136, 0.8272, 1.6543, 3.3086, 16.543]
rp_L = [0.2, 0.4, 1.0, 2.5, 5.0, 10.0, 20.0, 100.0]
rp_L_models = []
for item in rp_L:

    with open('EGF_CM.py') as f:
        content = f.readlines()
    new_model = ''
    for i, each in enumerate(content):
        if len(each.split()) > 2 and each[:3] == 'L =':
            print(1)
            line_split = each.split()
            print(line_split)
            line_split[2] = str(item) + ';'
            content[i] = ' '.join(line_split) + '\n'
            new_model += content[i]
        elif len(each.split()) > 2 and each.split()[0] in params and each.split()[1] == '=':
            line_split = each.split()
            line_split[2] = values[0][params.index(line_split[0])] + ';'
            content[i] = ' '.join(line_split) + '\n'
            new_model += content[i]
        else:
            new_model += content[i]
    rp_L_models.append(new_model)

for i, each in enumerate(rp_L):

    f = open('EGF_CM_rp_' + str(i) + '.py', 'w')
    f.write(rp_L_models[i])


# ---------------------------------------------------------------
#
# erkp_E = [0.0165, 0.0496, 0.1654, 0.4963, 1.6543,  4.9629, 16.543]
# erkp_E_models = []
# for item in erkp_E:
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
#     erkp_E_models.append(new_model)
#
# for i, each in enumerate(erkp_E):
#
#     f = open('EGF_erk_' + str(i) + '.py', 'w')
#     f.write(erkp_E_models[i])
#
# # ---------------------------------------------------------------
#
# ras123 = [0.165, 0.165, 0.165]
# ras123_models = []
#
# for item in ras123:
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
#     ras123_models.append(new_model)
#
# for i, each in enumerate(ras123):
#
#     f = open('EGF_ras123_' + str(i) + '.py', 'w')
#     f.write(ras123_models[i])
#
#
# # -------------------------
#
# ras4 = [0.0, 0.00165, 0.005, 0.0165, 0.05, 0.5]
# ras4_models = []
#
# for item in ras4:
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
#     ras4_models.append(new_model)
#
# for i, each in enumerate(ras4):
#
#     f = open('EGF_ras4_' + str(i) + '.py', 'w')
#     f.write(ras4_models[i])
#
# # -------------------------
#
# ras5 = [0.0, 0.0165, 0.05, 0.165, 1.65, 16.5]
# ras5_models = []
#
# for item in ras5:
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
#     ras5_models.append(new_model)
#
# for i, each in enumerate(ras5):
#
#     f = open('EGF_ras5_' + str(i) + '.py', 'w')
#     f.write(ras5_models[i])
