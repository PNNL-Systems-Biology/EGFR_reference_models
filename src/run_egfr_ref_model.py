
import tellurium as te

r = te.loada('egfr_ref_model.ant')

sim = r.simulate(0, 10)
print(sim)
