# Perfroming basic operation using Eager API

from __future__ import print_function, absolute_import, division
import tensorflow as tf
import numpy as np
import tensorflow.contrib.eager as tfe

print ("Setting Eager mode...")
tfe.enable_eager_execution()

print ("Define Constants.")
a = tf.constant(2)
print ("a = {}".format(a))
b = tf.constant(3)
print ("b = {}".format(b))


print("Running operations, without tf.Session")
c = a + b
print ("a + b = {}".format(c))
c = a * b
print ("a * b = {}".format(c))

print ("Mixing operations with Tensorflow and Numpy arrays")

a = tf.constant([[1., 2.],
                 [3., 4.]], dtype = tf.float32)
print ("Tensorflow:\n a = {}".format(a))
b = np.array([[4.,3.],
              [2.,1.]], dtype = np.float32)
print ("Numpy:\n b = {}".format(b))

c = a + b
print ("a + b = {}".format(c))

d = tf.matmul(a, b)
print ("a * b = {}".format(d))

for i in range(d.shape[0]):
    for j in range(d.shape[1]):
        print (d[i][j])