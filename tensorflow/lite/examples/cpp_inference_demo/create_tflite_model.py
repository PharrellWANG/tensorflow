import tensorflow as tf
import numpy as np
# from tensorflow import lite

model = tf.keras.Sequential([tf.keras.layers.Dense(units=1, input_shape=[1])])
model.compile(optimizer='sgd', loss='mean_squared_error')

xs = np.array([ -1.0, 0.0, 1.0, 2.0, 3.0, 4.0], dtype=float)
ys = np.array([ -3.0, -1.0, 1.0, 3.0, 5.0, 7.0], dtype=float)

model.fit(xs, ys, epochs=500)

print(model.predict([10.0]))

# keras_file = 'linear.h5'
# keras.models.save_model(model, keras_file)
path_of_saved_model = 'saved_model'
model.save(path_of_saved_model, save_format='tf')

converter = tf.lite.TFLiteConverter.from_saved_model(path_of_saved_model)
tflite_model = converter.convert()
open('linear.tflite', 'wb').write(tflite_model)