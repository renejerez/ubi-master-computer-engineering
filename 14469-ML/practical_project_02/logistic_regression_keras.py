import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix


#########################################################################
#   Read, Normalize and Split Data
#########################################################################


with open('/content/drive/My Drive/wines.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader) # to skip the header file
    X = []
    y = []
    for row in csv_reader:
        y.append(int(float(row[0]) == 1))
        temp= [float(i) for i in row[1:]]
        X.append(temp)


X = np.asarray(X)
y = np.asarray(y)

scaler = MinMaxScaler()
scaler.fit(X)
X = scaler.transform(X)
X = np.append(X, np.ones((X.shape[0],1), np.float64), axis=1)


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=1234)
    

#########################################################################
#   Logistic regression
#########################################################################

def compute_loss(y_true, y_pred):
    # binary cross entropy
    epsilon = 1e-9
    y1 = y_true * np.log(y_pred + epsilon)
    y2 = (1-y_true) * np.log(1 - y_pred + epsilon)
    return -np.mean(y1 + y2)

def _sigmoid(x):
    return 1 / (1 + np.exp(-x))

def feed_forward(X, weights, bias):
    z = np.dot(X, weights) + bias
    A = _sigmoid(z)
    return A

def fit(X, y, n_iters, lr):
    n_samples, n_features = X.shape

    # init parameters
    weights = np.zeros(n_features)
    bias = 0
    losses = []

    # gradient descent
    for _ in range(n_iters):
        A = feed_forward(X, weights, bias)
        losses.append(compute_loss(y,A))
        dz = A - y # derivative of sigmoid and bce X.T*(A-y)
        # compute gradients
        dw = (1 / n_samples) * np.dot(X.T, dz)
        db = (1 / n_samples) * np.sum(dz)
        # update parameters
        weights -= lr * dw
        bias -= lr * db
      
    return weights, bias, losses

def predict(X, weights, bias):
    threshold = .5
    y_hat = np.dot(X, weights) + bias
    y_predicted = _sigmoid(y_hat)
    y_predicted_cls = [1 if i > threshold else 0 for i in y_predicted]
    return np.array(y_predicted_cls)


learning_rate = 0.0001
n_iters = 1000

weights, bias, losses = fit(X_train, y_train, n_iters, learning_rate)

plt.ion()
plt.figure(1)
plt.plot(range(n_iters), losses, '-g', label='Tensorflow')
plt.xlabel('Iterations')
plt.ylabel('Loss')
plt.legend(loc='upper right')
plt.grid()
plt.show()
plt.pause(0.01)


predictions = predict(X_test, weights, bias)

cm  = confusion_matrix(np.asarray(y_test), np.asarray(predictions))

print("Test accuracy: {0:.3f}".format(np.sum(np.diag(cm))/np.sum(cm)))
print("Confusion Matrix:",np.array(cm))