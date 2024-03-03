
import glob
import os
import pandas as pd
import math
import matplotlib.pyplot as plt

os.chdir("/home/michael/PycharmProjects/EGF/pybnf/output_mh_run/Results/Histograms/")

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


for each in data_dict:
    print()
    print(each)
    zero_pre = [math.floor(min_data), data_dict[each].iloc[0, 0], 0]
    zero_post = [data_dict[each].iloc[-1, -2], math.ceil(max_data), 0]
    df_pre = pd.DataFrame([zero_pre])
    df_post = pd.DataFrame([zero_post])
    df2 = pd.concat([df_pre, data_dict[each], df_post], ignore_index=True)
    df2[3] = df2[1]-df2[0]
    width_sum = df2.iloc[:, -1][1:11].sum()
    df2[4] = (df2[2]/data_dict[each].iloc[:, -1].sum())/df2[3]
    print(df2)
    plt.bar(df2[0], df2[4], width=df2[3])
    plt.title(each)
    plt.ylim((0, 3.5))
    plt.xticks([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4])
    plt.xlim((-5, 4))
    plt.xlabel('log10 parameter values')
    # plt.savefig(each + '.png')
    # plt.clf()
