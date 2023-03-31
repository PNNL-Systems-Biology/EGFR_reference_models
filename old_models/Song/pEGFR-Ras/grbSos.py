# This script is for simulating egfrRas.sb with different parameters
import os
import sys
import matplotlib.pyplot as plt

import numpy as np
import scipy as sp
import pandas as pd
import seaborn as sn


import tellurium as te


with open("GrbSos.sb") as f:
    grbSosModel = f.read()

grbSos = te.loada(grbSosModel)
grbSos.reset()
grbSosSim = grbSos.simulate(0, 500, 51)
# grbSos.plot()
grbSos.Rp = 100
grbSosSim = grbSos.simulate(0, 500, 101, selections=['time', 'tRas'])
# grbSos.plot()
