
import tellurium as te

model = '''

 -> A; k1
 -> B; k2
 -> C; k3
 -> D; k4
 -> E; k5
 -> F; k6
 
 k1 = 1
 k2 = 1
 k3 = 1
 k4 = 1
 k5 = 1
 k6 = 1
 
 A = 1
 B = 1
 C = 1
 D = 1
 E = 1
 F = 1
 
 tot := A + B + C + D + E + F
 
 '''

r = te.loada(model)

sim = r.simulate(0, 10, 11, ['time', 'A', 'tot'])
print(sim)
r.plot()
