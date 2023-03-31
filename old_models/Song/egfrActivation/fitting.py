import roadrunner
import tellurium as te
from multiprocessing import Pool
import seaborn as sn
import pandas as pd
import scipy as sp
import numpy as np
import csv
import operator
import random
from datetime import datetime
import matplotlib.pyplot as plt
import sys
import os
import warnings
warnings.filterwarnings("ignore")
roadrunner.Logger_disableConsoleLogging()
# roadrunner.Logger_enableConsoleLogging(3)

# import ray#, psutil
directory = sys.argv[2]
tag = sys.argv[1]

with open(directory + "egfrActivation.sb") as f:
    egfrActivationModel = f.read()

model = te.loada(egfrActivationModel)
species = model.getFloatingSpeciesIds()
# model.reset()

egf = np.array([0.2, 0.4, 1.0, 2.5, 5.0, 10.0, 20.0, 100.0])
pegfr = np.array([[1.538, 1.639, 2.355, 1.899, 1.935, 1.790, 1.700, 0.781, 3.072],
                  [2.244, 1.943, 1.395, 1.749, 2.028, 2.039, 2.087, 1.108, 2.858],
                  [1.501, 2.935, 4.037, 5.768, 5.986, 7.527, 6.889, 7.812, 7.490],
                  [2.899, 9.543, 13.878, 18.940, 23.153,
                      27.694, 28.414, 34.901, 37.434],
                  [2.504, 13.263, 21.242, 31.053, 34.163,
                      37.691, 36.178, 47.017, 46.832],
                  [2.642, 12.110, 15.855, 28.133, 30.337,
                      29.640, 32.854, 31.818, 44.066],
                  [2.069, 18.130, 13.089, 24.388, 29.611,
                      36.226, 32.383, 37.782, 38.338],
                  [1.568, 20.861, 38.950, 38.886, 32.507, 32.372, 31.802, 30.657, 38.321]])

pegfrStd = np.array([[2.761, 2.510, 9.424, 4.139, 1.454, 5.456, 1.043, 1.674, 8.531],
                     [4.239, 5.368, 1.994, 3.809, 4.753,
                         7.857, 5.321, 7.262, 4.618],
                     [4.415, 4.692, 5.833, 5.214, 3.451,
                         14.933, 8.317, 4.091, 3.002],
                     [1.869, 4.165, 1.246, 6.793, 6.874,
                      10.611, 2.438, 14.655, 6.646],
                     [2.525, 6.282, 6.638, 7.443, 13.619,
                      3.516, 0.467, 7.783, 8.021],
                     [1.762, 2.914, 4.555, 11.463, 11.264,
                      23.662, 6.728, 13.159, 10.555],
                     [2.248, 5.310, 19.831, 4.977, 2.508,
                      7.178, 7.023, 5.578, 6.136],
                     [0.839, 7.993, 2.607, 6.204, 7.905, 11.694, 5.722, 2.411, 5.365]])


t0 = 0
teq = 5000
tf = 80
tnum = pegfr.shape[1]
egfLevels = len(egf)
tsnum = pegfr.shape[1] * 100

lowB = -5
highB = 5
parNum = 16


def getResidual(pars, model=model):
    model = setParameter(model, pars)
    residual = 1
    for i in range(egfLevels - 1):
        tempSc = 10 ** 12
        model.reset()
        model.E = 0
        try:
            model.simulate(t0, teq, tnum)
            model.E = egf[i]
            eq = model.simulate(t0, tf, tnum)
            tempSc = np.sqrt(np.sum((((eq["[RRp]"] + eq["[RRpE]"] + eq["[ERRpE]"] + 2 * (
                eq["[RpRp]"] + eq["[RpRpE]"] + eq["[ERpRpE]"])) - pegfr[i])/(pegfrStd[i]))**2) / tnum)
        except:
            tempSc = 10 ** 12

        residual *= tempSc
    residual **= 1/egfLevels

    return residual

# def getObs(model, pars):


def setParameter(model, pars):
    # model.Vr = pars[0]
    model.kf1 = pars[1]
    model.kf2 = pars[2]
    # model.ki = pars[3]
    # model.ke = pars[4]
    model.kp = pars[5]
    model.kd = pars[6]
    model.K1 = pars[7]
    model.K2 = pars[8]
    model.g1 = pars[9]
    model.g2 = pars[10]
    model.g3 = pars[11]
    model.g4 = pars[12]
    model.g5 = pars[13]
    model.g6 = pars[14]
    model.g7 = pars[15]
    return model


def getTempLin(lin, prob, scaler):
    dims = lin.shape
    tempLin = []
    for i in range(dims[0]):
        tempi = []
        randi = random.randrange(dims[1])
        choices = random.sample(range(dims[0]), 3)
        while i in choices:
            choices = random.sample(range(dims[0]), 3)
        for j in range(dims[1]):
            if random.random() < prob or j == randi:
                newPar = lin[choices[0], j] + scaler * \
                    (lin[choices[1], j] - lin[choices[2], j])
                if newPar < lowB or newPar > highB:
                    newPar = random.uniform(lowB, highB)
                tempi.append(newPar)
            else:
                tempi.append(lin[i, j])
        tempLin.append(tempi)
    return(np.array(tempLin))


#pool = Pool(processes=4)

# pool.close()

gen = 0
batchsize = 24
genNum = 1000000
epoch = 10000
interval = 1000
scaling = 0.9
error = 1.0e32
threshold = 0.1
trackfile = directory + "sims/trackingAll-" + tag + ".csv"
moniterfile = directory + "sims/monitorAll-" + tag + ".csv"

lineages = []
for i in range(batchsize):
    iLin3 = np.random.uniform(lowB, highB, parNum)
    lineages.append(iLin3)
lineages = np.array(lineages)

scores = [getResidual(10 ** iLin) for iLin in lineages]

count = 0
while gen <= genNum or error > threshold:
    crossProb = 0.25 * (2 - random.random())
    tempLin = getTempLin(lineages, crossProb, scaling)
    tempScores = [getResidual(10 ** iLin) for iLin in tempLin]

    for i in range(batchsize):
        if tempScores[i] < scores[i]:
            scores[i] = tempScores[i]
            lineages[i] = tempLin[i]
            count += 1
    bestindex, bestfit = min(enumerate(scores), key=operator.itemgetter(1))

    if bestfit < error:
        error = bestfit
        with open(trackfile, 'a') as output:
            writer = csv.writer(output)
            writer.writerow([gen, bestfit] + lineages[bestindex].tolist())
    if gen % interval == 0:
        with open(moniterfile, 'a') as output:
            writer = csv.writer(output)
            writer.writerow([str(datetime.now()), gen, bestfit, np.mean(
                scores), count, np.amin(tempScores), np.mean(tempScores)])
        count = 0

    gen += 1
