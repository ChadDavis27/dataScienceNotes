import numpy as np

def sumStat(values):
    '''
    Return the common stats for a given array
    '''
    valSum = np.zeros(5, dtype="float")
    valSum[0] = np.round(np.add.reduce(values), decimals = 2)
    valSum[1] = np.round(np.max(values), decimals = 2)
    valSum[2] = np.round(np.min(values), decimals = 2)
    valSum[3] = np.round(np.std(values), decimals = 2)

    return valSum

values = np.arange(5)
print(values)
print(summary(values))
