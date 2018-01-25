import tensorflow as tf
import numpy as np
import geneticevoloving.helpers as helpers
import random
import operator
import timeit


class GenEvolve:
    """Class genetic evolving of a neural network"""

    def __init__(self, data, x, best_sample, lucky_few,
                 number_children, chance_mutation, nn_info):
        self.data = data
        self.x = x
        self.best_sample = best_sample
        self.lucky_few = lucky_few
        self.number_children = number_children
        self.chance_mutation = chance_mutation
        self.nn_info = nn_info

    def mutate_nn(self, neural_net):
        neural_net_mutated = []
        for variables in neural_net:
            dim_variable = variables.shape
            if len(dim_variable) > 1:
                rows_weights = dim_variable[0]
                col_weights = dim_variable[1]
                var_mutated = np.zeros([rows_weights, col_weights],
                                       np.float32)
                for i in range(rows_weights):
                    for j in range(col_weights):
                        if int(100 * random.random() < 10):
                            var_mutated[i, j] = np.random.randn()
                        else:
                            var_mutated[i, j] = variables[i, j]

                neural_net_mutated.append(var_mutated)
            else:
                length_bias = dim_variable[0]
                var_mutated = np.zeros(length_bias, np.float32)
                for i in range(length_bias):
                    if int(100 * random.random() < 50):
                        var_mutated[i] = np.random.randn()
                    else:
                        var_mutated[i] = variables[i]

                neural_net_mutated.append(var_mutated)
        return neural_net_mutated

    def mutate_population(self, population):
        for i in range(len(population)):
            if random.random() * 100 < self.chance_mutation:
                population[i] = self.mutate_nn(population[i])
        return population

    def cross_section(self, father, mother):
        child = []
        for variables_father, variables_mother in zip(father, mother):
            dim_variable = variables_father.shape
            if len(dim_variable) > 1:
                rows_weights = dim_variable[0]
                col_weights = dim_variable[1]
                var_child = np.zeros([rows_weights, col_weights],
                                     np.float32)
                for i in range(rows_weights):
                    for j in range(col_weights):
                        if int(100 * random.random() < 50):
                            var_child[i, j] = variables_father[i, j]
                        else:
                            var_child[i, j] = variables_mother[i, j]
                child.append(var_child)
            else:
                length_bias = dim_variable[0]
                var_child = np.zeros(length_bias, np.float32)
                for i in range(length_bias):
                    if int(100 * random.random() < 50):
                        var_child[i] = variables_father[i]
                    else:
                        var_child[i] = variables_mother[i]
                child.append(var_child)
        return child

    def create_children(self, parents):
        next_population = []
        len_childs = int(len(parents)/2)
        len_parents = len(parents)
        for i in range(len_childs):
            for j in range(self.number_children):
                child = self.cross_section(parents[i],
                                           parents[len_parents - 1 - i])
                next_population.append(child)
        return next_population

    def select_from_population(self, population_sorted):
        next_generation = []

        for i in range(self.best_sample):
            next_generation.append(population_sorted[i])
        for i in range(self.lucky_few):
            next_generation.append(random.choice(population_sorted))
        return next_generation

    def fitness_calc(self, pred):
        input_data = self.data[0]
        target_data = self.data[1]

        y = tf.placeholder(tf.float32, [None, self.nn_info[-1]])
        cost = tf.losses.mean_squared_error(y, pred)
        init = tf.global_variables_initializer()
        with tf.Session() as sess:
            sess.run(init)
            err = sess.run(cost, feed_dict={self.x: input_data,
                                            y: target_data})
        return err

    def compute_fitness_population(self, population):
        population_fittest = {}
        i = 0
        for neural_net in population:
            tic = timeit.default_timer()
            restored_net, x_placeholder = helpers.restore_nn(neural_net,
                                                             self.nn_info)
            self.x = x_placeholder
            err = self.fitness_calc(pred=restored_net)
            population_fittest[i] = int(round(err*100))
            i = i + 1
            toc = timeit.default_timer()
            # print(toc - tic)
            tf.reset_default_graph()

        population_sorted = sorted(population_fittest.items(),
                                   key=operator.itemgetter(1))
        i = 0
        new_population = []
        for neural_net in population:
            ind = population_sorted[i][0]
            new_population.append(population[ind])
            i = i + 1
        return new_population

    def next_generation(self, previous_generation):
        population_sorted = self.compute_fitness_population(previous_generation)
        self.run_best_nn(population_sorted[0])
        next_parents = self.select_from_population(population_sorted)
        next_population = self.create_children(next_parents)
        next_generation = self.mutate_population(next_population)
        return next_generation

    def run_best_nn(self, best_nn):
        input_data = self.data[0]
        target_data = self.data[1]

        y = tf.placeholder(tf.float32, [None, 1])
        best_nn, x_placeholder = helpers.restore_nn(best_nn, self.nn_info)
        self.x = x_placeholder
        cost = tf.losses.mean_squared_error(y, best_nn)
        init = tf.global_variables_initializer()
        with tf.Session() as sess:
            sess.run(init)
            result = sess.run(best_nn, feed_dict={self.x: input_data,
                                            y: target_data})
            err = sess.run(cost, feed_dict={self.x: input_data,
                                            y: target_data})

            print('Result')
            print(result)
            print('Error')
            print(err)
