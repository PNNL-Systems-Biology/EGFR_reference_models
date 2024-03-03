
import tellurium as te
import matplotlib
matplotlib.use('TkAgg')

model = te.loada('''

// Functions

function T_CM_sp(v, kf, kr, s, p, Kms, Kmp, ms, mp)
    (kf*(s/Kms)^ms - kr*(p/Kmp)^mp) / ((1 + (s/Kms))^ms + (1 + (p/Kmp))^mp - 1)
end

function Reg_T_CM_asp(v, ra, kf, kr, a, s, p, Kma, Kms, Kmp, wa, ms, mp)
    ((ra + (1-ra) * ( (a/Kma) / (1 + a/Kma)) )^wa) * (kf*(s/Kms)^ms - kr*(p/Kmp)^mp) / ((1 + (s/Kms))^ms + (1 + (p/Kmp))^mp - 1)
end

function Reg_T_CM_isp(v, ri, kf, kr, i, s, p, Kmi, Kms, Kmp, wi, ms, mp)
    ((ri + (1-ri) * ( 1 / (1 + i/Kmi)) )^wi) * (kf*(s/Kms)^ms - kr*(p/Kmp)^mp) / ((1 + (s/Kms))^ms + (1 + (p/Kmp))^mp - 1)
end

function Reg_T_CM_iiisp(v, ri1, ri2, ri3, kf, kr, i1, i2, i3, s, p, Kmi1, Kmi2, Kmi3, Kms, Kmp, wi1, wi2, wi3, ms, mp)
    ((ri1 + (1-ri1) * ( 1 / (1 + i1/Kmi1)) )^wi1) * ((ri2 + (1-ri2) * ( 1 / (1 + i2/Kmi2)) )^wi2) * ((ri3 + (1-ri3) * ( 1 / (1 + i3/Kmi3)) )^wi3) * (kf*(s/Kms)^ms - kr*(p/Kmp)^mp) / ((1 + (s/Kms))^ms + (1 + (p/Kmp))^mp - 1)
end


model coarse_grained_EGF()

compartment extra = 5000;
species L in extra;

Mig6 = 0;
Spry2 = 0;
Precursor = 0;

L = .2;
E = 0.0;
R = 0.0;
Rp = 0.0;
 
Ligand: E -> L; Reg_T_CM_asp(v1, ro1, k1, k2, Precursor, E, L, KmPre, KmE, KmL, w1, m1, m2);
EGFRp:  L -> Rp; Reg_T_CM_isp(v2, ro2, k3, k4, Mig6, L, Rp, KmMig, KmL, KmP, w2, m3, m4);
Ras:    Rp -> R; Reg_T_CM_iiisp(v3, ro3, ro4, ro5, k5, k6, Spry2, Rp, E, Rp, R, KmSpr, KmPi, KmEi, KmP, KmR, w3, w4, w5, m5, m6)
Erk:    R -> E; T_CM_sp(v4, k7, k8, R, E, KmR, KmE, m7, m8);

// Parameters

v1 = 1;
v2 = 1;
v3 = 1;
v4 = 1;

ro1 = 1;
ro2 = 1;
ro3 = 1;
ro4 = 1;
ro5 = 1;

k1 = 1;
k2 = 1;
k3 = 1;
k4 = 1;
k5 = 1;
k6 = 1;
k7 = 1;
k8 = 1;

KmPre = 1;
KmE = 1;
KmL = 1;
KmMig = 1;
KmP = 1;
KmSpr = 1;
KmPi = 1;
KmEi = 1;
KmR = 1;

w1 = 1;
w2 = 1;
w3 = 1;
w4 = 1;
w5 = 1;

m1 = 1;
m2 = 1;
m3 = 1;
m4 = 1;
m5 = 1;
m6 = 1;
m7 = 1;
m8 = 1;

end
''')

# model.simulate(0, 50, 1000, selections=['time', 'L', 'Rp', 'R', 'E'])
# model.simulate(0, 50, 1000, selections=['time', 'Ligand', 'EGFRp', 'Ras', 'Erk'])
# model.plot()
# model.exportToSBML('EGF_CM_rp.xml')

