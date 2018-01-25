from geneticevoloving import geneticevolve as ge
from geneticevoloving import helpers
from neuralnet import createnet as nn
import tensorflow as tf
import numpy as np

population_count = 100
generation_count = 100
best_sample = 20
lucky_few = 20
number_children = 5
chance_mutation = 5

nn_info = [3, 10, 10, 1]

data = []
data_train_in = np.transpose([[0, 1, 1, 0], [0, 1, 0, 1], [1, 1, 1, 1]])
data_train_out = np.array([[0], [1], [1], [0]])
data.append(data_train_in)
data.append(data_train_out)

neural_nets = []

nn_init = nn.CreateNeuralNet(nn_info=nn_info)

for i in range(population_count):
    neural_net = nn_init.create_neural_net()
    neural_nets.append(helpers.get_variables_nn())
    tf.reset_default_graph()

x = nn_init.create_placeholder()

gene = ge.GenEvolve(best_sample=best_sample, lucky_few=lucky_few,
                    number_children=number_children, data=data,
                    chance_mutation=chance_mutation, x=x, nn_info=nn_info)



if ((best_sample + lucky_few) / 2 * number_children != population_count):
    print("population size not stable")
else:
    for generation in range(generation_count):
        print('Generation ' + str(generation + 1))
        next_generation = gene.next_generation(neural_nets)
        neural_nets = next_generation
        print('')