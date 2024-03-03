
import tellurium as te
#import matplotlib
#matplotlib.use('TkAgg')

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

Mig6 = 0;
Spry2 = 0;
Precursor = 0;

species L in extra;
L = 1.6543;
ppErk = 0.0;
tRas = 0.0;
Rp = 0.0;

Ligand: -> L; Reg_T_CM_asp(v1, ro1, k1, k2, Precursor, ppErk, L, KmPre, KmE, KmL, w1, m1, m2);
EGFRp:  -> Rp; Reg_T_CM_isp(v2, ro2, k3, k4, Mig6, L, Rp, KmMig, KmL, KmP, w2, m3, m4);
LSink: L ->; kLSink*L
RpSink:  Rp ->; kRpSink*Rp
Ras:    -> tRas; Reg_T_CM_iiisp(v3, ro3, ro4, ro5, k5, k6, Spry2, Rp, ppErk, Rp, tRas, KmSpr, KmPi, KmEi, KmP, KmR, w3, w4, w5, m5, m6)
tRasSink: tRas ->; ktRasSink*tRas
Erk:    -> ppErk; T_CM_sp(v4, k7, k8, tRas, ppErk, KmR, KmE, m7, m8);
ppErkSink: ppErk ->; kppErkSink*ppErk

// Parameters

kRpSink = 0.2219705172729163;
ktRasSink = 3423.021627392856;
kppErkSink = 0.20050256327765612;
kLSink = 2.037720492706224e-06;

v1 = 2.1985548651769264e-05;
v2 = 4.7930371347542246e-08;
v3 = 1.7630332027275003e-08;
v4 = 1618.1867263989989;
ro1 = 0.0006249083213605146;
ro2 = 1.7841723390352922;
ro3 = 5.823868476298559e-06;
ro4 = 0.0003725566982371315;
ro5 = 3532.0214067124257;
k1 = 191.52496561874906;
k2 = 8.747483324331377e-05;
k3 = 0.6673318023024665;
k4 = 0.0020407945566302955;
k5 = 78.91696634673548;
k6 = 0.00021765430545511122;
k7 = 3.0059750451086575e-06;
k8 = 0.007922427422437992;

KmPre = 115.5012402485367;
KmE = 0.016580502341118786;
KmL = 1.5030708245755995;
KmMig = 5.286496913644133e-05;
KmP = 88.67366903911191;
KmSpr = 75.58228148024112;
KmPi = 0.000626389735257831;
KmEi = 20.032356955135942;
KmR = 35.28147650393068;

w1 = 13.103901481849986;
w2 = 9.205373862375211e-05;
w3 = 0.5370883280704564;
w4 = 298.5129529638854;
w5 = 733.4072142960459;
m1 = 0.009442421840911777;
m2 = 0.007885125082240645;
m3 = 0.3610352294573804;
m4 = 0.0013477455510368724;
m5 = 3585.4146379610975;
m6 = 0.0013832878611057349;
m7 = 1.8059638077609025e-08;
m8 = 4.165973629055407e-06;

end
''')

#model.simulate(0, 5000, 1000, selections=['time', 'Rp', 'tRas', 'ppErk'])
#model.simulate(0, 50, 1000, selections=['time', 'Ligand', 'EGFRp', 'Ras', 'Erk'])

model.exportToSBML('EGF_CM_rp.xml')

