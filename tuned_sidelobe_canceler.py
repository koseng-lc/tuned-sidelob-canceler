'''
Author : Lintang E
NIM : 16/399897/TK/44911
Tuned Sidelobe canceler with signal incident tetha0 = 0 degree
'''
import numpy as np
import matplotlib.pyplot as plt
import sys

mu = 0.01

mean = 0
std_dev = 1
def genWhiteNoise():
    return np.random.normal(0,1)

shift = 2 #Time shift
C = 2 #Amplited
f = 2 #Frequency
w0 = 2*np.pi*f #Freq in rad/s
def inputSignal(step):
    n2 = genWhiteNoise()
    return np.matrix([C*np.cos((step + shift) * w0) + n2, C*np.cos((step + shift) * w0 + np.pi/2) + n2])

def desiredSignal(step):
    n1 = genWhiteNoise()
    return C*np.cos(step*w0) + n1

def calcError(desired, weight, input):
    return desired - input*weight.getT();

def updateWeight(desired, old_weight, input):
    error = calcError(desired,old_weight,input)
    return old_weight + 2*mu*error*input, error


if __name__ == "__main__":
    error = sys.maxint
    weight = np.matrix([0, 0])
    k = 0
    w1 = np.array([])
    w2 = np.array([])
    while abs(error) > 0.01:
        weight, error = updateWeight(desiredSignal(k),weight,inputSignal(k))
        w1 = np.append(w1, weight.item(0))
        w2 = np.append(w2, weight.item(1))
        k += 1
        # Debugging Only
        # print('Weight : {}'.format(weight))
        # print('Error : {}'.format(abs(error)))
    

    print('Final Weight : {} after {} steps'.format(weight, k))

    x1 = np.arange(0, k, 1)
    y1 = w1
    y2 = w2

    plt.plot(x1,y1)
    plt.show()

    plt.plot(x1,y2)
    plt.show()
