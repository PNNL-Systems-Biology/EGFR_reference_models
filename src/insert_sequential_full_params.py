
import pandas as pd
import tellurium as te

data = None
# with open('results/results_a/Results/sorted_params_final.txt', 'r') as file:

with open('Results/sorted_params_final.txt', 'r') as file:
# with open('Results2/Results/sorted_params_final.txt', 'r') as file:
# with open('Results1/Results/sorted_params_final.txt', 'r') as file:
# with open('Results/sorted_params_0.txt', 'r') as file:
# with open('Results/sorted_params_1.txt', 'r') as file:
# with open('Results/sorted_params_2.txt', 'r') as file:
# with open('Results/sorted_params_3.txt', 'r') as file:
# with open('Results/sorted_params_4.txt', 'r') as file:
# with open('Results/sorted_params_5.txt', 'r') as file:
# with open('Results/sorted_params_6.txt', 'r') as file:
# with open('Results/sorted_params_9.txt', 'r') as file:
# with open('Results/sorted_params_14.txt', 'r') as file:
# with open('Results/sorted_params_15.txt', 'r') as file:
# with open('Results/sorted_params_16.txt', 'r') as file:
# with open('Results/sorted_params_17.txt', 'r') as file:
# with open('Results/sorted_params_18.txt', 'r') as file:
# with open('Results/sorted_params_20.txt', 'r') as file:
# with open('Results/sorted_params_22.txt', 'r') as file:
# with open('Results/sorted_params_24.txt', 'r') as file:
# with open('Results/sorted_params_26.txt', 'r') as file:
# with open('Results/sorted_params_27.txt', 'r') as file:
# with open('Results/sorted_params_40.txt', 'r') as file:
    data = file.read().replace('#', '')

with open('parameters', 'w') as params:
    params.write(data)

params_df = pd.read_csv('parameters', delim_whitespace=True)

names = list(params_df.columns)
best = list(params_df.iloc[0])
names = names[2:]
best = best[2:]

param_dict = dict()
for i, name in enumerate(names):
    param_dict[name] = best[i]

print(param_dict)

# model_name = 'EGFR_sequential_fit_4a'
# model_name = 'EGFR_sequential_fit_4b'
# model_name = 'EGFR_sequential_fit_4c'
# model_name = 'EGFR_sequential_fit_4d'
# model_name = 'EGFR_sequential_fit_4e'
# model_name = 'EGFR_sequential_fit_4e2'
# model_name = 'EGFR_sequential_fit_4f'
# model_name = 'EGFR_sequential_fit_4g'
# model_name = 'EGFR_sequential_fit_4h'
# model_name = 'EGFR_sequential_fit_full'
# model_name = 'EGFR_4_HSW'
# model_name = 'EGFR_5_HSW_MK_rev'
# model_name = 'EGFR_5_HSW_MK_rev_2'
# model_name = 'EGFR_5_HSW_MK_rev_3'
model_name = 'EGFR_8a'

new_model = ''
with open(model_name + '.ant', 'r') as model:
    lines = model.readlines()
    for i, line in enumerate(lines):
        print(i, line)
        line_split = line[:-1].strip().split()
        print(i, line_split)
        if line_split and line_split[0] in param_dict:
            line_split[2] = str(param_dict[line_split[0]])
        line = ' '.join(line_split) + '\n'
        new_model += line

print(new_model)

with open(model_name + '.ant', 'w') as cur_mod:
    cur_mod.write(new_model)

r = te.loada(model_name + '.ant')
r.exportToSBML(model_name + '.xml')
