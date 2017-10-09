# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 16:45:28 2017

@author: zhan
"""

import random
from sklearn.metrics import accuracy_score
random.seed(0)

# calculate a random number where:  a <= rand < b
def rand(a, b):
    return (b-a)*random.random() + a

# Make a matrix 
def makeMatrix(I, J, fill=0.0):
    m = []
    for i in range(I):
        m.append([fill]*J)
    return m


# the activate function of hidden layer
def sigmoidh(x):
    return x**2

# the derivative of the activate function on hidden layer
def dsigmoidh(y):
    return 2*y

# the activate function of output layer
def sigmoido(x):
    return 1 if x > 0 else 0

# the derivative of the activate function on output layer
def dsigmoido(y):
    if y!= 0:
      return 0
    else:
      return rand(1,2)

    
class CBPNNClass:
    def __init__(self, ni, nh, no):
        # number of input, hidden, and output nodes
        self.ni = ni + 1 # +1 for bias node
        self.nh = nh
        self.no = no


        # activations for nodes
        self.ai = [1.0]*self.ni
        self.ah = [1.0]*self.nh
        self.ao = [1.0]*self.no
        
        
        # create weights
        self.wi = makeMatrix(self.ni, self.nh)
        self.wo = makeMatrix(self.nh, self.no)
        # set them to random vaules
        for i in range(self.ni):
            for j in range(self.nh):
                self.wi[i][j] = rand(-0.2, 0.2)
        for j in range(self.nh):
            for k in range(self.no):
                self.wo[j][k] = rand(-2.0, 2.0)


        # last change in weights for momentum   
        self.ci = makeMatrix(self.ni, self.nh)
        self.co = makeMatrix(self.nh, self.no)


    def update(self, inputs, compare):
        if len(inputs) != self.ni-1:
            raise ValueError('wrong number of inputs')


        # input activations
        for i in range(self.ni-1):
            self.ai[i] = inputs[i]


        # hidden activations
        for j in range(self.nh):
            sum = 0.0
            for i in range(self.ni):
                sum = sum + self.ai[i] * self.wi[i][j]
            self.ah[j] = sigmoidh(sum)


        # output activations
        for k in range(self.no):
            sum = 0.0
            for j in range(self.nh):
                sum = sum + self.ah[j] * self.wo[j][k]
            self.ao[k] = sigmoido(compare[0] - sum)
            
        return self.ao[:]
        

    def backPropagate(self, targets, N, M):
        if len(targets) != self.no:
            raise ValueError('wrong number of target values')

        # calculate error terms for output
        output_deltas = [0.0] * self.no
        for k in range(self.no):
            error = targets[k]-self.ao[k]
            output_deltas[k] = dsigmoido(self.ao[k]) * error


        # calculate error terms for hidden
        hidden_deltas = [0.0] * self.nh
        for j in range(self.nh):
            error = 0.0
            for k in range(self.no):
                error = error + output_deltas[k]*self.wo[j][k]
            hidden_deltas[j] = dsigmoidh(self.ah[j]) * error
        # update output weights
        for j in range(self.nh):
            for k in range(self.no):
                change = output_deltas[k]*self.ah[j]
                self.wo[j][k] = self.wo[j][k] + N*change + M*self.co[j][k]
                self.co[j][k] = change
                #print N*change, M*self.co[j][k]


        # update input weights
        for i in range(self.ni):
            for j in range(self.nh):
                change = hidden_deltas[j]*self.ai[i]
                self.wi[i][j] = self.wi[i][j] + N*change + M*self.ci[i][j]
                self.ci[i][j] = change

        # calculate gobal error
        error = 0.0
        for k in range(len(targets)):
            error = error + 0.5*(targets[k]-self.ao[k])**2
        return error
    def test(self, patterns):
        pred_test = []
        label_test = []
        for p in patterns:
            #print(p[0], '->', self.update(p[0]))
            label_test.append(p[2][0])
            pred_test.append(self.update(p[0], p[1])[0])
            print '(', p[0][0], ',', p[1][0], ')', '->', self.update(p[0], p[1])[0]
        print 'test predicting :', pred_test
        print 'true label :', label_test
        #print 'test accuracy:', (accuracy_score(label_test, pred_test))*100, '%'
        print 'testset_predict_error:', (1-accuracy_score(label_test, pred_test))*100, '%'
    def weights(self):
        print '*****************Omega and Bias:****************'
        for i in range(self.ni):
            print self.wi[i]
        print '*****************Lambda:***************'
        for j in range(self.nh):
            print self.wo[j]
    def train(self, patterns, iterations=1000, N=0.5, M=0.1):
        # N: learning rate
        # M: momentum factor
        for i in range(iterations):
            error = 0.0
            pred_train = []
            label_train = []
            for p in patterns:
                inputs = p[0] #list
                compare = p[1]
                targets = p[2] #list
                label_train.append(p[2][0])
                pred_train.append(self.update(inputs, compare)[0])
                error = error + self.backPropagate(targets, N, M)
            #if i % 100 == 0:
                #print('train gobal error :%-.5f' % error)
                
        print 'train predicting :', pred_train
        print 'true label :', label_train
        #print 'train accuracy:', (accuracy_score(label_train, pred_train))*100, '%'
        print 'trainset_predict_error:', (1-accuracy_score(label_train, pred_train))*100, '%'
def demo():
    trainSet = [[[-0.5],[12],[0]], [[0.5],[13.2],[1]], [[0.8],[8],[0]], [[1],[9],[1]], [[1.3],[6.5],[1]], [[1.5],[5],[1]], 
                [[1.7],[3],[0]], [[2.0],[1.5],[0]], [[2.2],[2],[1]], [[2.5],[1],[1]], [[3],[-1.3],[0]], [[3.3],[0.5],[1]],
               [[3.5],[1.5],[1]], [[3.8],[1.1],[0]], [[4.1],[2.8],[1]], [[4.5],[5.1],[1]], [[4.9],[6.8],[0]], 
               [[5.3],[11.2],[1]], [[5.7],[14.1],[0]], [[6.2],[21.2],[1]]]
    print 'creating a network with one input, two hidden, and one output nodes...'
    n = CBPNNClass(1, 2, 1)
    print '**********************train_NN:***************************'
    n.train(trainSet)
    n.weights()
    print '**********************test_NN:****************************'
    testSet=[[[0.7],[11],[1]],[[1.3],[5.2],[0]],[[1.7],[3.0],[0]],[[2.2],[1.5],[1]],[[2.6],[0.5],[1]]
            ,[[3.2],[-0.7],[0]],[[3.7],[1.3],[1]],[[4.3],[3.5],[1]],[[4.9],[6.8],[0]],[[5.5],[13.2],[1]]]
    n.test(testSet)
if __name__ == '__main__':
    demo()

