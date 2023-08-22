
import tellurium as te

# module_list = ['EGFR_module.ant', 'GAB_module.ant', 'GAREM_module.ant', 'SHC_module.ant', 'SOS_module.ant']
# module_list = ['EGFR_Reference_Model.ant']
# module_list = ['RAF_activation_2022.ant']
module_list = ['RAF_activation_2022_mek.ant']

for module in module_list:
    r = te.loada(module)
    r.exportToSBML(module[:-4] + '.xml')
