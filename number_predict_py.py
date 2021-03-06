# -*- coding: utf-8 -*-
"""Number_predict.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IviZPdnj-6SE80utCl84E2yotiVYOVAF
"""

import tensorflow as tf

mnist  = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train = tf.keras.utils.normalize(x_train, axis=1)
x_test = tf.keras.utils.normalize(x_test, axis=1)
print(x_train[0])
model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(128, activation = tf.nn.relu))
model.add(tf.keras.layers.Dense(128, activation = tf.nn.relu))
model.add(tf.keras.layers.Dense(10, activation = tf.nn.softmax))

model.compile(optimizer = 'adam', loss = 'sparse_categorical_crossentropy', metrics = ['accuracy'])

model.fit(x_train, y_train, epochs = 3)

val_loss, val_acc = model.evaluate(x_test, y_test)
print(val_loss, val_acc)

import matplotlib.pyplot as plt
plt.imshow(x_train[10], cmap = plt.cm.binary)

model.save('Num_predict.model')

new_model = tf.keras.models.load_model('Num_predict.model')

predict  = new_model.predict([x_test])  
import numpy as np
print(np.argmax(predict[1]))
plt.imshow(x_test[1])