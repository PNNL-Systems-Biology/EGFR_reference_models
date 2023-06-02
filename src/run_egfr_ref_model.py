
import tellurium as te

r = te.loada('EGFR_Reference_Model.ant')

sim = r.simulate(0, 10)
print(sim)
