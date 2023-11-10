import numpy as np

def readFile(name):
    return np.loadtxt(name, delimiter=";", dtype=float)

def getAveragePrirityValue(matrix):
    W = {}
    for i, row in enumerate(matrix):
        mul = 1
        for j, value in enumerate(matrix[i]):
            mul *= matrix[i][j]
        W[i] = mul ** (1. / len(matrix[i]))
    return W

def getNormalizeVec(W):
    Wnormalize = {}
    _sum = 0
    for value in W:
        _sum += value
    for index, row in enumerate(W):
        Wnormalize[index] = W[index] / _sum
    return Wnormalize

def getMO(MergedWnorm):
    MO = {}
    for i, row in enumerate(MergedWnorm):
        mul = 1
        for j, value in enumerate(MergedWnorm[i]):
            mul *= MergedWnorm[i][j]
        MO[i] = mul ** (1. / len(MergedWnorm[i]))
    return MO

x = readFile("Labb.csv")

y = {}

y[0] = x[0]
y[1] = x[1]
y[2] = x[2]

z = getAveragePrirityValue(y)

print(z)

print(getNormalizeVec(z))
