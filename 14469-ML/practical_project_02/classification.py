import argparse
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
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
        model.add(Dense(neurons, input_shape=(784,), activation="relu"))
    else:
        # Hidden layers
        model.add(Dense(neurons, activation="relu"))

# Output layer with 10 neurons (for MNIST classification)
model.add(Dense(10, activation="softmax"))

# Compile and train the model
model.compile(optimizer=SGD(0.01), loss="categorical_crossentropy", metrics=["accuracy"])
history = model.fit(trainX, trainY, validation_data=(testX, testY), epochs=20, batch_size=128)

# Evaluate model
test_loss, test_accuracy = model.evaluate(testX, testY, verbose=0)
print(f"Test Loss: {test_loss:.4f}")
print(f"Test Accuracy: {test_accuracy:.4f}")

