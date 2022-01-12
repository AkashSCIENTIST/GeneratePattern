import tensorflow as tf
import numpy as np

class GeneratePattern:
  def __init__(self, arr, n):
    self.arr = arr
    self.n = n

  def pad_second_dim(self, input, desired_size):
    padding = tf.tile([[0]], tf.stack([tf.shape(input)[0], desired_size - tf.shape(input)[1]], 0))
    return tf.concat([padding, input], 1)

  def pad(self,arr,n):
    if len(arr) > n:
      temp = arr[-1 * n :]
    else:
      temp = arr
    return list(list(np.array(self.pad_second_dim(tf.constant([temp]), n)))[0])

  def generate(self):
    arr = self.arr
    padlen = self.n
    first = []
    second = []
    trunc_type='post'
    padding_type='post'
    n = len(arr)

    for i in range(n-1):
      first.append(self.pad(arr[:i+1], padlen))
      second.append(arr[i+1])

    return (first, second)
