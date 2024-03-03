
import glob
import os
import pandas as pd
import math
from copy import deepcopy
import matplotlib.pyplot as plt

# os.chdir("/home/michael/PycharmProjects/EGF/pybnf/output_mh_run/Results/Histograms/")
os.chdir("/home/michael/PycharmProjects/EGF/pybnf/output_pt_ERK_only/Results/Histograms/")

hist_files = []
for filename in glob.glob("*final.txt"):
    hist_files.append(filename)

data_dict = dict()

for filename in hist_files:
    pd.set_option('display.width', 1000)
    param = filename.split('_final')[0]
    data = pd.read_csv(filename, sep='\t', skiprows=[0], header=None)
    data_dict[param] = data

min_data = 1000
max_data = -1000

for each in data_dict:
    if data_dict[each].iloc[0, 0] < min_data:
        min_data = data_dict[each].iloc[0, 0]
    if data_dict[each].iloc[-1, -2] > max_data:
        max_data = data_dict[each].iloc[-1, -2]

# print(min_data)
# print(max_data)

# quit()
max_height = 0
for each in data_dict:
    zero_pre = [math.floor(min_data), data_dict[each].iloc[0, 0], 0]
    zero_post = [data_dict[each].iloc[-1, -2], math.ceil(max_data), 0]
    df_pre = pd.DataFrame([zero_pre])
    df_post = pd.DataFrame([zero_post])
    df2 = pd.concat([df_pre, data_dict[each], df_post], ignore_index=True)
    df2[3] = df2[1]-df2[0]
    width_sum = df2.iloc[:, -1][1:11].sum()
    df2[4] = (df2[2]/data_dict[each].iloc[:, -1].sum())/df2[3]
    if df2[4].max() > max_height:
        max_height = df2[4].max()
    data_dict[each] = deepcopy(df2)

# print(max_height)

for each in data_dict:

    print(each)
    plt.bar(data_dict[each][0], data_dict[each][4], width=data_dict[each][3])
    plt.title(each)
    plt.ylim((0, 6))
    plt.xticks(range(-10, 11))
    plt.xlim((-10, 11.4))
    plt.xlabel('log10 parameter values')
    plt.savefig(each + '.png')
    plt.clf()
