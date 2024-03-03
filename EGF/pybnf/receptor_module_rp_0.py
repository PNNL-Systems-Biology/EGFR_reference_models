
import tellurium as te

# Created by libAntimony v2.8.1

r = te.loada('''
model receptor_module

  // Compartments and Species:
  compartment cell, extra, intra;
  species RE in cell, R in cell, REi in intra, E in extra, Ri in intra, Rd in cell, Rp in cell;
  
  // Reactions:
  // EGFR module
  
  New_Receptors: => R; Vr*cell; 
  Receptor_turnover: R => Ri; R*kt*cell;
  Ligand_binding: E + R -> RE; (k1*R*E - k_1*RE)*cell;
  Receptor_ligand_endo: RE => REi; RE*ke*cell;
  Receptor_degrad: Ri => ; Ri*kx*cell;
  Receptor_complex_degrad: REi => ; REi*kh*cell;
  
  Receptor_dimerization: 2RE => Rd; k2*RE*cell;
  // Receptor_dimerization: 2RE => Rd; k2*RE*RE*cell;
  Receptor_monomerization: Rd => 2RE; k_2*Rd*cell;
  Dimer_endo: Rd => Rdi; Rd*kt*cell;
  Receptor_phospho: Rd -> Rp; (k3*Rd - k_3*Rp)*cell;
  Dimer_phospho_endo: Rp => Rpi; Rp*ke*cell;

  // Species initializations:
  var E = 100;
  E has nM;
  R = Vr/kt;
  R has nM;
  RE = 0;
  RE has nM;
  Ri = 0;
  Ri has nM;
  REi = 0;
  REi has nM;
  Rd = 0;
  Rdi = 0;
  Rp = 0;
  Rpi = 0;

 // Compartment initializations:
  cell = 1;
  extra = 5000;
  intra = 1;

 // Variable initializations:
  k1 = 0.0016;
  k1 has per_nMs;
  k_1 = 0.004;
  k_1 has per_sec;
  kt = 0.0012;
  kt has per_sec;
  ke = .0033;
  ke has per_sec;
  Vr = .242;
  Vr has nM_per_sec;
  kx = 1;
  kx has per_sec;
  kh = 0.0004; // 0.00024;
  kh has per_sec; 
  k2 = 74227848212.98192;	// updated 3-20
  k2 has per_nMs;
  k_2 = 2779584.555098004;	// updated 3-20
  k_2 has per_sec;
  k3 = 66484799316.16354;		// 0.067;	// This is the phosphorylation probability
  k3 has per_sec;
  k_3 = 199450350858.46033;				// Dephosphorylation probability
  k_3 has per_sec;
  
  
    // Other declarations:
  var k_1, k_2;
  const cell, extra, k1, k2, k3;


   // Unit definitions:
  unit substance = 1e-9 mole;
  unit time_unit = second;
  unit nM = 1e-9 mole / litre;
  unit per_nM = litre / 1e-9 mole;
  unit per_sec = 1 / second;
  unit nM_per_s = 1e-9 mole / (litre * second);
  unit per_nMs = litre / (1e-9 mole * second);
 
end
''')

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


sim = r.simulate(0, 80, 81, selections=['time', 'Rp'])
time = []
values = []
for each in sim:
    time.append(each[0])
    values.append(each[1])

data = [[], [], []]
with open('egfrpSD7.exp', 'r') as f:

    content = f.readlines()
    for i, each in enumerate(content):
        print(each[:-1])
        if i > 0:
            data[0].append(float(each.split()[0]))
            data[1].append(float(each.split()[1]))
            data[2].append(float(each.split()[2]))

plt.plot(time, values)
plt.errorbar(data[0], data[1], yerr=data[2], capsize=10, marker='o')
plt.title('E=100.0')

# ----------------------------------------------------------------------

plt.show()
