
import tellurium as te

r = te.loada('EGFR_Reference_Model.ant')

sim = r.simulate(0, 10, 11, ['time', 'EGFR_aRtot'])
print(sim)
