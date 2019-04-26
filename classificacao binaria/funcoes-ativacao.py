import numpy as np
# transfer function

def stepFunction(soma):
    if (soma >= 1):
        return 1
    return 0

def sigmoidFunction(soma):
    return 1 / (1 + np.exp(-soma))

def tahnFunction(soma):
    return (np.exp(soma) - np.exp(-soma)) / (np.exp(soma) + np.exp(-soma))

def reluFunction(soma):
    if soma >= 0:
        return soma
    return 0

def linearFunction(soma):
    return soma

def softmaxFunction(x):
    ex = np.exp(x)
    return ex / ex.sum()

teste = stepFunction(2.1)
teste1 = sigmoidFunction(2.1)
teste2 = tahnFunction(2.1)
teste3 = reluFunction(2.1)
teste4 = linearFunction(2.1)
valores = [7.0, 2.0, 1.3]
print(softmaxFunction(valores))