import tellurium as te
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')

r = te.loada ('''
      MAPKKK -> MAPKKK_P; (V_1 + Sig)*MAPKKK/((Km_1 + MAPKKK)*(1 + MAPK_PP/Ki))
      MAPKKK_P -> MAPKKK; V_2*MAPKKK_P/(Km_2 + MAPKKK_P)
     
      MAPKK -> MAPKK_P;  V_3*MAPKK*MAPKKK_P/(Km_3 + MAPKK)
      MAPKK_P -> MAPKK;  V_4*MAPKK_P/(Km_6 + MAPKK_P)
      MAPKK_P -> MAPKK_PP;  V_5*MAPKK_P*MAPKKK_P/(Km_5+MAPKK_P)      
      MAPKK_PP -> MAPKK_P;  V_6*MAPKK_PP/(Km_4 + MAPKK_PP)
     
      MAPK -> MAPK_P;    V_7*MAPK*MAPKK_PP/(Km_7 + MAPK)
      MAPK_P -> MAPK;    V_8*MAPK_P/(Km_10 + MAPK_P)
      MAPK_P -> MAPK_PP; V_9*MAPK_P*MAPKK_PP/(Km_8 + MAPK_P)      
      MAPK_PP -> MAPK_P; V_10*MAPK_PP/(Km_9 + MAPK_PP)
             
      Km_1 = 10;   Km_2 = 8; Km_3 = 15; Km_4 = 15; Km_5 = 15
      Km_6 = 15;   Km_7 = 15; Km_8 = 15; Km_9 =15; Km_10 = 5
      V_1 = 2.5;   V_2 = 5.1; V_3 = 0.025; V_4 = 0.75
      V_5 = 0.025; V_6 = 0.75; V_7 = 0.025; V_8 = 0.5
      V_9 = 0.025; V_10 = 0.5;
     
      T_1 = 100; T_2=300; T_3 = 300    
     
      Sig = 0.3; Ki = 10000
     
      MAPKKK = 100
      MAPKK = 300
      MAPK = 200
             
''')

m = r.simulate (0, 20, 100)
r.plot()

r.steadyState()

steps = 160

r.Sig = 0.3
x = []; y1 = []
for i in range (steps):
    r.steadyState()
    x.append (r.Sig)
    y1.append (r.MAPK_PP)
    print (r.MAPK_PP)
    r.Sig = r.Sig + 0.04
plt.plot (x, y1)

r.Ki = 550
r.Sig = 0.3
x = []; y2 = []
for i in range (steps):
    r.simulate (0, 100, 20)
    r.steadyState()
    x.append (r.Sig)
    y2.append (r.MAPK_PP)
    #print (r.MAPK_PP)
    r.Sig = r.Sig + 0.04
plt.plot (x, y2)

r.Ki = 200
r.Sig = 0.3
x = []; y3 = []
for i in range (steps):
    r.simulate (0, 100, 20)
    r.steadyState()
    x.append (r.Sig)
    y3.append (r.MAPK_PP)
    #print (r.MAPK_PP, r.Sig)
    r.Sig = r.Sig + 0.04
plt.plot (x, y1)
plt.plot (x, y2)
plt.plot (x, y3)
