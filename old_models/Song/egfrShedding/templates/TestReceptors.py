import tellurium as te

with open('endocytosis+Signal_V1.sb') as f:
    antstr = f.read()
model = te.loada(antstr)
initialR = model.R
model.E = 3
model.simulate(0, 720, 200, selections=['time', 'ppErk', 'Raf', 'aRaf', 'tRas', 'aaRaf'])
# model.simulate(0, 720, 200, selections=['time', 'SOSp', 'SOS', 'GS', 'Rp_GS'])
model.plot()
print('Initial EGF: {:0.2f}'.format(model.E))
print('Total occupied receptors at end: {:.2f}'.format(model.RE+model.Rd+model.Rp))
print('Total active EGFR at end: {:.2f}'.format(model.Rp))
print('Total Receptor-GS-Shc at end: {:.2f}'.format(model.Rp_pShc_GS))
print('Total Receptor-GC at end: {:.2f}'.format(model.Rp_GS))
print('Total aRas at end: {:.2f}'.format(model.tRas))
print('Total ppErk at end: {:.2f}'.format(model.ppErk))