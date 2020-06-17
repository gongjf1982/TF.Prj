import tensorflow as tf

a = tf.constant([[1], [2], [3]])
print(a.shape)
print(a.numpy())
b = tf.expand_dims(a, 1)
print(b.shape)
print(b.numpy())

a1 = tf.constant([[2, 3, 4], [4, 5, 6], [2, 3, 4]])
a2 = tf.constant([[1, 2, 2], [6, 7, 9], [2, 3, 2]])
b1 = tf.concat([a1, a2], axis=0)
b2 = tf.concat([a1, a2], axis=1)

print(b1)
print("--------------------------")
print(b2)
print("--------------------------")

c1 = tf.constant([[1.1, 2.1], [3.1, 4.1], [5.1, 6.1]])
c2 = tf.bitcast(c1, type=tf.int32)
print(c1.numpy(), "---", c1.shape)
print(c2.numpy(), "---", c2.shape)
print(c1.dtype)
print(c2.dtype)
