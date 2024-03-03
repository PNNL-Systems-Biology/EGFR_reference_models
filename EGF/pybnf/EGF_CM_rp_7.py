
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

L = 100.0;
E = 0.0;
R = 0.0;
Rp = 0.0;
 
Ligand: E -> L; Reg_T_CM_asp(v1, ro1, k1, k2, Precursor, E, L, KmPre, KmE, KmL, w1, m1, m2);
EGFRp:  L -> Rp; Reg_T_CM_isp(v2, ro2, k3, k4, Mig6, L, Rp, KmMig, KmL, KmP, w2, m3, m4);
Ras:    Rp -> R; Reg_T_CM_iiisp(v3, ro3, ro4, ro5, k5, k6, Spry2, Rp, E, Rp, R, KmSpr, KmPi, KmEi, KmP, KmR, w3, w4, w5, m5, m6)
Erk:    R -> E; T_CM_sp(v4, k7, k8, R, E, KmR, KmE, m7, m8);

// Parameters

v1 = 13757.831758633452;
v2 = 394.0312739137179;
v3 = 4.0269710026864526e-08;
v4 = 1.1647713786607116e-07;

ro1 = 8885.293147031864;
ro2 = 0.007148234169889619;
ro3 = 1.554604570750478e-06;
ro4 = 34919.66053942365;
ro5 = 9.216626432711323e-08;

k1 = 19207.4994568695;
k2 = 94727.90791686326;
k3 = 2.114460762798222;
k4 = 93976.33555570827;
k5 = 0.0002088293133506557;
k6 = 18482.34194633765;
k7 = 1.2552851365334215e-06;
k8 = 7.327438389892893;

KmPre = 14.00846322939233;
KmE = 1.1012154754652698e-05;
KmL = 3.744463865624873e-06;
KmMig = 5.381820002229104;
KmP = 535.327663366266;
KmSpr = 20.000010632607292;
KmPi = 6.275808148794529e-06;
KmEi = 0.00012598009438281792;
KmR = 76.85964386117169;

w1 = 0.07122135207832204;
w2 = 2499.365848613704;
w3 = 2.05856147438783e-05;
w4 = 2.09046305867138;
w5 = 1.4514200887093558e-09;

m1 = 8.625286257236256e-05;
m2 = 27.18286764594396;
m3 = 0.11845752243713224;
m4 = 3.7439947716023307;
m5 = 13.107510939142063;
m6 = 167.79433617445633;
m7 = 1.4960753862722897e-09;
m8 = 7.196996116184613e-05;

end
''')

# model.simulate(0, 50, 1000, selections=['time', 'L', 'Rp', 'R', 'E'])
# model.simulate(0, 50, 1000, selections=['time', 'Ligand', 'EGFRp', 'Ras', 'Erk'])
# model.plot()
# model.exportToSBML('EGF_CM_rp.xml')

