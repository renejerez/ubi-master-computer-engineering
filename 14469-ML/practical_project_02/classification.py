import matplotlib.pyplot as plt

import argparse
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LeakyReLU
from tensorflow.keras.optimizers import SGD
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical

# Load and preprocess the MNIST dataset
(trainX, trainY), (testX, testY) = mnist.load_data()
trainX = trainX.reshape((trainX.shape[0], 28 * 28)).astype("float32") / 255.0
testX = testX.reshape((testX.shape[0], 28 * 28)).astype("float32") / 255.0
trainY = to_categorical(trainY, 10)
testY = to_categorical(testY, 10)

# Argument parsing to receive model topology as input
parser = argparse.ArgumentParser(description="Define model topology.")
parser.add_argument("--topology", required=True, help="Specify the model topology, e.g., '53' or '453'.")
args = parser.parse_args()

# Parse topology parameter to build model dynamically
topology = args.topology
model = Sequential()

# Add layers based on topology
for i, neurons in enumerate(topology):
    neurons = int(neurons)
    if i == 0:
        # First layer with input shape
        model.add(Dense(neurons, input_shape=(784,)))
        model.add(LeakyReLU(alpha=0.01))
    else:
        # Hidden layers
        model.add(Dense(neurons))
        model.add(LeakyReLU(alpha=0.01))

# Output layer with 10 neurons (for MNIST classification)
model.add(Dense(10, activation="softmax"))

# Compile and train the model
model.compile(optimizer=SGD(0.01), loss="categorical_crossentropy", metrics=["accuracy"])
history = model.fit(trainX, trainY, validation_data=(testX, testY), epochs=20, batch_size=128)

# Evaluate model
test_loss, test_accuracy = model.evaluate(testX, testY, verbose=0)
print(f"Test Loss: {test_loss:.4f}")
print(f"Test Accuracy: {test_accuracy:.4f}")


# Assuming 'history' contains the training results of the Leaky ReLU Large model
epochs = range(20)  # Set this to the number of epochs you used
import matplotlib.pyplot as plt

# Create a 2x2 plot layout
fig, axs = plt.subplots(2, 2, figsize=(14, 10))
epochs = range(20)

# Plot Training Loss
axs[0, 0].plot(epochs, history.history["loss"], label="Leaky ReLU Large Train Loss", color="purple", linestyle="solid", marker="o", markevery=2, alpha=0.7)
axs[0, 0].set_title("Training Loss")
axs[0, 0].set_xlabel("Epochs")
axs[0, 0].set_ylabel("Loss")
for i, loss in enumerate(history.history["loss"]):
    if i % 2 == 0:  # Display every 2 epochs
        axs[0, 0].annotate(f"{loss:.2f}", (i, loss), textcoords="offset points", xytext=(0,5), ha='center')
axs[0, 0].legend(loc="upper right")

# Plot Test Loss
axs[0, 1].plot(epochs, history.history["val_loss"], label="Leaky ReLU Large Test Loss", color="purple", linestyle="dashed", marker="o", markevery=2, alpha=0.7)
axs[0, 1].set_title("Test Loss")
axs[0, 1].set_xlabel("Epochs")
axs[0, 1].set_ylabel("Loss")
for i, val_loss in enumerate(history.history["val_loss"]):
    if i % 2 == 0:  # Display every 2 epochs
        axs[0, 1].annotate(f"{val_loss:.2f}", (i, val_loss), textcoords="offset points", xytext=(0,5), ha='center')
axs[0, 1].legend(loc="upper right")

# Plot Training Accuracy
axs[1, 0].plot(epochs, history.history["accuracy"], label="Leaky ReLU Large Train Accuracy", color="purple", linestyle="solid", marker="o", markevery=2, alpha=0.4)
axs[1, 0].set_title("Training Accuracy")
axs[1, 0].set_xlabel("Epochs")
axs[1, 0].set_ylabel("Accuracy")
for i, accuracy in enumerate(history.history["accuracy"]):
    if i % 2 == 0:  # Display every 2 epochs
        axs[1, 0].annotate(f"{accuracy:.2f}", (i, accuracy), textcoords="offset points", xytext=(0,5), ha='center')
axs[1, 0].legend(loc="upper left")

# Plot Test Accuracy
axs[1, 1].plot(epochs, history.history["val_accuracy"], label="Leaky ReLU Large Test Accuracy", color="purple", linestyle="dashed", marker="o", markevery=2, alpha=0.4)
axs[1, 1].set_title("Test Accuracy")
axs[1, 1].set_xlabel("Epochs")
axs[1, 1].set_ylabel("Accuracy")
for i, val_accuracy in enumerate(history.history["val_accuracy"]):
    if i % 2 == 0:  # Display every 2 epochs
        axs[1, 1].annotate(f"{val_accuracy:.2f}", (i, val_accuracy), textcoords="offset points", xytext=(0,5), ha='center')
axs[1, 1].legend(loc="upper left")

# Adjust layout and save plot
plt.tight_layout()
plt.savefig("leaky_relu_plot.png")  # Save the plot with annotations
print(f"Test Loss: {test_loss:.4f}")
print(f"Test Accuracy: {test_accuracy:.4f}")