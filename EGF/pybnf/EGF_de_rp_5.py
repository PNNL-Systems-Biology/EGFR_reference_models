
import tellurium as te
te.setDefaultPlottingEngine('matplotlib')

r = te.loada('''
model EGF()

  // Compartments and Species:
  compartment cell, extra, intra;
  species RE in cell, R in cell, REi in intra, E in extra, Ri in intra, Rd in cell;
  species Rp in cell, Grb2 in cell, SOS in cell, SOSp in cell, GS in cell, Rp_GS in cell, Rp_GSi in intra;
  species Shc in cell, Rp_Shc in cell, Rp_pShc in cell, pShc in cell, Rp_Shci in intra, Rp_pShci in intra;
  species Rp_pShc_GS in cell, pShc_GS in cell, Rp_pShc_GSi in intra;
  species RasGAP in cell, Rp_RasGAP in cell, IRp_RasGAP in cell;
  species dRas in cell, tRas in cell, bRasGAP in cell, Rp_RasGAP in cell, RasGAP in cell;
  species Raf in cell, Rafp in cell, aRaf in cell, aaRaf in cell, Mek in cell, ppMek in cell;
  species Erk in cell, pErk in cell, ppErk in cell;
  species SOS_ppErk in cell, Pro1433 in cell, SOSp_Pro1433 in cell, Raf_ppErk in cell, Rafp_Pro1433 in cell;
  
  
  // Reactions:
  // EGFR module
  
  New_Receptors: => R; Vr*cell; 
  Receptor_turnover: R => Ri; R*kt*cell;
  Ligand_binding: E + R -> RE; (k1*R*E - k_1*RE)*cell;
  Receptor_ligand_endo: RE => REi; RE*ke*cell;
  Receptor_degrad: Ri => ; Ri*kx*cell;
  Receptor_complex_degrad: REi => ; REi*kh*cell;
  
  Receptor_dimerization: 2RE => Rd; k2*RE*cell;
  Receptor_monomerization: Rd => 2RE; k_2*Rd*cell;
  Dimer_endo: Rd => Rdi; Rd*kt*cell;
  Receptor_phospho: Rd -> Rp; (k3*Rd - k_3*Rp)*cell;
  Dimer_phospho_endo: Rp => Rpi; Rp*ke*cell;
  
    // Grb2-Sos complex formation
  Grb2_Sos_formation: Grb2 + SOS -> GS; (Grb2*SOS*k204 - GS*k_204)*cell;

    // Shc complex formation
  Shc_receptor_bind: Rp + Shc -> Rp_Shc; (k5*Rp*Shc - k_5*Rp_Shc)*cell;
  Shc_phosphorylation: Rp_Shc => Rp_pShc; k6*Rp_Shc*cell;
  PhosphoShc_dissociation: Rp_pShc -> Rp + pShc; (k_7*Rp_pShc - k7*Rp*pShc)*cell;
  Phospho_Shc_dephosphorylation: pShc => Shc; (V8*pShc/(Km8 + pShc))*cell
  Shc_complex_endo: Rp_Shc => Rp_Shci; Rp_Shc*kt*cell;
  Phospho_Shc_complex_endo: Rp_pShc => Rp_pShci; Rp_pShc*kt*cell;
  Shc_complex_recycle: Rp_Shci => Shc; Rp_Shci*krec*intra;
  Phospho_Shc_complex_recycle: Rp_pShci => pShc; Rp_pShci*krec*intra;

    // Direct Grb2-Sos-receptor complex formation  
  Receptor_GS_binding: Rp + GS -> Rp_GS; (Rp*GS*k4 - k_4*Rp_GS)*cell; // Updated 3-20
  Receptor_GS_endo: Rp_GS => Rp_GSi; Rp_GS*ke*cell; // updated 2-20
  GS_endo_recycle: Rp_GSi => GS; Rp_GSi*krec*intra; // Recycle the GS, but leave the receptor

   // Indirect Grb2-Sos - pShc-receptor complex formation
  Receptor_Shc_GS_formation: Rp_pShc + GS -> Rp_pShc_GS; (k9*Rp_pShc*GS - k_9*Rp_pShc_GS)*cell; // form the pShc-receptor complex
  pShc_GS_formation: pShc + GS -> pShc_GS; (k11*pShc*GS - k_11*pShc_GS)*cell;
  Receptor_Shc_GS_formation2: Rp + pShc_GS -> Rp_pShc_GS; (k10*Rp*pShc_GS - k_10*Rp_pShc_GS)*cell;
  Receptor_Shc_GS_endo: Rp_pShc_GS => Rp_pShc_GSi; ke*Rp_pShc_GS*cell; // internalization of the complex
  Shc_GS_recycle: Rp_pShc_GSi => Shc + GS; Rp_pShc_GSi*krec*intra; // recycling of GS and Shc
  
	// RasGap complex formation
  Receptor_RasGap_formation: Rp + RasGAP -> Rp_RasGAP; (k13*Rp*RasGAP - k_13*Rp_RasGAP)*cell;

    // Ras module
  reaction_62: dRas => tRas; (kcat62*dRas*(Rp_pShc_GS + Rp_GS)/(Km62 + dRas))*cell;
  reaction_63: tRas => dRas; (kcat63*tRas*(bRasGAP+Rp_RasGAP)/(Km63 + tRas))*cell;

  // Raf module
  reaction_65: Raf => aRaf; (kcat65*tRas*Raf/(Km65 + Raf))*cell;
  reaction_66: aRaf => aaRaf; (kcat66*aRaf/(Km66 + aRaf))*cell; // changed to standard first order reaction
  reaction_67: aaRaf => Raf; (kcat67*aaRaf/(Km67 + aaRaf))*cell;

  // Mek module
  reaction_68: Mek => ppMek; (kcat68*aaRaf*Mek/(Km68 + Mek))*cell;
  reaction_69: ppMek => Mek; (V69*ppMek/(Km69 + ppMek))*cell;

  // Erk module
  reaction_70: Erk => pErk; (kcat70*Erk*ppMek/(Km70 + Erk + pErk*(Km70/Km71)))*cell;
  reaction_71: pErk => ppErk; (kcat71*pErk*ppMek/(Km71 + pErk + Erk*(Km71/Km70)))*cell;
  reaction_72: ppErk => pErk; (V72*ppErk/(Km72 + ppErk + pErk*(Km72/Km73)))*cell;
  reaction_73: pErk => Erk; (V73*pErk/(Km73 + pErk + ppErk*(Km73/Km72)))*cell;
  
  // Negative feedback from Erk
  Sos_Erk_binding: SOS + ppErk -> SOS_ppErk; (SOS*ppErk*k205 - SOS_ppErk*k_205)*cell;	// Binding of SOS by Erk
  Sos_phosphorylation: SOS_ppErk => ppErk + SOSp; (SOS_ppErk*kcat205)*cell;		// phosphorylation of SOS
  Sos_dephosphorylation: SOSp => SOS; (SOSp*kcat_205)*cell;				// dephosphorylation of pSOS
  SOS_sequestration: SOSp + Pro1433 -> SOSp_Pro1433; (SOSp*Pro1433*k206 - SOSp_Pro1433*k_206)*cell;		// SOS sequestration by 14-3-3 protein binding

  Raf_Erk_binding: Raf + ppErk -> Raf_ppErk; (k60*ppErk*Raf - Rafp*k_60)*cell; 		// Binding of Raf by Erk
  Raf_phosphorylation: Raf_ppErk => ppErk + Rafp; (Raf_ppErk*kcat60)*cell;		// phosphorylation of Raf
  Raf_dephosphorylation: Rafp => Raf; (Rafp*kcat_60)*cell;				// dephosphorylation of Raf
  Raf_sequestration: Rafp + Pro1433 -> Rafp_Pro1433; (Rafp*Pro1433*k61 - Rafp_Pro1433*k_61)*cell;		// Raf sequestration by 14-3-3 protein binding


  // Species initializations:
  var E = 10.0;
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
  SOSp = 0;
  Rp_Shc = 0;
  Rp_pShc = 0;
  Rp_Shci = 0;
  Rp_pShci = 0;
  pShc = 0;
  Rp_GS = 0;
  Rp_GSi = 0;
  Rp_pShc_GS = 0;
  pShc_GS = 0;
  Rp_pShc_GS = 0;
  Rp_pShc_GSi = 0;
  bRasGAP = 2e-3;
  Rp_RasGAP = 0;
  IRp_RasGAP = 0;
  aRaf = 0;
  Rafp = 0;
  pErk = 0;
  aaRaf = 0;
  ppMek = 0;
  ppErk = 0;
  tRas = 0; 	// activated Ras
  Rp_pShc_GS = 0;
  pShc_GS = 0;
  Rp_RasGAP = 0;
  SOS_ppErk = 0;
  SOSp_Pro1433 = 0;
  Raf_ppErk = 0;
  Rafp_Pro1433 = 0;
  
  // Pathway protein abndances
  Grb2 = 37.11;		// updated 3-20
  SOS = 0.07;		// updated 3-20
  GS = 3.98;		// updated 3-20
  Shc = 67.3;
  RasGAP = 25.2;
  dRas = 140; // inactivated Ras
  Raf =30;
  Mek = 128.3;
  Erk = 150;
  Pro1433 = 500;

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
  k2 = 1724.402176407356; // updated 3-20
  k2 has per_nMs;
  k_2 = 7.511807077098653e-07; // updated 3-20
  k_2 has per_sec;
  k3 = 6.405138187659494; // 0.067; // This is the phosphorylation probability
  k3 has per_sec;
  k_3 = 6.830706061788457; // Dephosphorylation probability
  k3 has per_sec;
  k4 = 0.0002829308459220364; // Receptor-GS forward rate constant
  k4 has per_nMs;
  k_4 = 4.387713713910572e-05; // Receptor-GS reverse rate constant
  k_4 has per_sec;
  k5 = 0.0013120004543844379; // Receptor - Shc recruitment
  k5 has per_nMs;
  k_5 = 0.025107592790234456; // Dissociation of Shc from phospho-EGFR
  k_5 has per_sec;
  k6 = 168255167.98391977; // Phosphorylation of Shc
  k6 has per_sec;
  k7 = 10.247258713795604; // Receptor-pShc forward rate constant
  k7 has per_nMs;
  k_7 = 6.559495337579578; // Receptor-pShc reverse rate constant
  k_7 has per_sec;
  V8 = 1.1950500126153385; // Dephosphorylation of Shc
  k8 has per_sec;
  V8 has nM_per_s;
  Km8 = 0.00038462940702344337;
  Km8 has nM;
  k8 = 1.3;	
  k9 = 0.0016497451780867031; // forward rate Grb2-Sos binding to pShc on receptor
  k9 has per_nMs;
  k_9 = 0.0006182349490324431; // dissociation of Grb2-Sos from pShc-receptor complex
  k_9 has per_sec;
  k10 = 18769981154.18988; // association pShc-GS to Rp
  k10 has per_nMs;
  k_10 = 0.06629741183396518; // reverse binding of Grb2-Sos-pShc from receptor
  k_10 has per_sec;
  k11 = 0.0007134527186375951; // association of pShc with GS
  k11 has per_nMs;
  k_11 = 8.280834051801134e+34; // dissociation of pShc-GS complex
  k_11 has per_sec;
  k13 = 0.02350876084665959; // Association of RasGap with EGFR
  k13 has per_nMs;
  k_13 = 59.37629199887897; // Dissociation of RasGap
  k_13 has per_sec;
  krec = 24.51669627747582; // Recycling of the GS to pool
  krec has per_sec;
  k204 = 468648.72921710514; //Grb2-SOS association rate constant
  k204 has per_nMs;
  k_204 = 0.0002118111213033319;
  k_204 has per_sec;	// Grb2-Sos dissociation rate constant
  k205 = 169685172.80849618; // Binding of SOS by Erk
  k205 has per_nMs;
  k_205 = 9.079413337983296e-05; // Dissociation of SOS from ppErk
  k_205 has per_sec;
  kcat205 = 0.5101594465126978; // phosphorylation of SOS
  kcat205 has per_sec;
  kcat_205 = 0.14093674590865204; // dephosphorylation of SOS
  kcat_205 has per_sec;
  k206 = 1.7376112038561815e-12; // Binding of 14-3-3 protein to Sos
  k206 has per_nMs;
  k_206 = 0.2655368306929242; // Dissociation of 14-3-3 protein from Sos
  k_206 has per_sec;
  k60 = 2.586815713947532; // Binding of Raf by Erk
  k60 has per_nMs;
  k_60 = 5.847385035367207; // Dissociation of Raf from ERK
  k_60 has per_sec;
  kcat60 = 0.03031921878189872; // phosphorylation of Raf by Erk
  kcat60 has per_sec;
  kcat_60 = 2.184373456841811e-08; // dephosphorylation of Raf
  kcat_60 has per_sec;
  k61 = 0.29037406362456253; // Binding of 14-3-3 protein to Raf
  k61 has per_nMs;
  k_61 = 0.00020311299206911488; // Dissociation of 14-3-3 protein from Raf
  k_61 has per_sec;
  kcat62 = 0.04685934196468215; // Activation of Ras
  kcat62 has per_sec;
  Km62 = 2.9877218824833676e-05;
  Km62 has nM;
  kcat63 = 3594.274334597429; // ORIG 20000;
  kcat63 has per_sec;
  Km63 = 4.363864997498567e-06;
  Km63 has nM;
  kcat65 = 738806654349313.5;
  kcat65 has per_sec;
  Km65 = 76562.78640721431;
  Km65 has nM;
  kcat66 = 60.689979563422014; // activation of raf
  kcat66 has nM_per_s;
  Km66 = 7419.08711828693; // raf activation equilibrium constant
  Km66 has nM;
  kcat67 = 0.023124414934175483; // inactivation of Raf
  kcat67 has nM_per_s;
  Km67 = 1.7218388601012922; // Equilibrium inactivation of Raf
  Km67 has nM;
  kcat68 = 0.00014877794164681966;
  kcat68 has per_sec;
  Km68 = 336595.3189193795;
  Km68 has nM;
  V69 = 24836760074.48042; // inactivation of Mek
  V69 has nM_per_s;
  Km69 = 3823549375057.23;
  Km69 has nM;
  kcat70 = 353.9302775752609;
  kcat70 has per_sec;
  Km70 = 0.13904093378246135;
  Km70 has nM;
  kcat71 = 6.278265740498987e+36;
  kcat71 has per_sec;
  Km71 = 0.5668034713446758;
  Km71 has nM;
  V72 = 5.212564555406555e+17;
  V72 has nM_per_s;
  Km72 = 11095.26134454957;
  Km72 has nM;
  V73 = 496.65223902035956;
  V73 has nM_per_s;
  Km73 = 1.1404011701895407;
  Km73 has nM;
  
    // Other declarations:
  var k11, k_1, k_2, k_4, k_5, k_7, k_9, k_10, k_11;
  const cell, extra, k1, k2, k3, k4;

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

