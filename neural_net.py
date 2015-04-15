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

def ask_user(question):
    print(question)
    return input("> ")
    
# get user to answer questions, store answers in list
def quiz(questions):
    answers = []
    for question in questions:
        answer = ask_user(question)
        print()
        answers.append(answer)
    return answers

# convert user input string to boolean value
def s_to_bool(s):
    s = s.lower()
    if s in ['t','y','1','true','yes']:
        return True
    elif s in ['f','n','0','false','no']:
        return False
    else:
        error_msg = \
                'String cannot be converted to boolean value'
        raise ValueError(error_msg)

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
        
    def quiz_run(self):
        questions = (name+'? (y/n)' for name in self.names)
        answers = (quiz(questions))
        bools = [ s_to_bool(s) for s in answers ]
        return self.run(bools)
