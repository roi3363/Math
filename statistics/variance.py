import numpy as np

def deviation(x, mean):
    return mean - x

def variance(deviations):
    print(sum(deviations))
    return round(sum(deviations)/len(deviations), 64)

Xs = [890, 6, 7, 8, 900]
mean = sum(Xs)/len(Xs)
deviations = [deviation(x, mean) for x in Xs]

variance = variance(deviations)
print(f'{mean=}')
print(f'{deviations=}')
print(f'{variance=}')