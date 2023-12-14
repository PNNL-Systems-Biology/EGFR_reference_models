
import tellurium as te

# module_list = ['EGFR_module.ant', 'GAB_module.ant', 'GAREM_module.ant', 'SHC_module.ant', 'SOS_module2.ant']
# module_list = ['EGFR_module_hsw.ant']
module_list = ['EGFR_module.ant']
# module_list = ['EGFR_Reference_Model.ant']
# module_list = ['RAF_activation_2022.ant']
# module_list = ['RAF_activation_2022_1.ant']
# module_list = ['RAF_activation_2022_erk_fit.ant']
# module_list = ['GAREM_module.ant']
# module_list = ['GAB_module.ant']
# module_list = ['SHC_MA_module.ant']
# module_list = ['SHC_module.ant']
# module_list = ['SOS_module.ant']
# module_list = ['RAF_activation_2022_mek.ant']

for module in module_list:
    r = te.loada(module)
    r.exportToSBML(module[:-4] + '.xml')
