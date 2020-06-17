import tensorflow as tf

x = tf.constant([[[1, 2, 3],
                  [4, 5, 6]],
                 [[7, 8, 9],
                  [10, 11, 12]]])
print(x)
print("x Shape = ", x.shape)
y = tf.transpose(x, perm=[0, 2, 1])
print(y)
print("y Shape = ", y.shape)
print(tf.math.argmax(x).numpy())
print(tf.math.argmax(y).numpy())
print("****************************")
a = tf.constant([[11, 2, 3, 4, 5, 6, 7],
                 [11, 12, 5, 4, 5, 6, 7]])
print(tf.math.argmax(a).numpy())
