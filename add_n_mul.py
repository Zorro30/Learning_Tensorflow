from __future__ import print_function
import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' #this is to remove the unwanted warning.

a = tf.constant(2)
b = tf.constant(3)

with tf.Session() as sess:
    print ("a = 2, b = 3")
    print ("Addition = {}".format(sess.run(a+b)))
    print ("Multiplication = {}".format(sess.run(a*b)))
    #