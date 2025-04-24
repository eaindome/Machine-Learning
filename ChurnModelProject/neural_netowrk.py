import tensorflow as tf
import matplotlib.pyplot as plt                                           # type: ignore
from tensorflow.keras import Sequential                         # type: ignore
from tensorflow.keras.layers import Flatten, Dense       # type: ignore

(train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.mnist.load_data()

# scale down images
train_images = train_images/255.0
test_images = test_images/255.0

# check the shape of the data
print(f"Training data shape: {train_images.shape}")
print(f"Test data shape: {test_images.shape}")
print(f"Training labels: {train_labels} ")

plt.imshow(train_images[0], cmap='grey')
plt.show()

# define neural network model
my_model = tf.keras.models.Sequential()             # creates a sequential model where layers are added one after another
my_model.add(Flatten(input_shape=(28, 28)))         # flattens 128x128 images to 1D array suitable for the Dense layer
my_model.add(Dense(128, activation='relu'))
my_model.add(Dense(10, activation='softmax'))

# compile the model
my_model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# train themodel
my_model.fit(train_images, train_labels, epochs=3)

# evaluate the model
val_loss, val_acc = my_model.evaluate(test_images, test_labels)
print(f"Test accuracy of my model: {val_acc}")