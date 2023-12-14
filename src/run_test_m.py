
import tellurium as te

r = te.loada('m_test.ant')
print(1)
# sim = r.simulate(0, 8, 81, ['time', 'EGFR_aRtot'])
sim = r.simulate(0, 8, 81)
# print(sim)
