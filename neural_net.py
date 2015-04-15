import operator
from math import exp

def dot(t1, t2):
    return sum(map(operator.mul, t1, t2))

def sig(z):
    ret = 1/(1+exp(-z))
    assert 0<ret<1 #just in case
    return ret

def adhoc_perceptron(bools, weights, bias):
    return dot(bools, weights) + bias > 0

def adhoc_sigmoid_neuron(bools, weights, bias):
    z = dot(bools, weights) + bias
    return sig(z)

class perceptron(object):
    def __init__(self, names, weights, bias):

        # input dict should be:
        #       key = input name/identifier
        #       value = weight

        self.num_inputs = len(names)
        self.names = names
        self.weights = weights
        self.bias = bias
        return

    def run(self, bools):
        assert len(bools) == self.num_inputs
        return adhoc_perceptron(bools, self.weights, self.bias)
        
