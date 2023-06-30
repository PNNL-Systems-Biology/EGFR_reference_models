
import tellurium as te

r = te.loada('EGFR_Reference_Model.ant')

# sim = r.simulate(0, 10, 11, ['time', 'Grb2_SOS1_input'])
sim = r.simulate(0, 10, 11)
print(sim)
