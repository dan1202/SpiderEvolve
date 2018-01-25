import tensorflow as tf
import numpy as np
import neuralnet.tensorfunctions as tff


class CreateNeuralNet:

    def __init__(self, nn_info):
        self.nn_info = nn_info
        self.generations_nn = []

    def create_neural_net(self):
        try:
            nn_input = self.nn_info[0]
        except IndexError:
            print("Variable nn_info is not declined correctly.")
            print("Cannot find first element of list")
            return

        x = tf.placeholder(tf.float32, [None, nn_input])

#        for i in range(self.generations_count):
#            neural_net = tff.multilayer_perceptron(x, nn_info=self.nn_info)
#            self.generations_nn.append(neural_net)
        neural_net = tff.multilayer_perceptron(x, nn_info=self.nn_info)
        return neural_net

    def create_placeholder(self):
        try:
            nn_input = self.nn_info[0]
        except IndexError:
            print("Variable nn_info is not declined correctly.")
            print("Cannot find first element of list")
            return

        x = tf.placeholder(tf.float32, [None, nn_input])
        return x
