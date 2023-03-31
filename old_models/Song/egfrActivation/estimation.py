import os
import sys
import matplotlib.pyplot as plt

import numpy as np
import scipy as sp
import pandas as pd
import seaborn as sn


import tellurium as te

with open("egfrActivation.sb") as f:
    egfrActivationModel = f.read()

model = te.loada(egfrActivationModel)

model.reset()
