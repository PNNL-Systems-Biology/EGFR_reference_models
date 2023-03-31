import os
import sys
import matplotlib.pyplot as plt

import numpy as np
import scipy as sp
import pandas as pd
import seaborn as sn


import tellurium as te


with open("sheddingTgfa.sb") as f:
    sheddingTgfaModel = f.read()

sheddingTgfa = te.loada(sheddingTgfaModel)
species = sheddingTgfa.getFloatingSpeciesIds()

sheddingTgfa.reset()
# equilibrium
sheddingTgfa.ppErk = 0.0
tgfaEq = sheddingTgfa.simulate(0, 500000, 501)
# sheddingTgfa.plot(yscale="log", ylim=[0.000001, 100])
# sheddingTgfa.plot()
# fig0 = te.plot(tgfaEq[:, 0],
#                tgfaEq[:, 1:10], names=species[0:9])
fig00 = te.plot(tgfaEq[:, 0],
                tgfaEq[:, 1:5], names=species[0:4])
fig01 = te.plot(tgfaEq[:, 0],
                tgfaEq[:, 5:10], names=species[4:9])
# figTest = te.plot(tgfaEq[:, 0],
#                   tgfaEq[:, 5:11], names=species[4:10])
# figTest2 = te.plot(tgfaEq[:, 0],
#                    tgfaEq[:, -3:-1], names=species[-3:-1])


# adding TGFalpha
sheddingTgfa.ppErk = 7.5
tgfaPerturbBasal = sheddingTgfa.simulate(0, 2000, 501)
# sheddingTgfa.plot(tgfaPerturbBasal, figsize=(20, 10),
#                   yscale="log", ylim=[0.0001, 100])
# fig1 = te.plot(tgfaPerturbBasal[:, 0],
#                tgfaPerturbBasal[:, 1:10], names=species[0:9])
fig10 = te.plot(tgfaPerturbBasal[:, 0],
                tgfaPerturbBasal[:, 1:5], names=species[0:4])
fig11 = te.plot(tgfaPerturbBasal[:, 0],
                tgfaPerturbBasal[:, 5:10], names=species[4:9])

# fig20 = te.plot(tgfaPerturbBasal[:, 0],
#                 tgfaPerturbBasal[:, 1] * sheddingTgfa.extra, names=species[0])


# te.plot(tgfaPerturbBasal[:, 0],
#         tgfaPerturbBasal[:, 1] * sheddingTgfa.extra, names=species[0])
# te.plot(tgfaPerturbBasal[:, 0],
#         tgfaPerturbBasal[:, 2] * sheddingTgfa.pool, names=species[1])


sheddingTgfa.reset()
# equilibrium
sheddingTgfa.ppErk = 0.0
sheddingTgfa.simulate(0, 50000, 501)
# sheddingTgfa.plot(figsize=(20, 10))  # , yscale="log", ylim=[0.0001, 100000])
# adding TGFalpha
sheddingTgfa.ppErk = 150
tgfaPerturbMax = sheddingTgfa.simulate(0, 2000, 501)
# sheddingTgfa.plot(tgfaPerturbMax, figsize=(20, 10),
#                   yscale="log", ylim=[0.0001, 100])
# fig2 = te.plot(tgfaPerturbMax[:, 0],
#                tgfaPerturbMax[:, 1:10], names=species[0:9])
fig20 = te.plot(tgfaPerturbMax[:, 0],
                tgfaPerturbMax[:, 1:5], names=species[0:4])
fig21 = te.plot(tgfaPerturbMax[:, 0],
                tgfaPerturbMax[:, 5:10], names=species[4:9])

# te.plot(tgfaPerturbMax[:, 0],
#         tgfaPerturbMax[:, 1] * sheddingTgfa.extra, names=species[1])
# te.plot(tgfaPerturbMax[:, 0],
#         tgfaPerturbMax[:, 2] * sheddingTgfa.pool, names=species[2])
