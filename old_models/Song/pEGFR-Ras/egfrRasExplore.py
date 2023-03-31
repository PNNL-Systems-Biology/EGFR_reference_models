# This script is for simulating egfrRas.sb with different parameters
import os
import sys
import matplotlib.pyplot as plt

import numpy as np
import scipy as sp
import pandas as pd
import seaborn as sn


import tellurium as te


with open("egfrRas.sb") as f:
    egfrRasModel = f.read()

egfrRas = te.loada(egfrRasModel)
egfrRas.reset()
egfrRasSim = egfrRas.simulate(0, 50000, 501)

egfrRas.plot()
