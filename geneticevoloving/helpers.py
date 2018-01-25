import tensorflow as tf
from neuralnet import createnet as nn
import numpy as np


def get_variables_nn():
    variables_values = []

    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())

        for var in tf.trainable_variables():
            variables_values.append(sess.run(var))
    return variables_values


def restore_nn(variables, nn_info):
    x = nn.CreateNeuralNet(nn_info=nn_info).create_placeholder()

    weights = get_tf_variable(variables[0])
    bias = get_tf_variable(variables[1])
    #    bias = bias_variable([dimension_Input])
    layer = tf.add(tf.matmul(x, weights), bias)

    for i in range(len(variables) - 5):
        weights = get_tf_variable(variables[i + 2])
        bias = get_tf_variable(variables[i + 3])

        # Hidden layer with activation Function
        layer = tf.add(tf.matmul(layer, weights), bias)
        layer = tf.nn.elu(layer)

    last_element = len(variables)
    # Output layer with linear activation
    weights_out = get_tf_variable(variables[last_element - 2])
    bias_out = get_tf_variable(variables[last_element - 1])
    restored_nn = tf.matmul(layer, weights_out) + bias_out
    return restored_nn, x


def get_tf_variable(variable):
    var = tf.Variable([], dtype=tf.float32)
    constant = tf.constant(variable)

    tf_variable = tf.assign(var, constant, validate_shape=False)
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
    return tf_variable
