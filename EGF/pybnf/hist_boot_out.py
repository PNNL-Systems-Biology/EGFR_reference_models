
import glob
import os
import pandas as pd
import math
from copy import deepcopy
import matplotlib.pyplot as plt

# os.chdir("/home/michael/PycharmProjects/EGF/pybnf/output_mh_run/Results/Histograms/")
# os.chdir("/home/michael/PycharmProjects/EGF/pybnf/output_pt_run/Results/Histograms/")

pd.set_option('display.width', 1000)
pd.set_option("display.max_columns", 100)
pd.set_option("display.max_rows", 2000)

os.chdir("/home/michael/PycharmProjects/EGF/pybnf/output_sa_node0/Results/")
df0 = pd.read_csv('bootstrapped_parameter_sets.txt', sep='\t')
del df0['#']
del df0['Simulation']
del df0['Obj']

os.chdir("/home/michael/PycharmProjects/EGF/pybnf/output_sa_node1/Results/")
df1 = pd.read_csv('bootstrapped_parameter_sets.txt', sep='\t')
del df1['#']
del df1['Simulation']
del df1['Obj']

os.chdir("/home/michael/PycharmProjects/EGF/pybnf/output_sa_node2/Results/")
df2 = pd.read_csv('bootstrapped_parameter_sets.txt', sep='\t')
del df2['#']
del df2['Simulation']
del df2['Obj']

os.chdir("/home/michael/PycharmProjects/EGF/pybnf/output_sa_node3/Results/")
df3 = pd.read_csv('bootstrapped_parameter_sets.txt', sep='\t')
del df3['#']
del df3['Simulation']
del df3['Obj']

df = pd.concat([df0, df1, df2, df3], ignore_index=True)

print(df)

df = df.applymap(math.log10)
# print(df0)

fig = df.hist(bins=100)
plt.subplots_adjust(hspace=1)
# [x.title.set_size(10) for x in fig.ravel()]
plt.show()
