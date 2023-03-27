import tellurium as te
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('TkAgg')

egf_pathway_model = te.loada('''
    
    // === REACTIONS ===
    
    // --- ligand activity --------------------------------------------
    
    // mL (membrane bound ligand) presentation and internalization
    
    J: -> mL; kf - kr * mL
    
    //presentation of receptors
    
    J: -> EGFR; kf
    
    // ligand shedding
    
    J: IROHM2p12_ADAM17p1 + mL -> IROHM2p12_ADAM17p1 + L
    
    // ligand binding receptor
    
    J: L + EGFR -> bEGFR; kf * L * EGFR - kr * bEGFR
    
    // --- EGFR phosphorylation ---------------------------------------
    
    // phosphorylation of bound receptor
    // phosphorylation site 1 is a target of the kinase ERKp12 (and MIG6?)
    
    J: bEGFR + ERKp12 -> bEGFRp1;       kf * bEGFR * ERKp12 - kr * bEGFRp1
    J: bEGFR + MIG6 -> bEGFRp1;         kf * bEGFR * MIG6 - kr * bEGFRp1
    J: bEGFR -> bEGFRp2;                kf * bEGFR - kr * bEGFRp2
    J: bEGFR -> bEGFRp3;                kf * bEGFR - kr * bEGFRp3
    J: bEGFRp1 -> bEGFRp12;             kf * bEGFRp1 - kr * bEGFRp4
    J: bEGFRp1 -> bEGFRp13;             kf * bEGFRp1 - kr * bEGFRp5
    J: bEGFRp2 + ERKp12 -> bEGFRp12;    kf * bEGFRp2 * ERKp12 - kr * bEGFRp6
    J: bEGFRp2 + MIG6 -> bEGFRp12;      kf * bEGFRp2 * MIG6 - kr * bEGFRp6
    J: bEGFRp2 -> bEGFRp23;             kf * bEGFRp2 - kr * bEGFRp7
    J: bEGFRp3 + ERKp12 -> bEGFRp13;    kf * bEGFRp3 * ERKp12 - kr * bEGFRp8
    J: bEGFRp3 + MIG6 -> bEGFRp13;      kf * bEGFRp3 * MIG6 - kr * bEGFRp8
    J: bEGFRp3 -> bEGFRp23;             kf * bEGFRp4 - kr * bEGFRp9
    J: bEGFRp12 -> bEGFRp123;           kf * bEGFRp12 - kr * bEGFRp10
    J: bEGFRp13 -> bEGFRp123;           kf * bEGFRp13 - kr * bEGFRp11
    J: bEGFRp23 + ERKp12 -> bEGFRp123;  kf * bEGFRp23 * ERKp12 - kr * bEGFRp12
    J: bEGFRp23 + MIG6 -> bEGFRp123;    kf * bEGFRp23 * MIG6 - kr * bEGFRp12
    
    // internalization/degradation (one step) of bEGFRp1__
    
    J: bEGFRp1 -> ;     kf
    J: bEGFRp12 -> ;    kf
    J: bEGFRp13 -> ;    kf
    J: bEGFRp123 -> ;   kf
    
    // EGFRp mediated phosphorylation of MIG6
    
    J: bEGFRp1 + MIG6 -> bEGFRp1 + MIG6p;           kf * bEGFRp1 * MIG6 - kr * MIG6p
    J: bEGFRp2 + MIG6 -> bEGFRp2 + MIG6p;           kf * bEGFRp2 * MIG6 - kr * MIG6p
    J: bEGFRp3 + MIG6 -> bEGFRp3 + MIG6p;           kf * bEGFRp3 * MIG6 - kr * MIG6p
    J: bEGFRp12 + MIG6 -> bEGFRp12 + MIG6p;         kf * bEGFRp12 * MIG6 - kr * MIG6p
    J: bEGFRp13 + MIG6 -> bEGFRp13 + MIG6p;         kf * bEGFRp13 * MIG6 - kr * MIG6p
    J: bEGFRp23 + MIG6 -> bEGFRp23 + MIG6p;         kf * bEGFRp23 * MIG6 - kr * MIG6p
    J: bEGFRp123 + MIG6 -> bEGFRp123 + MIG6p;       kf * bEGFRp123 * MIG6 - kr * MIG6p
    
    // --- GAREM phosphorylation -----------------------------------------------------
    
    // EGFRp mediated phosphorylation of GAREM
    
    J: bEGFRp1 + GAREM -> bEGFRp1 + GAREMp;         kf * bEGFRp1 * GAREM - kr * GAREMp
    J: bEGFRp2 + GAREM -> bEGFRp2 + GAREMp;         kf * bEGFRp2 * GAREM - kr * GAREMp
    J: bEGFRp3 + GAREM -> bEGFRp3 + GAREMp;         kf * bEGFRp3 * GAREM - kr * GAREMp
    J: bEGFRp12 + GAREM -> bEGFRp12 + GAREMp;       kf * bEGFRp12 * GAREM - kr * GAREMp
    J: bEGFRp13 + GAREM -> bEGFRp13 + GAREMp;       kf * bEGFRp13 * GAREM - kr * GAREMp
    J: bEGFRp23 + GAREM -> bEGFRp23 + GAREMp;       kf * bEGFRp23 * GAREM - kr * GAREMp
    J: bEGFRp123 + GAREM -> bEGFRp123 + GAREMp;     kf * bEGFRp123 * GAREM - kr * GAREMp
    
    // --- GAREM SHP2 binding ----------------------------------------------------------
    
    // GAREMp and SHP2 binding
    J: GAREMp + SHP2 -> GAREMp_SHP2;    kf * GAREMp * SHP2 - kr * GAREMp_SHP2
    
    // --- SHC1 phosphorylation ---------------------------------------------------------
    
    // EGFRp mediated phosphorylation of SHC1 (SHC1p1)
    
    J: bEGFRp1 + SHC1 -> bEGFRp1 + SHC1p1;              kf * bEGFRp1 * SHC1 - kr * SHC1p1
    J: bEGFRp2 + SHC1 -> bEGFRp2 + SHC1p1;              kf * bEGFRp2 * SHC1 - kr * SHC1p1
    J: bEGFRp3 + SHC1 -> bEGFRp3 + SHC1p1;              kf * bEGFRp3 * SHC1 - kr * SHC1p1
    J: bEGFRp12 + SHC1 -> bEGFRp12 + SHC1p1;            kf * bEGFRp12 * SHC1 - kr * SHC1p1
    J: bEGFRp13 + SHC1 -> bEGFRp13 + SHC1p1;            kf * bEGFRp13 * SHC1 - kr * SHC1p1
    J: bEGFRp23 + SHC1 -> bEGFRp23 + SHC1p1;            kf * bEGFRp23 * SHC1 - kr * SHC1p1
    J: bEGFRp123 + SHC1 -> bEGFRp123 + SHC1p1;          kf * bEGFRp123 * SHC1 - kr * SHC1p1
    
    // EGFRp mediated phosphorylation of SHC1 (SHC1p2)
    
    J: bEGFRp1 + SHC1 -> bEGFRp1 + SHC1p2;              kf * bEGFRp1 * SHC1 - kr * SHC1p2
    J: bEGFRp2 + SHC1 -> bEGFRp2 + SHC1p2;              kf * bEGFRp2 * SHC1 - kr * SHC1p2
    J: bEGFRp3 + SHC1 -> bEGFRp3 + SHC1p2;              kf * bEGFRp3 * SHC1 - kr * SHC1p2
    J: bEGFRp12 + SHC1 -> bEGFRp12 + SHC1p2;            kf * bEGFRp12 * SHC1 - kr * SHC1p2
    J: bEGFRp13 + SHC1 -> bEGFRp13 + SHC1p2;            kf * bEGFRp13 * SHC1 - kr * SHC1p2
    J: bEGFRp23 + SHC1 -> bEGFRp23 + SHC1p2;            kf * bEGFRp23 * SHC1 - kr * SHC1p2
    J: bEGFRp123 + SHC1 -> bEGFRp123 + SHC1p2;          kf * bEGFRp123 * SHC1 - kr * SHC1p2
    
    // EGFRp mediated phosphorylation of SHC1 (SHC1p3)
    
    J: bEGFRp1 + SHC1 -> bEGFRp1 + SHC1p3;              kf * bEGFRp1 * SHC1 - kr * SHC1p3
    J: bEGFRp2 + SHC1 -> bEGFRp2 + SHC1p3;              kf * bEGFRp2 * SHC1 - kr * SHC1p3
    J: bEGFRp3 + SHC1 -> bEGFRp3 + SHC1p3;              kf * bEGFRp3 * SHC1 - kr * SHC1p3
    J: bEGFRp12 + SHC1 -> bEGFRp12 + SHC1p3;            kf * bEGFRp12 * SHC1 - kr * SHC1p3
    J: bEGFRp13 + SHC1 -> bEGFRp13 + SHC1p3;            kf * bEGFRp13 * SHC1 - kr * SHC1p3
    J: bEGFRp23 + SHC1 -> bEGFRp23 + SHC1p3;            kf * bEGFRp23 * SHC1 - kr * SHC1p3
    J: bEGFRp123 + SHC1 -> bEGFRp123 + SHC1p3;          kf * bEGFRp123 * SHC1 - kr * SHC1p3
    
    // EGFRp mediated phosphorylation of SHC1p1 (SHC1p12)
    
    J: bEGFRp1 + SHC1p1 -> bEGFRp1 + SHC1p12;           kf * bEGFRp1 * SHC1p1 - kr * SHC1p12
    J: bEGFRp2 + SHC1p1 -> bEGFRp2 + SHC1p12;           kf * bEGFRp2 * SHC1p1 - kr * SHC1p12
    J: bEGFRp3 + SHC1p1 -> bEGFRp3 + SHC1p12;           kf * bEGFRp3 * SHC1p1 - kr * SHC1p12
    J: bEGFRp12 + SHC1p1 -> bEGFRp12 + SHC1p12;         kf * bEGFRp12 * SHC1p1 - kr * SHC1p12
    J: bEGFRp13 + SHC1p1 -> bEGFRp13 + SHC1p12;         kf * bEGFRp13 * SHC1p1 - kr * SHC1p12
    J: bEGFRp23 + SHC1p1 -> bEGFRp23 + SHC1p12;         kf * bEGFRp23 * SHC1p1 - kr * SHC1p12
    J: bEGFRp123 + SHC1p1 -> bEGFRp123 + SHC1p12;       kf * bEGFRp123 * SHC1p1 - kr * SHC1p12
    
    // EGFRp mediated phosphorylation of SHC1p1 (SHC1p13)
    
    J: bEGFRp1 + SHC1p1 -> bEGFRp1 + SHC1p13;           kf * bEGFRp1 * SHC1p1 - kr * SHC1p13
    J: bEGFRp2 + SHC1p1 -> bEGFRp2 + SHC1p13;           kf * bEGFRp2 * SHC1p1 - kr * SHC1p13
    J: bEGFRp3 + SHC1p1 -> bEGFRp3 + SHC1p13;           kf * bEGFRp3 * SHC1p1 - kr * SHC1p13
    J: bEGFRp12 + SHC1p1 -> bEGFRp12 + SHC1p13;         kf * bEGFRp12 * SHC1p1 - kr * SHC1p13
    J: bEGFRp13 + SHC1p1 -> bEGFRp13 + SHC1p13;         kf * bEGFRp13 * SHC1p1 - kr * SHC1p13
    J: bEGFRp23 + SHC1p1 -> bEGFRp23 + SHC1p13;         kf * bEGFRp23 * SHC1p1 - kr * SHC1p13
    J: bEGFRp123 + SHC1p1 -> bEGFRp123 + SHC1p13;       kf * bEGFRp123 * SHC1p1 - kr * SHC1p13
    
    // EGFRp mediated phosphorylation of SHC1p2 (SHC1p23)
    
    J: bEGFRp1 + SHC1p2 -> bEGFRp1 + SHC1p23;           kf * bEGFRp1 * SHC1p2 - kr * SHC1p23
    J: bEGFRp2 + SHC1p2 -> bEGFRp2 + SHC1p23;           kf * bEGFRp2 * SHC1p2 - kr * SHC1p23
    J: bEGFRp3 + SHC1p2 -> bEGFRp3 + SHC1p23;           kf * bEGFRp3 * SHC1p2 - kr * SHC1p23
    J: bEGFRp12 + SHC1p2 -> bEGFRp12 + SHC1p23;         kf * bEGFRp12 * SHC1p2 - kr * SHC1p23
    J: bEGFRp13 + SHC1p2 -> bEGFRp13 + SHC1p23;         kf * bEGFRp13 * SHC1p2 - kr * SHC1p23
    J: bEGFRp23 + SHC1p2 -> bEGFRp23 + SHC1p23;         kf * bEGFRp23 * SHC1p2 - kr * SHC1p23
    J: bEGFRp123 + SHC1p2 -> bEGFRp123 + SHC1p23;       kf * bEGFRp123 * SHC1p2 - kr * SHC1p23
    
    // EGFRp mediated phosphorylation of SHC1p12 (SHC1p123)
    
    J: bEGFRp1 + SHC1p12 -> bEGFRp1 + SHC1p123;         kf * bEGFRp1 * SHC1p12 - kr * SHC1p123
    J: bEGFRp2 + SHC1p12 -> bEGFRp2 + SHC1p123;         kf * bEGFRp2 * SHC1p12 - kr * SHC1p123
    J: bEGFRp3 + SHC1p12 -> bEGFRp3 + SHC1p123;         kf * bEGFRp3 * SHC1p12 - kr * SHC1p123
    J: bEGFRp12 + SHC1p12 -> bEGFRp12 + SHC1p123;       kf * bEGFRp12 * SHC1p12 - kr * SHC1p123
    J: bEGFRp13 + SHC1p12 -> bEGFRp13 + SHC1p123;       kf * bEGFRp13 * SHC1p12 - kr * SHC1p123
    J: bEGFRp23 + SHC1p12 -> bEGFRp23 + SHC1p123;       kf * bEGFRp23 * SHC1p12 - kr * SHC1p123
    J: bEGFRp123 + SHC1p12 -> bEGFRp123 + SHC1p123;     kf * bEGFRp123 * SHC1p12 - kr * SHC1p123
    
    // EGFRp mediated phosphorylation of SHC1p13 (SHC1p123)
    
    J: bEGFRp1 + SHC1p13 -> bEGFRp1 + SHC1p123;         kf * bEGFRp1 * SHC1p13 - kr * SHC1p123
    J: bEGFRp2 + SHC1p13 -> bEGFRp2 + SHC1p123;         kf * bEGFRp2 * SHC1p13 - kr * SHC1p123
    J: bEGFRp3 + SHC1p13 -> bEGFRp3 + SHC1p123;         kf * bEGFRp3 * SHC1p13 - kr * SHC1p123
    J: bEGFRp12 + SHC1p13 -> bEGFRp12 + SHC1p123;       kf * bEGFRp12 * SHC1p13 - kr * SHC1p123
    J: bEGFRp13 + SHC1p13 -> bEGFRp13 + SHC1p123;       kf * bEGFRp13 * SHC1p13 - kr * SHC1p123
    J: bEGFRp23 + SHC1p13 -> bEGFRp23 + SHC1p123;       kf * bEGFRp23 * SHC1p13 - kr * SHC1p123
    J: bEGFRp123 + SHC1p13 -> bEGFRp123 + SHC1p123;     kf * bEGFRp123 * SHC1p13 - kr * SHC1p123
    
    // EGFRp mediated phosphorylation of SHC1p23 (SHC1p123)
    
    J: bEGFRp1 + SHC1p23 -> bEGFRp1 + SHC1p123;         kf * bEGFRp1 * SHC1p23 - kr * SHC1p123
    J: bEGFRp2 + SHC1p23 -> bEGFRp2 + SHC1p123;         kf * bEGFRp2 * SHC1p23 - kr * SHC1p123
    J: bEGFRp3 + SHC1p23 -> bEGFRp3 + SHC1p123;         kf * bEGFRp3 * SHC1p23 - kr * SHC1p123
    J: bEGFRp12 + SHC1p23 -> bEGFRp12 + SHC1p123;       kf * bEGFRp12 * SHC1p23 - kr * SHC1p123
    J: bEGFRp13 + SHC1p23 -> bEGFRp13 + SHC1p123;       kf * bEGFRp13 * SHC1p23 - kr * SHC1p123
    J: bEGFRp23 + SHC1p23 -> bEGFRp23 + SHC1p123;       kf * bEGFRp23 * SHC1p23 - kr * SHC1p123
    J: bEGFRp123 + SHC1p23 -> bEGFRp123 + SHC1p123;     kf * bEGFRp123 * SHC1p23 - kr * SHC1p123
    
    // --- ERKp12 mediated phosphorylation of GAB1 at site 1 --------------------------------------
    
    J: ERKp12 + GAB1 -> ERKp12 + GAB1p1;      kf * ERKp12 * GAB1 - kr * GAB1p1
    
    // --- GAB1 phosphorylation ------------------------------------------------------------
    
    // EGFRp mediated phosphorylation of GAB1p1 (GAB1p12)
    
    J: bEGFRp1 + GAB1p1 -> bEGFRp1 + GAB1p12;           kf * bEGFRp1 * GAB1p1 - kr * GAB1p12
    J: bEGFRp2 + GAB1p1 -> bEGFRp2 + GAB1p12;           kf * bEGFRp2 * GAB1p1 - kr * GAB1p12
    J: bEGFRp3 + GAB1p1 -> bEGFRp3 + GAB1p12;           kf * bEGFRp3 * GAB1p1 - kr * GAB1p12
    J: bEGFRp12 + GAB1p1 -> bEGFRp12 + GAB1p12;         kf * bEGFRp12 * GAB1p1 - kr * GAB1p12
    J: bEGFRp13 + GAB1p1 -> bEGFRp13 + GAB1p12;         kf * bEGFRp13 * GAB1p1 - kr * GAB1p12
    J: bEGFRp23 + GAB1p1 -> bEGFRp23 + GAB1p12;         kf * bEGFRp23 * GAB1p1 - kr * GAB1p12
    J: bEGFRp123 + GAB1p1 -> bEGFRp123 + GAB1p12;       kf * bEGFRp123 * GAB1p1 - kr * GAB1p12
    
    // EGFRp mediated phosphorylation of GAB1p1 (GAB1p13)
    
    J: bEGFRp1 + GAB1p1 -> bEGFRp1 + GAB1p13;           kf * bEGFRp1 * GAB1p1 - kr * GAB1p13
    J: bEGFRp2 + GAB1p1 -> bEGFRp2 + GAB1p13;           kf * bEGFRp2 * GAB1p1 - kr * GAB1p13
    J: bEGFRp3 + GAB1p1 -> bEGFRp3 + GAB1p13;           kf * bEGFRp3 * GAB1p1 - kr * GAB1p13
    J: bEGFRp12 + GAB1p1 -> bEGFRp12 + GAB1p13;         kf * bEGFRp12 * GAB1p1 - kr * GAB1p13
    J: bEGFRp13 + GAB1p1 -> bEGFRp13 + GAB1p13;         kf * bEGFRp13 * GAB1p1 - kr * GAB1p13
    J: bEGFRp23 + GAB1p1 -> bEGFRp23 + GAB1p13;         kf * bEGFRp23 * GAB1p1 - kr * GAB1p13
    J: bEGFRp123 + GAB1p1 -> bEGFRp123 + GAB1p13;       kf * bEGFRp123 * GAB1p1 - kr * GAB1p13
    
    // EGFRp mediated phosphorylation of GAB1p12 (GAB1p123)
    
    J: bEGFRp1 + GAB1p12 -> bEGFRp1 + GAB1p123;         kf * bEGFRp1 * GAB1p12 - kr * GAB1p123
    J: bEGFRp2 + GAB1p12 -> bEGFRp2 + GAB1p123;         kf * bEGFRp2 * GAB1p12 - kr * GAB1p123
    J: bEGFRp3 + GAB1p12 -> bEGFRp3 + GAB1p123;         kf * bEGFRp3 * GAB1p12 - kr * GAB1p123
    J: bEGFRp12 + GAB1p12 -> bEGFRp12 + GAB1p123;       kf * bEGFRp12 * GAB1p12 - kr * GAB1p123
    J: bEGFRp13 + GAB1p12 -> bEGFRp13 + GAB1p123;       kf * bEGFRp13 * GAB1p12 - kr * GAB1p123
    J: bEGFRp23 + GAB1p12 -> bEGFRp23 + GAB1p123;       kf * bEGFRp23 * GAB1p12 - kr * GAB1p123
    J: bEGFRp123 + GAB1p12 -> bEGFRp123 + GAB1p123;     kf * bEGFRp123 * GAB1p12 - kr * GAB1p123
    
    // EGFRp mediated phosphorylation of GAB1p13 (GAB1p123)
    
    J: bEGFRp1 + GAB1p13 -> bEGFRp1 + GAB1p123;         kf * bEGFRp1 * GAB1p13 - kr * GAB1p123
    J: bEGFRp2 + GAB1p13 -> bEGFRp2 + GAB1p123;         kf * bEGFRp2 * GAB1p13 - kr * GAB1p123
    J: bEGFRp3 + GAB1p13 -> bEGFRp3 + GAB1p123;         kf * bEGFRp3 * GAB1p13 - kr * GAB1p123
    J: bEGFRp12 + GAB1p13 -> bEGFRp12 + GAB1p123;       kf * bEGFRp12 * GAB1p13 - kr * GAB1p123
    J: bEGFRp13 + GAB1p13 -> bEGFRp13 + GAB1p123;       kf * bEGFRp13 * GAB1p13 - kr * GAB1p123
    J: bEGFRp23 + GAB1p13 -> bEGFRp23 + GAB1p123;       kf * bEGFRp23 * GAB1p13 - kr * GAB1p123
    J: bEGFRp123 + GAB1p13 -> bEGFRp123 + GAB1p123;     kf * bEGFRp123 * GAB1p13 - kr * GAB1p123
    
    // --- GAB1 SHP2 binding -------------------------------------------------------------------
    
    // GAB1p and SHP2 binding
    J: GAB1p1 + SHP2 -> GAB1p1_SHP2;        kf * GAB1p1 * SHP2 - kr * GAB1p1_SHP2
    J: GAB1p12 + SHP2 -> GAB1p12_SHP2;      kf * GAB1p12 * SHP2 - kr * GAB1p12_SHP2
    J: GAB1p13 + SHP2 -> GAB1p13_SHP2;      kf * GAB1p13 * SHP2 - kr * GAB1p13_SHP2
    J: GAB1p123 + SHP2 -> GAB1p123_SHP2;    kf * GAB1p123 * SHP2 - kr * GAB1p123_SHP2
    
    // --- GAB1p_2_SHP2 dephosphorylation -------------------------------------------
    
    J: GAB1p2_SHP2 -> GAB1 + SHP2;
    J: GAB1p12_SHP2 -> GAB1p1_SHP2;
    J: GAB1p23_SHP2 -> GAB1p3_SHP2;
    J: GAB1p123_SHP2 -> GAB1p13_SHP2;
    
    // --- Inducement of GRB2_SOS1 complex ----------------------------------------------------
    
    // GAREMp_SHP2 induced
    J: GAREMp_SHP2 + GRB2 + SOS1 -> GAREMp_SHP2 + GRB2_SOS1;    kf * GAREMp_SHP2 * GRB2 * SHP2
    
    // SHC1p induced
    
    J: SHC1p1 + GRB2 + SOS1 -> GAREMp_SHP2 + GRB2_SOS1;         kf * SHC1p1 * GRB2 * SHP2
    J: SHC1p2 + GRB2 + SOS1 -> GAREMp_SHP2 + GRB2_SOS1;         kf * SHC1p2 * GRB2 * SHP2
    J: SHC1p3 + GRB2 + SOS1 -> GAREMp_SHP2 + GRB2_SOS1;         kf * SHC1p3 * GRB2 * SHP2
    J: SHC1p12 + GRB2 + SOS1 -> GAREMp_SHP2 + GRB2_SOS1;        kf * SHC1p12 * GRB2 * SHP2
    J: SHC1p13 + GRB2 + SOS1 -> GAREMp_SHP2 + GRB2_SOS1;        kf * SHC1p13 * GRB2 * SHP2
    J: SHC1p23 + GRB2 + SOS1 -> GAREMp_SHP2 + GRB2_SOS1;        kf * SHC1p23 * GRB2 * SHP2
    J: SHC1p123 + GRB2 + SOS1 -> GAREMp_SHP2 + GRB2_SOS1;       kf * SHC1p123 * GRB2 * SHP2
    
    // GAB1p_SHP2 induced
    
    J: GAB1p1_SHP2 + GRB2 + SOS1 -> GAREMp_SHP2 + GRB2_SOS1;        kf * GAB1p1_SHP2 * GRB2 * SHP2
    J: GAB1p2_SHP2 + GRB2 + SOS1 -> GAREMp_SHP2 + GRB2_SOS1;        kf * GAB1p2_SHP2 * GRB2 * SHP2
    J: GAB1p3_SHP2 + GRB2 + SOS1 -> GAREMp_SHP2 + GRB2_SOS1;        kf * GAB1p3_SHP2 * GRB2 * SHP2
    J: GAB1p12_SHP2 + GRB2 + SOS1 -> GAREMp_SHP2 + GRB2_SOS1;       kf * GAB1p12_SHP2 * GRB2 * SHP2
    J: GAB1p13_SHP2 + GRB2 + SOS1 -> GAREMp_SHP2 + GRB2_SOS1;       kf * GAB1p13_SHP2 * GRB2 * SHP2
    J: GAB1p23_SHP2 + GRB2 + SOS1 -> GAREMp_SHP2 + GRB2_SOS1;       kf * GAB1p23_SHP2 * GRB2 * SHP2
    J: GAB1p123_SHP2 + GRB2 + SOS1 -> GAREMp_SHP2 + GRB2_SOS1;      kf * GAB1p123_SHP2 * GRB2 * SHP2
    
    // --- RSK phosphorylation of SOS1 and disassociation of the GRB2_SOS1 complex ------------------
    
    // RSK
    J: RSK + GRB2_SOS1 -> RSK + GRB2 + SOS1p;           kf * RSK * GRB2_SOS1
    
    // RSK1
    // J: RSK1 + GRB2_SOS1 -> RSK1 + GRB2 + SOS1p;      kf * RSK1 * GRB2_SOS1
    
    // RSK2
    // J: RSK2 + GRB2_SOS1 -> RSK2 + GRB2 + SOS1p;      kf * RSK2 * GRB2_SOS1
    
    // --- Inducement of GRB2_SOS2 complex ----------------------------------------------------
    
    // GAREMp_SHP2 induced
    J: GAREMp_SHP2 + GRB2 + SOS2 -> GAREMp_SHP2 + GRB2_SOS2;    kf * GAREMp_SHP2 * GRB2 * SHP2
    
    // SHC1p induced
    
    J: SHC1p1 + GRB2 + SOS2 -> GAREMp_SHP2 + GRB2_SOS2;         kf * SHC1p1 * GRB2 * SHP2
    J: SHC1p2 + GRB2 + SOS2 -> GAREMp_SHP2 + GRB2_SOS2;         kf * SHC1p2 * GRB2 * SHP2
    J: SHC1p3 + GRB2 + SOS2 -> GAREMp_SHP2 + GRB2_SOS2;         kf * SHC1p3 * GRB2 * SHP2
    J: SHC1p12 + GRB2 + SOS2 -> GAREMp_SHP2 + GRB2_SOS2;        kf * SHC1p12 * GRB2 * SHP2
    J: SHC1p13 + GRB2 + SOS2 -> GAREMp_SHP2 + GRB2_SOS2;        kf * SHC1p13 * GRB2 * SHP2
    J: SHC1p23 + GRB2 + SOS2 -> GAREMp_SHP2 + GRB2_SOS2;        kf * SHC1p23 * GRB2 * SHP2
    J: SHC1p123 + GRB2 + SOS2 -> GAREMp_SHP2 + GRB2_SOS2;       kf * SHC1p123 * GRB2 * SHP2
    
    // GAB1p_SHP2 induced
    
    J: GAB1p1_SHP2 + GRB2 + SOS2 -> GAREMp_SHP2 + GRB2_SOS2;        kf * GAB1p1_SHP2 * GRB2 * SHP2
    J: GAB1p2_SHP2 + GRB2 + SOS2 -> GAREMp_SHP2 + GRB2_SOS2;        kf * GAB1p2_SHP2 * GRB2 * SHP2
    J: GAB1p3_SHP2 + GRB2 + SOS2 -> GAREMp_SHP2 + GRB2_SOS2;        kf * GAB1p3_SHP2 * GRB2 * SHP2
    J: GAB1p12_SHP2 + GRB2 + SOS2 -> GAREMp_SHP2 + GRB2_SOS2;       kf * GAB1p12_SHP2 * GRB2 * SHP2
    J: GAB1p13_SHP2 + GRB2 + SOS2 -> GAREMp_SHP2 + GRB2_SOS2;       kf * GAB1p13_SHP2 * GRB2 * SHP2
    J: GAB1p23_SHP2 + GRB2 + SOS2 -> GAREMp_SHP2 + GRB2_SOS2;       kf * GAB1p23_SHP2 * GRB2 * SHP2
    J: GAB1p123_SHP2 + GRB2 + SOS2 -> GAREMp_SHP2 + GRB2_SOS2;      kf * GAB1p123_SHP2 * GRB2 * SHP2
    
    // --- RSK phosphorylation of SOS2 and disassociation of the GRB2_SOS2 complex ------------------
    
    // RSK1
    J: RSK1 + GRB2_SOS2 -> RSK1 + GRB2 + SOS2p;     kf * RSK1 * GRB2_SOS2
    
    // RSK2
    J: RSK2 + GRB2_SOS2 -> RSK2 + GRB2 + SOS2p;     kf * RSK2 * GRB2_SOS2
    
    // --- RAS activation ------------------------------------------------------
    
    // GRB2_SOS1 induced ras activation
    J: GRB2_SOS1 + RAS -> GRB2_SOS1 + RASa;     kf * GRB2_SOS1 * RAS - kr * RASa
    
    // GRB2_SOS2 induced ras activation
    J: GRB2_SOS2 + RAS -> GRB2_SOS2 + RASa;     kf * GRB2_SOS2 * RAS - kr * RASa
    
    // --- RAF activity -------------------------------------------------------------------
    
    // --- ARAF, BRAF and CRAF recruitment to membrane, dimerization and activation via RAS
    // --- All phosphorylation events that happen in complex are combined into one step here
    
    J: BRAFp2 + RASa -> BRAFp2_RASa;                    kf * BRAFp2 * RASa - kr * BRAFp2_RASa
    J: CRAF + RASa -> RASa_CRAF;                        kf * CRAF * RASa - kr * RASa_CRAF
    J: BRAFp2 + RASa_CRAF -> BRAFp2_RASa_CRAF;          kf * BRAFp2 * RASa_CRAF - kr * BRAFp2_RASa_CRAF
    J: CRAF + BRAFp2_RASa -> BRAFp2_RASa_CRAF;          kf * CRAF * BRAFp2_RASa - kr * BRAFp2_RASa_CRAF
    J: BRAFp2_RASa_CRAF -> BRAF_RASa_CRAFp3;            kf * BRAFp2_RASa_CRAF
    
    J: ARAFp2 + RASa -> RASa_ARAFp2;                    kf * ARAFp2 * RASa - kr * RASa_ARAFp2
    J: BRAFp2 + RASa_ARAFp2 -> BRAFp2_RASa_ARAFp2;      kf * BRAFp2 * RASa_ARAFp2 - kr * BRAFp2_RASa_ARAFp2
    J: ARAFp2 + BRAFp2_RASa -> BRAFp2_RASa_ARAFp2;      kf * ARAFp2 * BRAFp2_RASa - kr * BRAFp2_RASa_ARAFp2
    J: BRAFp2_RASa_ARAFp2 -> BRAF_RASa_ARAFp13          kf * BRAF_RASa_ARAFp13
    
    // --- BRAF-ARAF complex phosphorylation and deactivation by ERKp12
    
    J: ERKp12 + BRAF_RASa_ARAFp13 -> ERKp12 + BRAFp1_RASa_ARAFp13;              kf * ERKp12 * BRAF_RASa_ARAFp13
    J: ERKp12 + BRAF_RASa_ARAFp13 -> ERKp12 + BRAFp3_RASa_ARAFp13;              kf * ERKp12 * BRAF_RASa_ARAFp13
    J: ERKp12 + BRAF_RASa_ARAFp13 -> ERKp12 + BRAFp4_RASa_ARAFp13;              kf * ERKp12 * BRAF_RASa_ARAFp13
    
    J: ERKp12 + BRAF1_RASa_ARAFp13 -> ERKp12 + BRAFp13_RASa_ARAFp13;            kf * ERKp12 * BRAF1_RASa_ARAFp13
    J: ERKp12 + BRAF1_RASa_ARAFp13 -> ERKp12 + BRAFp14_RASa_ARAFp13;            kf * ERKp12 * BRAF1_RASa_ARAFp13
    
    J: ERKp12 + BRAF3_RASa_ARAFp13 -> ERKp12 + BRAFp13_RASa_ARAFp13;            kf * ERKp12 * BRAF3_RASa_ARAFp13
    J: ERKp12 + BRAF3_RASa_ARAFp13 -> ERKp12 + BRAFp14_RASa_ARAFp13;            kf * ERKp12 * BRAF3_RASa_ARAFp13
    
    J: ERKp12 + BRAF4_RASa_ARAFp13 -> ERKp12 + BRAFp14_RASa_ARAFp13;            kf * ERKp12 * BRAF4_RASa_ARAFp13
    J: ERKp12 + BRAF4_RASa_ARAFp13 -> ERKp12 + BRAFp34_RASa_ARAFp13;            kf * ERKp12 * BRAF4_RASa_ARAFp13
    
    J: ERKp12 + BRAF13_RASa_ARAFp13 -> ERKp12 + BRAFp134_RASa_ARAFp13;          kf * ERKp12 * BRAF13_RASa_ARAFp13
    J: ERKp12 + BRAF14_RASa_ARAFp13 -> ERKp12 + BRAFp134_RASa_ARAFp13;          kf * ERKp12 * BRAF14_RASa_ARAFp13
    J: ERKp12 + BRAF34_RASa_ARAFp13 -> ERKp12 + BRAFp134_RASa_ARAFp13;          kf * ERKp12 * BRAF34_RASa_ARAFp13
    
    // --- Dissociation of BRAF-ARAF complex and return to original states
    // --- It is assumed dissociation occurs only after full phosphorylation of BRAF by ERK
    
    J: BRAFp134_RASa_ARAFp13 -> BRAFp134 + RASa + ARAFp13
    
    // --- BRAF-CRAF complex phosphorylation and deactivation by ERK
    
    J: ERKp12 + BRAF_RASa_CRAFp3 -> ERKp12 + BRAFp1_RASa_CRAFp3;                  kf * ERKp12 * BRAF_RASa_CRAFp3
    J: ERKp12 + BRAF_RASa_CRAFp3 -> ERKp12 + BRAFp3_RASa_CRAFp3;                  kf * ERKp12 * BRAF_RASa_CRAFp3
    J: ERKp12 + BRAF_RASa_CRAFp3 -> ERKp12 + BRAFp4_RASa_CRAFp3;                  kf * ERKp12 * BRAF_RASa_CRAFp3
    J: ERKp12 + BRAF_RASa_CRAFp3 -> ERKp12 + BRAF_RASa_CRAFp13;                   kf * ERKp12 * BRAF_RASa_CRAFp3
    J: ERKp12 + BRAF_RASa_CRAFp3 -> ERKp12 + BRAF_RASa_CRAFp23;                   kf * ERKp12 * BRAF_RASa_CRAFp3
    J: ERKp12 + BRAF_RASa_CRAFp3 -> ERKp12 + BRAF_RASa_CRAFp34;                   kf * ERKp12 * BRAF_RASa_CRAFp3
    
    J: ERKp12 + BRAF_RASa_CRAFp13 -> ERKp12 + BRAFp1_RASa_CRAFp13;                kf * ERKp12 * BRAF_RASa_CRAFp13
    J: ERKp12 + BRAF_RASa_CRAFp13 -> ERKp12 + BRAFp3_RASa_CRAFp13;                kf * ERKp12 * BRAF_RASa_CRAFp13
    J: ERKp12 + BRAF_RASa_CRAFp13 -> ERKp12 + BRAFp4_RASa_CRAFp13;                kf * ERKp12 * BRAF_RASa_CRAFp13
    J: ERKp12 + BRAF_RASa_CRAFp13 -> ERKp12 + BRAF_RASa_CRAFp123;                 kf * ERKp12 * BRAF_RASa_CRAFp13
    J: ERKp12 + BRAF_RASa_CRAFp13 -> ERKp12 + BRAF_RASa_CRAFp134;                 kf * ERKp12 * BRAF_RASa_CRAFp13
    
    J: ERKp12 + BRAF_RASa_CRAFp23 -> ERKp12 + BRAFp1_RASa_CRAFp23;                kf * ERKp12 * BRAF_RASa_CRAFp23
    J: ERKp12 + BRAF_RASa_CRAFp23 -> ERKp12 + BRAFp3_RASa_CRAFp23;                kf * ERKp12 * BRAF_RASa_CRAFp23
    J: ERKp12 + BRAF_RASa_CRAFp23 -> ERKp12 + BRAFp4_RASa_CRAFp23;                kf * ERKp12 * BRAF_RASa_CRAFp23
    J: ERKp12 + BRAF_RASa_CRAFp23 -> ERKp12 + BRAF_RASa_CRAFp123;                 kf * ERKp12 * BRAF_RASa_CRAFp23
    J: ERKp12 + BRAF_RASa_CRAFp23 -> ERKp12 + BRAF_RASa_CRAFp234;                 kf * ERKp12 * BRAF_RASa_CRAFp23
    
    J: ERKp12 + BRAF_RASa_CRAFp34 -> ERKp12 + BRAFp1_RASa_CRAFp34;                kf * ERKp12 * BRAF_RASa_CRAFp34
    J: ERKp12 + BRAF_RASa_CRAFp34 -> ERKp12 + BRAFp3_RASa_CRAFp34;                kf * ERKp12 * BRAF_RASa_CRAFp34
    J: ERKp12 + BRAF_RASa_CRAFp34 -> ERKp12 + BRAFp4_RASa_CRAFp34;                kf * ERKp12 * BRAF_RASa_CRAFp34
    J: ERKp12 + BRAF_RASa_CRAFp34 -> ERKp12 + BRAF_RASa_CRAFp134;                 kf * ERKp12 * BRAF_RASa_CRAFp34
    J: ERKp12 + BRAF_RASa_CRAFp34 -> ERKp12 + BRAF_RASa_CRAFp234;                 kf * ERKp12 * BRAF_RASa_CRAFp34
    
    J: ERKp12 + BRAF_RASa_CRAFp123 -> ERKp12 + BRAFp1_RASa_CRAFp123;              kf * ERKp12 * BRAF_RASa_CRAFp123
    J: ERKp12 + BRAF_RASa_CRAFp123 -> ERKp12 + BRAFp3_RASa_CRAFp123;              kf * ERKp12 * BRAF_RASa_CRAFp123
    J: ERKp12 + BRAF_RASa_CRAFp123 -> ERKp12 + BRAFp4_RASa_CRAFp123;              kf * ERKp12 * BRAF_RASa_CRAFp123
    J: ERKp12 + BRAF_RASa_CRAFp123 -> ERKp12 + BRAF_RASa_CRAFp1234;               kf * ERKp12 * BRAF_RASa_CRAFp123
    
    J: ERKp12 + BRAF_RASa_CRAFp134 -> ERKp12 + BRAFp1_RASa_CRAFp134;              kf * ERKp12 * BRAF_RASa_CRAFp134
    J: ERKp12 + BRAF_RASa_CRAFp134 -> ERKp12 + BRAFp3_RASa_CRAFp134;              kf * ERKp12 * BRAF_RASa_CRAFp134
    J: ERKp12 + BRAF_RASa_CRAFp134 -> ERKp12 + BRAFp4_RASa_CRAFp134;              kf * ERKp12 * BRAF_RASa_CRAFp134
    J: ERKp12 + BRAF_RASa_CRAFp134 -> ERKp12 + BRAF_RASa_CRAFp1234;               kf * ERKp12 * BRAF_RASa_CRAFp134
    
    J: ERKp12 + BRAF_RASa_CRAFp234 -> ERKp12 + BRAFp1_RASa_CRAFp234;              kf * ERKp12 * BRAF_RASa_CRAFp234
    J: ERKp12 + BRAF_RASa_CRAFp234 -> ERKp12 + BRAFp3_RASa_CRAFp234;              kf * ERKp12 * BRAF_RASa_CRAFp234
    J: ERKp12 + BRAF_RASa_CRAFp234 -> ERKp12 + BRAFp4_RASa_CRAFp234;              kf * ERKp12 * BRAF_RASa_CRAFp234
    J: ERKp12 + BRAF_RASa_CRAFp234 -> ERKp12 + BRAF_RASa_CRAFp1234;               kf * ERKp12 * BRAF_RASa_CRAFp234
    
    J: ERKp12 + BRAF_RASa_CRAFp1234 -> ERKp12 + BRAFp1_RASa_CRAFp1234;            kf * ERKp12 * BRAF_RASa_CRAFp1234
    J: ERKp12 + BRAF_RASa_CRAFp1234 -> ERKp12 + BRAFp3_RASa_CRAFp1234;            kf * ERKp12 * BRAF_RASa_CRAFp1234
    J: ERKp12 + BRAF_RASa_CRAFp1234 -> ERKp12 + BRAFp4_RASa_CRAFp1234;            kf * ERKp12 * BRAF_RASa_CRAFp1234
    
    J: ERKp12 + BRAFp1_RASa_CRAFp3 -> ERKp12 + BRAFp13_RASa_CRAFp3;               kf * ERKp12 * BRAFp1_RASa_CRAFp3
    J: ERKp12 + BRAFp1_RASa_CRAFp3 -> ERKp12 + BRAFp14_RASa_CRAFp3;               kf * ERKp12 * BRAFp1_RASa_CRAFp3
    J: ERKp12 + BRAFp1_RASa_CRAFp3 -> ERKp12 + BRAFp1_RASa_CRAFp13;               kf * ERKp12 * BRAFp1_RASa_CRAFp3
    J: ERKp12 + BRAFp1_RASa_CRAFp3 -> ERKp12 + BRAFp1_RASa_CRAFp23;               kf * ERKp12 * BRAFp1_RASa_CRAFp3
    J: ERKp12 + BRAFp1_RASa_CRAFp3 -> ERKp12 + BRAFp1_RASa_CRAFp34;               kf * ERKp12 * BRAFp1_RASa_CRAFp3
    
    J: ERKp12 + BRAFp1_RASa_CRAFp13 -> ERKp12 + BRAFp13_RASa_CRAFp13;             kf * ERKp12 * BRAFp1_RASa_CRAFp13
    J: ERKp12 + BRAFp1_RASa_CRAFp13 -> ERKp12 + BRAFp14_RASa_CRAFp13;             kf * ERKp12 * BRAFp1_RASa_CRAFp13
    J: ERKp12 + BRAFp1_RASa_CRAFp13 -> ERKp12 + BRAFp1_RASa_CRAFp123;             kf * ERKp12 * BRAFp1_RASa_CRAFp13
    J: ERKp12 + BRAFp1_RASa_CRAFp13 -> ERKp12 + BRAFp1_RASa_CRAFp134;             kf * ERKp12 * BRAFp1_RASa_CRAFp13
    
    J: ERKp12 + BRAFp1_RASa_CRAFp23 -> ERKp12 + BRAFp13_RASa_CRAFp23;             kf * ERKp12 * BRAFp1_RASa_CRAFp23
    J: ERKp12 + BRAFp1_RASa_CRAFp23 -> ERKp12 + BRAFp14_RASa_CRAFp23;             kf * ERKp12 * BRAFp1_RASa_CRAFp23
    J: ERKp12 + BRAFp1_RASa_CRAFp23 -> ERKp12 + BRAFp1_RASa_CRAFp123;             kf * ERKp12 * BRAFp1_RASa_CRAFp23
    J: ERKp12 + BRAFp1_RASa_CRAFp23 -> ERKp12 + BRAFp1_RASa_CRAFp234;             kf * ERKp12 * BRAFp1_RASa_CRAFp23
    
    J: ERKp12 + BRAFp1_RASa_CRAFp34 -> ERKp12 + BRAFp13_RASa_CRAFp34;             kf * ERKp12 * BRAFp1_RASa_CRAFp34
    J: ERKp12 + BRAFp1_RASa_CRAFp34 -> ERKp12 + BRAFp14_RASa_CRAFp34;             kf * ERKp12 * BRAFp1_RASa_CRAFp34
    J: ERKp12 + BRAFp1_RASa_CRAFp34 -> ERKp12 + BRAFp1_RASa_CRAFp134;             kf * ERKp12 * BRAFp1_RASa_CRAFp34
    J: ERKp12 + BRAFp1_RASa_CRAFp34 -> ERKp12 + BRAFp1_RASa_CRAFp234;             kf * ERKp12 * BRAFp1_RASa_CRAFp34
    
    J: ERKp12 + BRAFp1_RASa_CRAFp123 -> ERKp12 + BRAFp13_RASa_CRAFp123;           kf * ERKp12 * BRAFp1_RASa_CRAFp123
    J: ERKp12 + BRAFp1_RASa_CRAFp123 -> ERKp12 + BRAFp14_RASa_CRAFp123;           kf * ERKp12 * BRAFp1_RASa_CRAFp123
    J: ERKp12 + BRAFp1_RASa_CRAFp123 -> ERKp12 + BRAFp1_RASa_CRAFp1234;           kf * ERKp12 * BRAFp1_RASa_CRAFp123
    
    J: ERKp12 + BRAFp1_RASa_CRAFp134 -> ERKp12 + BRAFp13_RASa_CRAFp134;           kf * ERKp12 * BRAFp1_RASa_CRAFp134
    J: ERKp12 + BRAFp1_RASa_CRAFp134 -> ERKp12 + BRAFp14_RASa_CRAFp134;           kf * ERKp12 * BRAFp1_RASa_CRAFp134
    J: ERKp12 + BRAFp1_RASa_CRAFp134 -> ERKp12 + BRAFp1_RASa_CRAFp1234;           kf * ERKp12 * BRAFp1_RASa_CRAFp134
    
    J: ERKp12 + BRAFp1_RASa_CRAFp234 -> ERKp12 + BRAFp13_RASa_CRAFp234;           kf * ERKp12 * BRAFp1_RASa_CRAFp234
    J: ERKp12 + BRAFp1_RASa_CRAFp234 -> ERKp12 + BRAFp14_RASa_CRAFp234;           kf * ERKp12 * BRAFp1_RASa_CRAFp234
    J: ERKp12 + BRAFp1_RASa_CRAFp234 -> ERKp12 + BRAFp1_RASa_CRAFp1234;           kf * ERKp12 * BRAFp1_RASa_CRAFp234
    
    J: ERKp12 + BRAFp1_RASa_CRAFp1234 -> ERKp12 + BRAFp13_RASa_CRAFp1234;         kf * ERKp12 * BRAFp1_RASa_CRAFp1234
    J: ERKp12 + BRAFp1_RASa_CRAFp1234 -> ERKp12 + BRAFp14_RASa_CRAFp1234;         kf * ERKp12 * BRAFp1_RASa_CRAFp1234
    
    J: ERKp12 + BRAFp3_RASa_CRAFp3 -> ERKp12 + BRAFp13_RASa_CRAFp3;               kf * ERKp12 * BRAFp3_RASa_CRAFp3
    J: ERKp12 + BRAFp3_RASa_CRAFp3 -> ERKp12 + BRAFp34_RASa_CRAFp3;               kf * ERKp12 * BRAFp3_RASa_CRAFp3
    J: ERKp12 + BRAFp3_RASa_CRAFp3 -> ERKp12 + BRAFp3_RASa_CRAFp13;               kf * ERKp12 * BRAFp3_RASa_CRAFp3
    J: ERKp12 + BRAFp3_RASa_CRAFp3 -> ERKp12 + BRAFp3_RASa_CRAFp23;               kf * ERKp12 * BRAFp3_RASa_CRAFp3
    J: ERKp12 + BRAFp3_RASa_CRAFp3 -> ERKp12 + BRAFp3_RASa_CRAFp34;               kf * ERKp12 * BRAFp3_RASa_CRAFp3
    
    J: ERKp12 + BRAFp3_RASa_CRAFp13 -> ERKp12 + BRAFp13_RASa_CRAFp13;             kf * ERKp12 * BRAFp3_RASa_CRAFp13
    J: ERKp12 + BRAFp3_RASa_CRAFp13 -> ERKp12 + BRAFp34_RASa_CRAFp13;             kf * ERKp12 * BRAFp3_RASa_CRAFp13
    J: ERKp12 + BRAFp3_RASa_CRAFp13 -> ERKp12 + BRAFp3_RASa_CRAFp123;             kf * ERKp12 * BRAFp3_RASa_CRAFp13
    J: ERKp12 + BRAFp3_RASa_CRAFp13 -> ERKp12 + BRAFp3_RASa_CRAFp134;             kf * ERKp12 * BRAFp3_RASa_CRAFp13
    
    J: ERKp12 + BRAFp3_RASa_CRAFp23 -> ERKp12 + BRAFp13_RASa_CRAFp23;             kf * ERKp12 * BRAFp3_RASa_CRAFp23
    J: ERKp12 + BRAFp3_RASa_CRAFp23 -> ERKp12 + BRAFp34_RASa_CRAFp23;             kf * ERKp12 * BRAFp3_RASa_CRAFp23
    J: ERKp12 + BRAFp3_RASa_CRAFp23 -> ERKp12 + BRAFp3_RASa_CRAFp123;             kf * ERKp12 * BRAFp3_RASa_CRAFp23
    J: ERKp12 + BRAFp3_RASa_CRAFp23 -> ERKp12 + BRAFp3_RASa_CRAFp234;             kf * ERKp12 * BRAFp3_RASa_CRAFp23
    
    J: ERKp12 + BRAFp3_RASa_CRAFp34 -> ERKp12 + BRAFp13_RASa_CRAFp34;             kf * ERKp12 * BRAFp3_RASa_CRAFp34
    J: ERKp12 + BRAFp3_RASa_CRAFp34 -> ERKp12 + BRAFp34_RASa_CRAFp34;             kf * ERKp12 * BRAFp3_RASa_CRAFp34
    J: ERKp12 + BRAFp3_RASa_CRAFp34 -> ERKp12 + BRAFp3_RASa_CRAFp134;             kf * ERKp12 * BRAFp3_RASa_CRAFp34
    J: ERKp12 + BRAFp3_RASa_CRAFp34 -> ERKp12 + BRAFp3_RASa_CRAFp234;             kf * ERKp12 * BRAFp3_RASa_CRAFp34
    
    J: ERKp12 + BRAFp3_RASa_CRAFp123 -> ERKp12 + BRAFp13_RASa_CRAFp123;           kf * ERKp12 * BRAFp3_RASa_CRAFp123
    J: ERKp12 + BRAFp3_RASa_CRAFp123 -> ERKp12 + BRAFp34_RASa_CRAFp123;           kf * ERKp12 * BRAFp3_RASa_CRAFp123
    J: ERKp12 + BRAFp3_RASa_CRAFp123 -> ERKp12 + BRAFp3_RASa_CRAFp1234;           kf * ERKp12 * BRAFp3_RASa_CRAFp123
    
    J: ERKp12 + BRAFp3_RASa_CRAFp134 -> ERKp12 + BRAFp13_RASa_CRAFp134;           kf * ERKp12 * BRAFp3_RASa_CRAFp134
    J: ERKp12 + BRAFp3_RASa_CRAFp134 -> ERKp12 + BRAFp34_RASa_CRAFp134;           kf * ERKp12 * BRAFp3_RASa_CRAFp134
    J: ERKp12 + BRAFp3_RASa_CRAFp134 -> ERKp12 + BRAFp3_RASa_CRAFp1234;           kf * ERKp12 * BRAFp3_RASa_CRAFp134
    
    J: ERKp12 + BRAFp3_RASa_CRAFp234 -> ERKp12 + BRAFp13_RASa_CRAFp234;           kf * ERKp12 * BRAFp3_RASa_CRAFp234
    J: ERKp12 + BRAFp3_RASa_CRAFp234 -> ERKp12 + BRAFp34_RASa_CRAFp234;           kf * ERKp12 * BRAFp3_RASa_CRAFp234
    J: ERKp12 + BRAFp3_RASa_CRAFp234 -> ERKp12 + BRAFp3_RASa_CRAFp1234;           kf * ERKp12 * BRAFp3_RASa_CRAFp234
    
    J: ERKp12 + BRAFp3_RASa_CRAFp1234 -> ERKp12 + BRAFp13_RASa_CRAFp1234;         kf * ERKp12 * BRAFp3_RASa_CRAFp1234
    J: ERKp12 + BRAFp3_RASa_CRAFp1234 -> ERKp12 + BRAFp34_RASa_CRAFp1234;         kf * ERKp12 * BRAFp3_RASa_CRAFp1234
    
    J: ERKp12 + BRAFp4_RASa_CRAFp3 -> ERKp12 + BRAFp14_RASa_CRAFp3;               kf * ERKp12 * BRAFp4_RASa_CRAFp3
    J: ERKp12 + BRAFp4_RASa_CRAFp3 -> ERKp12 + BRAFp34_RASa_CRAFp3;               kf * ERKp12 * BRAFp4_RASa_CRAFp3
    J: ERKp12 + BRAFp4_RASa_CRAFp3 -> ERKp12 + BRAFp4_RASa_CRAFp13;               kf * ERKp12 * BRAFp4_RASa_CRAFp3
    J: ERKp12 + BRAFp4_RASa_CRAFp3 -> ERKp12 + BRAFp4_RASa_CRAFp23;               kf * ERKp12 * BRAFp4_RASa_CRAFp3
    J: ERKp12 + BRAFp4_RASa_CRAFp3 -> ERKp12 + BRAFp4_RASa_CRAFp34;               kf * ERKp12 * BRAFp4_RASa_CRAFp3
    
    J: ERKp12 + BRAFp4_RASa_CRAFp13 -> ERKp12 + BRAFp14_RASa_CRAFp13;             kf * ERKp12 * BRAFp4_RASa_CRAFp13
    J: ERKp12 + BRAFp4_RASa_CRAFp13 -> ERKp12 + BRAFp34_RASa_CRAFp13;             kf * ERKp12 * BRAFp4_RASa_CRAFp13
    J: ERKp12 + BRAFp4_RASa_CRAFp13 -> ERKp12 + BRAFp4_RASa_CRAFp123;             kf * ERKp12 * BRAFp4_RASa_CRAFp13
    J: ERKp12 + BRAFp4_RASa_CRAFp13 -> ERKp12 + BRAFp4_RASa_CRAFp134;             kf * ERKp12 * BRAFp4_RASa_CRAFp13
    
    J: ERKp12 + BRAFp4_RASa_CRAFp23 -> ERKp12 + BRAFp14_RASa_CRAFp23;             kf * ERKp12 * BRAFp4_RASa_CRAFp23
    J: ERKp12 + BRAFp4_RASa_CRAFp23 -> ERKp12 + BRAFp34_RASa_CRAFp23;             kf * ERKp12 * BRAFp4_RASa_CRAFp23
    J: ERKp12 + BRAFp4_RASa_CRAFp23 -> ERKp12 + BRAFp4_RASa_CRAFp123;             kf * ERKp12 * BRAFp4_RASa_CRAFp23
    J: ERKp12 + BRAFp4_RASa_CRAFp23 -> ERKp12 + BRAFp4_RASa_CRAFp234;             kf * ERKp12 * BRAFp4_RASa_CRAFp23
    
    J: ERKp12 + BRAFp4_RASa_CRAFp34 -> ERKp12 + BRAFp14_RASa_CRAFp34;             kf * ERKp12 * BRAFp4_RASa_CRAFp34
    J: ERKp12 + BRAFp4_RASa_CRAFp34 -> ERKp12 + BRAFp34_RASa_CRAFp34;             kf * ERKp12 * BRAFp4_RASa_CRAFp34
    J: ERKp12 + BRAFp4_RASa_CRAFp34 -> ERKp12 + BRAFp4_RASa_CRAFp134;             kf * ERKp12 * BRAFp4_RASa_CRAFp34
    J: ERKp12 + BRAFp4_RASa_CRAFp34 -> ERKp12 + BRAFp4_RASa_CRAFp234;             kf * ERKp12 * BRAFp4_RASa_CRAFp34
    
    J: ERKp12 + BRAFp4_RASa_CRAFp123 -> ERKp12 + BRAFp14_RASa_CRAFp123;           kf * ERKp12 * BRAFp4_RASa_CRAFp123
    J: ERKp12 + BRAFp4_RASa_CRAFp123 -> ERKp12 + BRAFp34_RASa_CRAFp123;           kf * ERKp12 * BRAFp4_RASa_CRAFp123
    J: ERKp12 + BRAFp4_RASa_CRAFp123 -> ERKp12 + BRAFp4_RASa_CRAFp1234;           kf * ERKp12 * BRAFp4_RASa_CRAFp123
    
    J: ERKp12 + BRAFp4_RASa_CRAFp134 -> ERKp12 + BRAFp14_RASa_CRAFp134;           kf * ERKp12 * BRAFp4_RASa_CRAFp134
    J: ERKp12 + BRAFp4_RASa_CRAFp134 -> ERKp12 + BRAFp34_RASa_CRAFp134;           kf * ERKp12 * BRAFp4_RASa_CRAFp134
    J: ERKp12 + BRAFp4_RASa_CRAFp134 -> ERKp12 + BRAFp4_RASa_CRAFp1234;           kf * ERKp12 * BRAFp4_RASa_CRAFp134
    
    J: ERKp12 + BRAFp4_RASa_CRAFp234 -> ERKp12 + BRAFp14_RASa_CRAFp234;           kf * ERKp12 * BRAFp4_RASa_CRAFp234
    J: ERKp12 + BRAFp4_RASa_CRAFp234 -> ERKp12 + BRAFp34_RASa_CRAFp234;           kf * ERKp12 * BRAFp4_RASa_CRAFp234
    J: ERKp12 + BRAFp4_RASa_CRAFp234 -> ERKp12 + BRAFp4_RASa_CRAFp1234;           kf * ERKp12 * BRAFp4_RASa_CRAFp234
    
    J: ERKp12 + BRAFp4_RASa_CRAFp1234 -> ERKp12 + BRAFp14_RASa_CRAFp1234;         kf * ERKp12 * BRAFp4_RASa_CRAFp1234
    J: ERKp12 + BRAFp4_RASa_CRAFp1234 -> ERKp12 + BRAFp34_RASa_CRAFp1234;         kf * ERKp12 * BRAFp4_RASa_CRAFp1234
    
    J: ERKp12 + BRAFp13_RASa_CRAFp3 -> ERKp12 + BRAFp134_RASa_CRAFp3;             kf * ERKp12 * BRAFp13_RASa_CRAFp3
    J: ERKp12 + BRAFp13_RASa_CRAFp3 -> ERKp12 + BRAFp13_RASa_CRAFp13;             kf * ERKp12 * BRAFp13_RASa_CRAFp3
    J: ERKp12 + BRAFp13_RASa_CRAFp3 -> ERKp12 + BRAFp13_RASa_CRAFp23;             kf * ERKp12 * BRAFp13_RASa_CRAFp3
    J: ERKp12 + BRAFp13_RASa_CRAFp3 -> ERKp12 + BRAFp13_RASa_CRAFp34;             kf * ERKp12 * BRAFp13_RASa_CRAFp3
    
    J: ERKp12 + BRAFp13_RASa_CRAFp13 -> ERKp12 + BRAFp134_RASa_CRAFp13;           kf * ERKp12 * BRAFp13_RASa_CRAFp13
    J: ERKp12 + BRAFp13_RASa_CRAFp13 -> ERKp12 + BRAFp13_RASa_CRAFp123;           kf * ERKp12 * BRAFp13_RASa_CRAFp13
    J: ERKp12 + BRAFp13_RASa_CRAFp13 -> ERKp12 + BRAFp13_RASa_CRAFp134;           kf * ERKp12 * BRAFp13_RASa_CRAFp13
    
    J: ERKp12 + BRAFp13_RASa_CRAFp23 -> ERKp12 + BRAFp134_RASa_CRAFp23;           kf * ERKp12 * BRAFp13_RASa_CRAFp23
    J: ERKp12 + BRAFp13_RASa_CRAFp23 -> ERKp12 + BRAFp13_RASa_CRAFp123;           kf * ERKp12 * BRAFp13_RASa_CRAFp23
    J: ERKp12 + BRAFp13_RASa_CRAFp23 -> ERKp12 + BRAFp13_RASa_CRAFp234;           kf * ERKp12 * BRAFp13_RASa_CRAFp23
    
    J: ERKp12 + BRAFp13_RASa_CRAFp34 -> ERKp12 + BRAFp134_RASa_CRAFp34;           kf * ERKp12 * BRAFp13_RASa_CRAFp34
    J: ERKp12 + BRAFp13_RASa_CRAFp34 -> ERKp12 + BRAFp13_RASa_CRAFp134;           kf * ERKp12 * BRAFp13_RASa_CRAFp34
    J: ERKp12 + BRAFp13_RASa_CRAFp34 -> ERKp12 + BRAFp13_RASa_CRAFp234;           kf * ERKp12 * BRAFp13_RASa_CRAFp34
    
    J: ERKp12 + BRAFp13_RASa_CRAFp123 -> ERKp12 + BRAFp134_RASa_CRAFp123;         kf * ERKp12 * BRAFp13_RASa_CRAFp123
    J: ERKp12 + BRAFp13_RASa_CRAFp123 -> ERKp12 + BRAFp13_RASa_CRAFp1234;         kf * ERKp12 * BRAFp13_RASa_CRAFp123
    
    J: ERKp12 + BRAFp13_RASa_CRAFp134 -> ERKp12 + BRAFp134_RASa_CRAFp134;         kf * ERKp12 * BRAFp13_RASa_CRAFp134
    J: ERKp12 + BRAFp13_RASa_CRAFp134 -> ERKp12 + BRAFp13_RASa_CRAFp1234;         kf * ERKp12 * BRAFp13_RASa_CRAFp134
    
    J: ERKp12 + BRAFp13_RASa_CRAFp234 -> ERKp12 + BRAFp134_RASa_CRAFp234;         kf * ERKp12 * BRAFp13_RASa_CRAFp234
    J: ERKp12 + BRAFp13_RASa_CRAFp234 -> ERKp12 + BRAFp13_RASa_CRAFp1234;         kf * ERKp12 * BRAFp13_RASa_CRAFp234
    
    J: ERKp12 + BRAFp13_RASa_CRAFp1234 -> ERKp12 + BRAFp134_RASa_CRAFp1234;       kf * ERKp12 * BRAFp13_RASa_CRAFp1234
    
    J: ERKp12 + BRAFp14_RASa_CRAFp3 -> ERKp12 + BRAFp134_RASa_CRAFp3;             kf * ERKp12 * BRAFp14_RASa_CRAFp3
    J: ERKp12 + BRAFp14_RASa_CRAFp3 -> ERKp12 + BRAFp14_RASa_CRAFp13;             kf * ERKp12 * BRAFp14_RASa_CRAFp3
    J: ERKp12 + BRAFp14_RASa_CRAFp3 -> ERKp12 + BRAFp14_RASa_CRAFp23;             kf * ERKp12 * BRAFp14_RASa_CRAFp3
    J: ERKp12 + BRAFp14_RASa_CRAFp3 -> ERKp12 + BRAFp14_RASa_CRAFp34;             kf * ERKp12 * BRAFp14_RASa_CRAFp3
    
    J: ERKp12 + BRAFp14_RASa_CRAFp13 -> ERKp12 + BRAFp134_RASa_CRAFp13;           kf * ERKp12 * BRAFp14_RASa_CRAFp13
    J: ERKp12 + BRAFp14_RASa_CRAFp13 -> ERKp12 + BRAFp14_RASa_CRAFp123;           kf * ERKp12 * BRAFp14_RASa_CRAFp13
    J: ERKp12 + BRAFp14_RASa_CRAFp13 -> ERKp12 + BRAFp14_RASa_CRAFp134;           kf * ERKp12 * BRAFp14_RASa_CRAFp13
    
    J: ERKp12 + BRAFp14_RASa_CRAFp23 -> ERKp12 + BRAFp134_RASa_CRAFp23;           kf * ERKp12 * BRAFp14_RASa_CRAFp23
    J: ERKp12 + BRAFp14_RASa_CRAFp23 -> ERKp12 + BRAFp14_RASa_CRAFp123;           kf * ERKp12 * BRAFp14_RASa_CRAFp23
    J: ERKp12 + BRAFp14_RASa_CRAFp23 -> ERKp12 + BRAFp14_RASa_CRAFp234;           kf * ERKp12 * BRAFp14_RASa_CRAFp23
    
    J: ERKp12 + BRAFp14_RASa_CRAFp34 -> ERKp12 + BRAFp134_RASa_CRAFp34;           kf * ERKp12 * BRAFp14_RASa_CRAFp34
    J: ERKp12 + BRAFp14_RASa_CRAFp34 -> ERKp12 + BRAFp14_RASa_CRAFp134;           kf * ERKp12 * BRAFp14_RASa_CRAFp34
    J: ERKp12 + BRAFp14_RASa_CRAFp34 -> ERKp12 + BRAFp14_RASa_CRAFp234;           kf * ERKp12 * BRAFp14_RASa_CRAFp34
    
    J: ERKp12 + BRAFp14_RASa_CRAFp123 -> ERKp12 + BRAFp134_RASa_CRAFp123;         kf * ERKp12 * BRAFp14_RASa_CRAFp123
    J: ERKp12 + BRAFp14_RASa_CRAFp123 -> ERKp12 + BRAFp14_RASa_CRAFp1234;         kf * ERKp12 * BRAFp14_RASa_CRAFp123
    
    J: ERKp12 + BRAFp14_RASa_CRAFp134 -> ERKp12 + BRAFp134_RASa_CRAFp134;         kf * ERKp12 * BRAFp14_RASa_CRAFp134
    J: ERKp12 + BRAFp14_RASa_CRAFp134 -> ERKp12 + BRAFp14_RASa_CRAFp1234;         kf * ERKp12 * BRAFp14_RASa_CRAFp134
    
    J: ERKp12 + BRAFp14_RASa_CRAFp234 -> ERKp12 + BRAFp134_RASa_CRAFp234;         kf * ERKp12 * BRAFp14_RASa_CRAFp234
    J: ERKp12 + BRAFp14_RASa_CRAFp234 -> ERKp12 + BRAFp14_RASa_CRAFp1234;         kf * ERKp12 * BRAFp14_RASa_CRAFp234
    
    J: ERKp12 + BRAFp14_RASa_CRAFp1234 -> ERKp12 + BRAFp134_RASa_CRAFp1234;       kf * ERKp12 * BRAFp14_RASa_CRAFp1234
    
    J: ERKp12 + BRAFp34_RASa_CRAFp3 -> ERKp12 + BRAFp134_RASa_CRAFp3;             kf * ERKp12 * BRAFp34_RASa_CRAFp3
    J: ERKp12 + BRAFp34_RASa_CRAFp3 -> ERKp12 + BRAFp34_RASa_CRAFp13;             kf * ERKp12 * BRAFp34_RASa_CRAFp3
    J: ERKp12 + BRAFp34_RASa_CRAFp3 -> ERKp12 + BRAFp34_RASa_CRAFp23;             kf * ERKp12 * BRAFp34_RASa_CRAFp3
    J: ERKp12 + BRAFp34_RASa_CRAFp3 -> ERKp12 + BRAFp34_RASa_CRAFp34;             kf * ERKp12 * BRAFp34_RASa_CRAFp3
    
    J: ERKp12 + BRAFp34_RASa_CRAFp13 -> ERKp12 + BRAFp134_RASa_CRAFp13;           kf * ERKp12 * BRAFp34_RASa_CRAFp13
    J: ERKp12 + BRAFp34_RASa_CRAFp13 -> ERKp12 + BRAFp34_RASa_CRAFp123;           kf * ERKp12 * BRAFp34_RASa_CRAFp13
    J: ERKp12 + BRAFp34_RASa_CRAFp13 -> ERKp12 + BRAFp34_RASa_CRAFp134;           kf * ERKp12 * BRAFp34_RASa_CRAFp13
    
    J: ERKp12 + BRAFp34_RASa_CRAFp23 -> ERKp12 + BRAFp134_RASa_CRAFp23;           kf * ERKp12 * BRAFp34_RASa_CRAFp23
    J: ERKp12 + BRAFp34_RASa_CRAFp23 -> ERKp12 + BRAFp34_RASa_CRAFp123;           kf * ERKp12 * BRAFp34_RASa_CRAFp23
    J: ERKp12 + BRAFp34_RASa_CRAFp23 -> ERKp12 + BRAFp34_RASa_CRAFp234;           kf * ERKp12 * BRAFp34_RASa_CRAFp23
    
    J: ERKp12 + BRAFp34_RASa_CRAFp34 -> ERKp12 + BRAFp134_RASa_CRAFp34;           kf * ERKp12 * BRAFp34_RASa_CRAFp34
    J: ERKp12 + BRAFp34_RASa_CRAFp34 -> ERKp12 + BRAFp34_RASa_CRAFp134;           kf * ERKp12 * BRAFp34_RASa_CRAFp34
    J: ERKp12 + BRAFp34_RASa_CRAFp34 -> ERKp12 + BRAFp34_RASa_CRAFp234;           kf * ERKp12 * BRAFp34_RASa_CRAFp34
    
    J: ERKp12 + BRAFp34_RASa_CRAFp123 -> ERKp12 + BRAFp134_RASa_CRAFp123;         kf * ERKp12 * BRAFp34_RASa_CRAFp123
    J: ERKp12 + BRAFp34_RASa_CRAFp123 -> ERKp12 + BRAFp34_RASa_CRAFp1234;         kf * ERKp12 * BRAFp34_RASa_CRAFp123
    
    J: ERKp12 + BRAFp34_RASa_CRAFp134 -> ERKp12 + BRAFp134_RASa_CRAFp134;         kf * ERKp12 * BRAFp34_RASa_CRAFp134
    J: ERKp12 + BRAFp34_RASa_CRAFp134 -> ERKp12 + BRAFp34_RASa_CRAFp1234;         kf * ERKp12 * BRAFp34_RASa_CRAFp134
    
    J: ERKp12 + BRAFp34_RASa_CRAFp234 -> ERKp12 + BRAFp134_RASa_CRAFp234;         kf * ERKp12 * BRAFp34_RASa_CRAFp234
    J: ERKp12 + BRAFp34_RASa_CRAFp234 -> ERKp12 + BRAFp34_RASa_CRAFp1234;         kf * ERKp12 * BRAFp34_RASa_CRAFp234
    
    J: ERKp12 + BRAFp34_RASa_CRAFp1234 -> ERKp12 + BRAFp134_RASa_CRAFp1234;       kf * ERKp12 * BRAFp34_RASa_CRAFp1234
    
    J: ERKp12 + BRAFp134_RASa_CRAFp3 -> ERKp12 + BRAFp134_RASa_CRAFp13;           kf * ERKp12 * BRAFp134_RASa_CRAFp3
    J: ERKp12 + BRAFp134_RASa_CRAFp3 -> ERKp12 + BRAFp134_RASa_CRAFp23;           kf * ERKp12 * BRAFp134_RASa_CRAFp3
    J: ERKp12 + BRAFp134_RASa_CRAFp3 -> ERKp12 + BRAFp134_RASa_CRAFp34;           kf * ERKp12 * BRAFp134_RASa_CRAFp3
    
    J: ERKp12 + BRAFp134_RASa_CRAFp13 -> ERKp12 + BRAFp134_RASa_CRAFp123;         kf * ERKp12 * BRAFp134_RASa_CRAFp13
    J: ERKp12 + BRAFp134_RASa_CRAFp13 -> ERKp12 + BRAFp134_RASa_CRAFp134;         kf * ERKp12 * BRAFp134_RASa_CRAFp13
    
    J: ERKp12 + BRAFp134_RASa_CRAFp23 -> ERKp12 + BRAFp134_RASa_CRAFp123;         kf * ERKp12 * BRAFp134_RASa_CRAFp23
    J: ERKp12 + BRAFp134_RASa_CRAFp23 -> ERKp12 + BRAFp134_RASa_CRAFp234;         kf * ERKp12 * BRAFp134_RASa_CRAFp23
    
    J: ERKp12 + BRAFp134_RASa_CRAFp34 -> ERKp12 + BRAFp134_RASa_CRAFp134;         kf * ERKp12 * BRAFp134_RASa_CRAFp34
    J: ERKp12 + BRAFp134_RASa_CRAFp34 -> ERKp12 + BRAFp134_RASa_CRAFp234;         kf * ERKp12 * BRAFp134_RASa_CRAFp34
    
    J: ERKp12 + BRAFp134_RASa_CRAFp123 -> ERKp12 + BRAFp134_RASa_CRAFp1234;       kf * ERKp12 * BRAFp134_RASa_CRAFp123
    J: ERKp12 + BRAFp134_RASa_CRAFp134 -> ERKp12 + BRAFp134_RASa_CRAFp1234;       kf * ERKp12 * BRAFp134_RASa_CRAFp134
    J: ERKp12 + BRAFp134_RASa_CRAFp234 -> ERKp12 + BRAFp134_RASa_CRAFp1234;       kf * ERKp12 * BRAFp134_RASa_CRAFp234
    
    // --- Dissociation of RAF dimer ---------------------------------------------------------------------------
    // --- Dissociation events for all but the fully phosphorylated BRAF/CRAF dimers are currently commented out
    
    // J: BRAF_RASa_CRAFp13 -> BRAF + RASa + CRAFp13;                  kf * BRAF_RASa_CRAFp13
    // J: BRAF_RASa_CRAFp23 -> BRAF + RASa + CRAFp23;                  kf * BRAF_RASa_CRAFp23
    // J: BRAF_RASa_CRAFp34 -> BRAF + RASa + CRAFp34;                  kf * BRAF_RASa_CRAFp34
    // J: BRAF_RASa_CRAFp123 -> BRAF + RASa + CRAFp123;                kf * BRAF_RASa_CRAFp123
    // J: BRAF_RASa_CRAFp134 -> BRAF + RASa + CRAFp134;                kf * BRAF_RASa_CRAFp134
    // J: BRAF_RASa_CRAFp234 -> BRAF + RASa + CRAFp234;                kf * BRAF_RASa_CRAFp234
    // J: BRAF_RASa_CRAFp1234 -> BRAF + RASa + CRAFp1234;              kf * BRAF_RASa_CRAFp1234
    
    // J: BRAFp1_RASa_CRAFp3 -> BRAFp1 + RASa + CRAFp3;                kf * BRAFp1_RASa_CRAFp3
    // J: BRAFp1_RASa_CRAFp13 -> BRAFp1 + RASa + CRAFp13;              kf * BRAFp1_RASa_CRAFp13
    // J: BRAFp1_RASa_CRAFp23 -> BRAFp1 + RASa + CRAFp23;              kf * BRAFp1_RASa_CRAFp23
    // J: BRAFp1_RASa_CRAFp34 -> BRAFp1 + RASa + CRAFp34;              kf * BRAFp1_RASa_CRAFp34
    // J: BRAFp1_RASa_CRAFp123 -> BRAFp1 + RASa + CRAFp123;            kf * BRAFp1_RASa_CRAFp123
    // J: BRAFp1_RASa_CRAFp134 -> BRAFp1 + RASa + CRAFp134;            kf * BRAFp1_RASa_CRAFp134
    // J: BRAFp1_RASa_CRAFp234 -> BRAFp1 + RASa + CRAFp234;            kf * BRAFp1_RASa_CRAFp234
    // J: BRAFp1_RASa_CRAFp1234 -> BRAFp1 + RASa + CRAFp1234;          kf * BRAFp1_RASa_CRAFp1234
    
    // J: BRAFp3_RASa_CRAFp3 -> BRAFp3 + RASa + CRAFp3;                kf * BRAFp3_RASa_CRAFp3
    // J: BRAFp3_RASa_CRAFp13 -> BRAFp3 + RASa + CRAFp13;              kf * BRAFp3_RASa_CRAFp13
    // J: BRAFp3_RASa_CRAFp23 -> BRAFp3 + RASa + CRAFp23;              kf * BRAFp3_RASa_CRAFp23
    // J: BRAFp3_RASa_CRAFp34 -> BRAFp3 + RASa + CRAFp34;              kf * BRAFp3_RASa_CRAFp34
    // J: BRAFp3_RASa_CRAFp123 -> BRAFp3 + RASa + CRAFp123;            kf * BRAFp3_RASa_CRAFp123
    // J: BRAFp3_RASa_CRAFp134 -> BRAFp3 + RASa + CRAFp134;            kf * BRAFp3_RASa_CRAFp134
    // J: BRAFp3_RASa_CRAFp234 -> BRAFp3 + RASa + CRAFp234;            kf * BRAFp3_RASa_CRAFp234
    // J: BRAFp3_RASa_CRAFp1234 -> BRAFp3 + RASa + CRAFp1234;          kf * BRAFp3_RASa_CRAFp1234
    
    // J: BRAFp4_RASa_CRAFp3 -> BRAFp4 + RASa + CRAFp3;                kf * BRAFp4_RASa_CRAFp3
    // J: BRAFp4_RASa_CRAFp13 -> BRAFp4 + RASa + CRAFp13;              kf * BRAFp4_RASa_CRAFp13
    // J: BRAFp4_RASa_CRAFp23 -> BRAFp4 + RASa + CRAFp23;              kf * BRAFp4_RASa_CRAFp23
    // J: BRAFp4_RASa_CRAFp34 -> BRAFp4 + RASa + CRAFp34;              kf * BRAFp4_RASa_CRAFp34
    // J: BRAFp4_RASa_CRAFp123 -> BRAFp4 + RASa + CRAFp123;            kf * BRAFp4_RASa_CRAFp123
    // J: BRAFp4_RASa_CRAFp134 -> BRAFp4 + RASa + CRAFp134;            kf * BRAFp4_RASa_CRAFp134
    // J: BRAFp4_RASa_CRAFp234 -> BRAFp4 + RASa + CRAFp234;            kf * BRAFp4_RASa_CRAFp234
    // J: BRAFp4_RASa_CRAFp1234 -> BRAFp4 + RASa + CRAFp1234;          kf * BRAFp4_RASa_CRAFp1234
    
    // J: BRAFp13_RASa_CRAFp3 -> BRAFp13 + RASa + CRAFp3;              kf * BRAFp13_RASa_CRAFp3
    // J: BRAFp13_RASa_CRAFp13 -> BRAFp13 + RASa + CRAFp13;            kf * BRAFp13_RASa_CRAFp13
    // J: BRAFp13_RASa_CRAFp23 -> BRAFp13 + RASa + CRAFp23;            kf * BRAFp13_RASa_CRAFp23
    // J: BRAFp13_RASa_CRAFp34 -> BRAFp13 + RASa + CRAFp34;            kf * BRAFp13_RASa_CRAFp34
    // J: BRAFp13_RASa_CRAFp123 -> BRAFp13 + RASa + CRAFp123;          kf * BRAFp13_RASa_CRAFp123
    // J: BRAFp13_RASa_CRAFp134 -> BRAFp13 + RASa + CRAFp134;          kf * BRAFp13_RASa_CRAFp134
    // J: BRAFp13_RASa_CRAFp234 -> BRAFp13 + RASa + CRAFp234;          kf * BRAFp13_RASa_CRAFp234
    // J: BRAFp13_RASa_CRAFp1234 -> BRAFp13 + RASa + CRAFp1234;        kf * BRAFp13_RASa_CRAFp1234
    
    // J: BRAFp14_RASa_CRAFp3 -> BRAFp14 + RASa + CRAFp3;              kf * BRAFp14_RASa_CRAFp3
    // J: BRAFp14_RASa_CRAFp13 -> BRAFp14 + RASa + CRAFp13;            kf * BRAFp14_RASa_CRAFp13
    // J: BRAFp14_RASa_CRAFp23 -> BRAFp14 + RASa + CRAFp23;            kf * BRAFp14_RASa_CRAFp23
    // J: BRAFp14_RASa_CRAFp34 -> BRAFp14 + RASa + CRAFp34;            kf * BRAFp14_RASa_CRAFp34
    // J: BRAFp14_RASa_CRAFp123 -> BRAFp14 + RASa + CRAFp123;          kf * BRAFp14_RASa_CRAFp123
    // J: BRAFp14_RASa_CRAFp134 -> BRAFp14 + RASa + CRAFp134;          kf * BRAFp14_RASa_CRAFp134
    // J: BRAFp14_RASa_CRAFp234 -> BRAFp14 + RASa + CRAFp234;          kf * BRAFp14_RASa_CRAFp234
    // J: BRAFp14_RASa_CRAFp1234 -> BRAFp14 + RASa + CRAFp1234;        kf * BRAFp14_RASa_CRAFp1234
    
    // J: BRAFp34_RASa_CRAFp3 -> BRAFp34 + RASa + CRAFp3;              kf * BRAFp34_RASa_CRAFp3
    // J: BRAFp34_RASa_CRAFp13 -> BRAFp34 + RASa + CRAFp13;            kf * BRAFp34_RASa_CRAFp13
    // J: BRAFp34_RASa_CRAFp23 -> BRAFp34 + RASa + CRAFp23;            kf * BRAFp34_RASa_CRAFp23
    // J: BRAFp34_RASa_CRAFp34 -> BRAFp34 + RASa + CRAFp34;            kf * BRAFp34_RASa_CRAFp34
    // J: BRAFp34_RASa_CRAFp123 -> BRAFp34 + RASa + CRAFp123;          kf * BRAFp34_RASa_CRAFp123
    // J: BRAFp34_RASa_CRAFp134 -> BRAFp34 + RASa + CRAFp134;          kf * BRAFp34_RASa_CRAFp134
    // J: BRAFp34_RASa_CRAFp234 -> BRAFp34 + RASa + CRAFp234;          kf * BRAFp34_RASa_CRAFp234
    // J: BRAFp34_RASa_CRAFp1234 -> BRAFp34 + RASa + CRAFp1234;        kf * BRAFp34_RASa_CRAFp1234
    
    // J: BRAFp134_RASa_CRAFp3 -> BRAFp134 + RASa + CRAFp3;            kf * BRAFp134_RASa_CRAFp3
    // J: BRAFp134_RASa_CRAFp13 -> BRAFp134 + RASa + CRAFp13;          kf * BRAFp134_RASa_CRAFp13
    // J: BRAFp134_RASa_CRAFp23 -> BRAFp134 + RASa + CRAFp23;          kf * BRAFp134_RASa_CRAFp23
    // J: BRAFp134_RASa_CRAFp34 -> BRAFp134 + RASa + CRAFp34;          kf * BRAFp134_RASa_CRAFp34
    // J: BRAFp134_RASa_CRAFp123 -> BRAFp134 + RASa + CRAFp123;        kf * BRAFp134_RASa_CRAFp123
    // J: BRAFp134_RASa_CRAFp134 -> BRAFp134 + RASa + CRAFp134;        kf * BRAFp134_RASa_CRAFp134
    // J: BRAFp134_RASa_CRAFp234 -> BRAFp134 + RASa + CRAFp234;        kf * BRAFp134_RASa_CRAFp234
    
    J: BRAFp134_RASa_CRAFp1234 -> BRAFp134 + RASa + CRAFp1234;      kf * BRAFp134_RASa_CRAFp1234
    
    // --- (De)phosphorylation events returning ARAF, BRAF and CRAF to original state -----------
    
    J: ARAFp13 -> ARAFp1;       kf * ARAFp13
    J: ARAFp13 -> ARAFp3;       kf * ARAFp13
    J: ARAFp1 -> ARAF;          kf * ARAFp1
    J: ARAFp3 -> ARAF;          kf * ARAFp3
    
    J: ARAF -> ARAFp2;          kf * ARAF
    
    J: BRAFp134 -> BRAFp34;     kf * BRAFp134
    J: BRAFp134 -> BRAFp14;     kf * BRAFp134
    J: BRAFp134 -> BRAFp13;     kf * BRAFp134
    J: BRAFp34 -> BRAFp4;       kf * BRAFp34
    J: BRAFp34 -> BRAFp3;       kf * BRAFp34
    J: BRAFp14 -> BRAFp1;       kf * BRAFp14
    J: BRAFp14 -> BRAFp4;       kf * BRAFp14
    J: BRAFp13 -> BRAFp1;       kf * BRAFp13
    J: BRAFp13 -> BRAFp3;       kf * BRAFp13
    J: BRAFp1 -> BRAF;          kf * BRAFp1
    J: BRAFp3 -> BRAF;          kf * BRAFp3
    J: BRAFp4 -> BRAF;          kf * BRAFp4
    
    J: BRAF -> BRAFp2;          kf * BRAF
    
    J: CRAFp1234 -> CRAFp234;   kf * CRAFp1234
    J: CRAFp1234 -> CRAFp134;   kf * CRAFp1234
    J: CRAFp1234 -> CRAFp124;   kf * CRAFp1234
    J: CRAFp1234 -> CRAFp123;   kf * CRAFp1234
    J: CRAFp234 -> CRAFp34;     kf * CRAFp234
    J: CRAFp234 -> CRAFp24;     kf * CRAFp234
    J: CRAFp234 -> CRAFp23;     kf * CRAFp234
    J: CRAFp134 -> CRAFp34;     kf * CRAFp134
    J: CRAFp134 -> CRAFp14;     kf * CRAFp134
    J: CRAFp134 -> CRAFp13;     kf * CRAFp134
    J: CRAFp124 -> CRAFp24;     kf * CRAFp124
    J: CRAFp124 -> CRAFp14;     kf * CRAFp124
    J: CRAFp124 -> CRAFp12;     kf * CRAFp124
    J: CRAFp123 -> CRAFp23;     kf * CRAFp123
    J: CRAFp123 -> CRAFp13;     kf * CRAFp123
    J: CRAFp123 -> CRAFp12;     kf * CRAFp123
    J: CRAFp12 -> CRAFp2;       kf * CRAFp12
    J: CRAFp12 -> CRAFp1;       kf * CRAFp12
    J: CRAFp13 -> CRAFp3;       kf * CRAFp13
    J: CRAFp13 -> CRAFp1;       kf * CRAFp13
    J: CRAFp14 -> CRAFp4;       kf * CRAFp14
    J: CRAFp14 -> CRAFp1;       kf * CRAFp14
    J: CRAFp23 -> CRAFp3;       kf * CRAFp23
    J: CRAFp23 -> CRAFp2;       kf * CRAFp23
    J: CRAFp24 -> CRAFp4;       kf * CRAFp24
    J: CRAFp24 -> CRAFp2;       kf * CRAFp24
    J: CRAFp34 -> CRAFp4;       kf * CRAFp34
    J: CRAFp34 -> CRAFp3;       kf * CRAFp34
    J: CRAFp1 -> CRAF;          kf * CRAFp1
    J: CRAFp2 -> CRAF;          kf * CRAFp2
    J: CRAFp3 -> CRAF;          kf * CRAFp3
    J: CRAFp4 -> CRAF;          kf * CRAFp4
    
    // --- Activation of MEK1/MEK2 --------
    
    J: BRAF_RASa_CRAFp3 + MEK1 -> BRAF_RASa_CRAFp3 + MEK1p1;        kf * BRAF_RASa_CRAFp3 * MEK1 - kr * MEK1p1
    J: BRAF_RASa_CRAFp3 + MEK2 -> BRAF_RASa_CRAFp3 + MEK2p1;        kf * BRAF_RASa_CRAFp3 * MEK2 - kr * MEK2p1
    J: BRAF_RASa_CRAFp3 + MEK2 -> BRAF_RASa_CRAFp3 + MEK2p2;        kf * BRAF_RASa_CRAFp3 * MEK2 - kr * MEK2p2
    J: BRAF_RASa_CRAFp3 + MEK2p1 -> BRAF_RASa_CRAFp3 + MEK2p12;     kf * BRAF_RASa_CRAFp3 * MEK2p1 - kr * MEK2p12
    J: BRAF_RASa_CRAFp3 + MEK2p2 -> BRAF_RASa_CRAFp3 + MEK2p12;     kf * BRAF_RASa_CRAFp3 * MEK2p2 - kr * MEK2p12
    
    J: BRAF_RASa_ARAFp13 + MEK1 -> BRAF_RASa_CRAFp3 + MEK1p1;        kf * BRAF_RASa_CRAFp3 * MEK1 - kr * MEK1p1
    J: BRAF_RASa_ARAFp13 + MEK2 -> BRAF_RASa_CRAFp3 + MEK2p1;        kf * BRAF_RASa_CRAFp3 * MEK2 - kr * MEK2p1
    J: BRAF_RASa_ARAFp13 + MEK2 -> BRAF_RASa_CRAFp3 + MEK2p2;        kf * BRAF_RASa_CRAFp3 * MEK2 - kr * MEK2p2
    J: BRAF_RASa_ARAFp13 + MEK2p1 -> BRAF_RASa_CRAFp3 + MEK2p12;     kf * BRAF_RASa_CRAFp3 * MEK2p1 - kr * MEK2p12
    J: BRAF_RASa_ARAFp13 + MEK2p2 -> BRAF_RASa_CRAFp3 + MEK2p12;     kf * BRAF_RASa_CRAFp3 * MEK2p2 - kr * MEK2p12
    
    J: ERKp12 + MEK1 -> ERKp12 + MEK1p1;                            kf * ERKp12 * MEK1 - kr * MEK1p1
    
    // --- Activation of ERK -----------------------------------------------------------------------
    
    J: MEK1p1 + ERK -> MEKp1 + ERKp1;               kf * MEK1p1 + ERK - kr * ERKp1
    J: MEK1p1 + ERK -> MEKp1 + ERKp2;               kf * MEK1p1 + ERK - kr * ERKp2
    J: MEK1p1 + ERKp1 -> MEKp1 + ERKp12;            kf * MEK1p1 + ERKp1 - kr * ERKp12
    J: MEK1p1 + ERKp2 -> MEKp1 + ERKp12;            kf * MEK1p1 + ERKp2 - kr * ERKp12
    
    J: MEK2p12 + ERK -> MEKp1 + ERKp1;              kf * MEK2p12 + ERK - kr * ERKp1
    J: MEK2p12 + ERK -> MEKp1 + ERKp2;              kf * MEK2p12 + ERK - kr * ERKp2
    J: MEK2p12 + ERKp1 -> MEKp1 + ERKp12;           kf * MEK2p12 + ERKp1 - kr * ERKp12
    J: MEK2p12 + ERKp2 -> MEKp1 + ERKp12;           kf * MEK2p12 + ERKp2 - kr * ERKp12
    
    // J: MEK1p1 + ERK1 -> MEKp1 + ERK1p1;             kf * MEK1p1 + ERK1 - kr * ERK1p1
    // J: MEK1p1 + ERK1 -> MEKp1 + ERK1p2;             kf * MEK1p1 + ERK1 - kr * ERK1p2
    // J: MEK1p1 + ERK1p1 -> MEKp1 + ERK1p12;          kf * MEK1p1 + ERK1p1 - kr * ERK1p12
    // J: MEK1p1 + ERK1p2 -> MEKp1 + ERK1p12;          kf * MEK1p1 + ERK1p2 - kr * ERK1p12
    
    // J: MEK2p12 + ERK1 -> MEKp1 + ERK1p1;            kf * MEK2p12 + ERK1 - kr * ERK1p1
    // J: MEK2p12 + ERK1 -> MEKp1 + ERK1p2;            kf * MEK2p12 + ERK1 - kr * ERK1p2
    // J: MEK2p12 + ERK1p1 -> MEKp1 + ERK1p12;         kf * MEK2p12 + ERK1p1 - kr * ERK1p12
    // J: MEK2p12 + ERK1p2 -> MEKp1 + ERK1p12;         kf * MEK2p12 + ERK1p2 - kr * ERK1p12
    
    // J: MEK1p1 + ERK2 -> MEKp1 + ERK2p1;             kf * MEK1p1 + ERK2 - kr * ERK2p1
    // J: MEK1p1 + ERK2 -> MEKp1 + ERK2p2;             kf * MEK1p1 + ERK2 - kr * ERK2p2
    // J: MEK1p1 + ERK2p1 -> MEKp1 + ERK2p12;          kf * MEK1p1 + ERK2p1 - kr * ERK2p12
    // J: MEK1p1 + ERK2p2 -> MEKp1 + ERK2p12;          kf * MEK1p1 + ERK2p2 - kr * ERK2p12
    
    // J: MEK2p12 + ERK2 -> MEKp1 + ERK2p1;            kf * MEK2p12 + ERK2 - kr * ERK2p1
    // J: MEK2p12 + ERK2 -> MEKp1 + ERK2p2;            kf * MEK2p12 + ERK2 - kr * ERK2p2
    // J: MEK2p12 + ERK2p1 -> MEKp1 + ERK2p12;         kf * MEK2p12 + ERK2p1 - kr * ERK2p12
    // J: MEK2p12 + ERK2p2 -> MEKp1 + ERK2p12;         kf * MEK2p12 + ERK2p2 - kr * ERK2p12
    
    // --- Activation of RSK --------------------------------------------------------------
    
    J: ERKp12 + RSK -> ERKp12 + RSKp1;          kf * ERKp12 * RSK - kr * RSKp1
    J: ERKp12 + RSK -> ERKp12 + RSKp2;          kf * ERKp12 * RSK - kr * RSKp2
    J: ERKp12 + RSK -> ERKp12 + RSKp3;          kf * ERKp12 * RSK - kr * RSKp3
    
    J: ERKp12 + RSKp1 -> ERKp12 + RSKp12;       kf * ERKp12 * RSKp1 - kr * RSKp12
    J: ERKp12 + RSKp1 -> ERKp12 + RSKp13;       kf * ERKp12 * RSKp1 - kr * RSKp13
    
    J: ERKp12 + RSKp2 -> ERKp12 + RSKp12;       kf * ERKp12 * RSKp2 - kr * RSKp12
    J: ERKp12 + RSKp2 -> ERKp12 + RSKp23;       kf * ERKp12 * RSKp2 - kr * RSKp23
    
    J: ERKp12 + RSKp3 -> ERKp12 + RSKp13;       kf * ERKp12 * RSKp3 - kr * RSKp13
    J: ERKp12 + RSKp3 -> ERKp12 + RSKp23;       kf * ERKp12 * RSKp3 - kr * RSKp23
    
    J: ERKp12 + RSKp12 -> ERKp12 + RSKp123;     kf * ERKp12 * RSKp12 - kr * RSKp123
    J: ERKp12 + RSKp13 -> ERKp12 + RSKp123;     kf * ERKp12 * RSKp13 - kr * RSKp123
    J: ERKp12 + RSKp23 -> ERKp12 + RSKp123;     kf * ERKp12 * RSKp23 - kr * RSKp123
    
    // --- ERK activation of IROHM2 and ADAM17 of RSK --------------------------------
    
    J: ERKp12 + IRHOM2 -> ERKp12 + IRHOM2p1;      kf * ERKp12 * IROHM2 - kr * IROHM2p1
    J: ERKp12 + IRHOM2 -> ERKp12 + IRHOM2p2;      kf * ERKp12 * IROHM2 - kr * IROHM2p2
    J: ERKp12 + IRHOM2p1 -> ERKp12 + IRHOM2p12;      kf * ERKp12 * IROHM2p1 - kr * IROHM2p12
    J: ERKp12 + IRHOM2p2 -> ERKp12 + IRHOM2p12;      kf * ERKp12 * IROHM2p2 - kr * IROHM2p12
    
    J: ERKp12 + ADAM17 -> ERKp12 + ADAM17p1;      kf * ERKp12 * ADAM17 - kr * ADAM17p1
    
    J: IROHM2p12 + ADAM17p1 -> IROHM2p12_ADAM17p1;      kf * IROHM2p12 * ADAM17p1 - kr * IROHM2p12_ADAM17p1
    
    // === PARAMETERS ===
    
    // === SPECIES ===
    

''')
