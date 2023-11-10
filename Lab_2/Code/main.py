import numpy as np

def readFile(name):
    return np.loadtxt(name, delimiter = ";", dtype = float)

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
    _sum = 0.
    for index, row in enumerate(W):
        _sum += W[index]
    for index, row in enumerate(W):
        Wnormalize[index] = W[index] / _sum
    return Wnormalize

def getMO(MergedWnorm):
    MO = {}
    for i, row in enumerate(MergedWnorm):
        mul = 1
        for j, value in enumerate(MergedWnorm[i]):
            mul *= MergedWnorm[j][i]
        MO[i] = mul ** (1. / len(MergedWnorm[i]))
    return MO

def ff(id):
    y = {}
    y[0] = x[id + 0]
    y[1] = x[id + 1]
    y[2] = x[id + 2]
    z = getAveragePrirityValue(y)
    #print(z)
    #print(getNormalizeVec(z))
    return getNormalizeVec(z)

x = readFile("1.csv")

MergedWnorm = []

MergedWnorm.append(ff(0))
MergedWnorm.append(ff(3))
MergedWnorm.append(ff(6))

#print(MergedWnorm)

print(getMO(MergedWnorm))


