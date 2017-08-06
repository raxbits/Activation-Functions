from math import e

def sigmoid(logit):
    return (1/(1+e**(logit*-1)))


def relu(logit):
    return(0 if (logit<0) else logit)

def tanh(logit):
    return ((e**logit - e**-logit)/(e**logit + e**-logit))

