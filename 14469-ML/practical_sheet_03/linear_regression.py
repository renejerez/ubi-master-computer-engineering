import tensorflow as tf
import csv
import numpy as np
import matplotlib.pyplot as plt
from random import uniform


def J(X, y, theta):
    preds = np.squeeze(np.matmul(X, theta))
    temp =  preds - np.squeeze(y)
    return np.sqrt(np.sum(np.matmul(np.transpose(temp), temp)))

#########################################################################
#   Read Data
#########################################################################


with open('pizza.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader) # to skip the header file
    X = []
    y = []
    for row in csv_reader:
        X.append([float(row[0]), 1])
        y.append(float(row[1]))

X = np.asarray(X)
y = np.asarray(y)


#########################################################################
#   Closed-form method
#########################################################################

theta_direct = np.matmul(np.matmul(np.linalg.inv(np.matmul(np.transpose(X), X)), np.transpose(X)), y)

print('Solution (closed-form): J={:.1f}, Theta=({:.2f}, {:.2f})'.format(J(X,y, theta_direct), theta_direct[0], theta_direct[1]))


#########################################################################
#   Gradient Descent method
#########################################################################

learning_rate = 0.0000001
tot_iterations = 100

theta_gd = [uniform(0., 0.5), uniform(750., 1000.)]

for i in range(tot_iterations):
    t_0 = 0
    t_1 = 0
    for j in range(len(y)):
        t_0 +=  (theta_gd[0] * X[j][0] + theta_gd[1] - y[j]) * X[j][0]
        t_1 +=  theta_gd[0] * X[j][0] + theta_gd[1] - y[j]

    t_0 /= len(y)
    t_1 /= len(y)

    theta_gd[0] = theta_gd[0] - learning_rate * t_0
    theta_gd[1] = theta_gd[1] - learning_rate * t_1

print('Solution (Gradient descent): J={:.1f}, Theta=({:.2f}, {:.2f})'.format(J(X,y, theta_gd), theta_gd[0], theta_gd[1]))


#########################################################################
#   Tensor flow
#########################################################################

sess = tf.Session()

# Graph Definition

x_data = tf.placeholder(shape=[None, 2], dtype=tf.float32)
y_target = tf.placeholder(shape=[None], dtype=tf.float32)
weight_0 = tf.Variable(tf.random.uniform(shape=[1, 1], minval=0., maxval=0.5))
weight_1 = tf.Variable(tf.random.uniform(shape=[1, 1], minval=750., maxval=1000))
weights = tf.concat([weight_0, weight_1], 0)

# Define the Model
with tf.variable_scope('model_definition') as scope:
    model_output = tf.matmul(x_data, weights)
    scope.reuse_variables()


def loss_l2(predict, gt):
    predict = tf.squeeze(predict)
    #predict = tf.Print(predict,["predict: ", tf.shape(predict)])
    resid = predict - gt
    ret = tf.sqrt(tf.reduce_sum(tf.pow(resid, tf.constant(2.))))
    return ret

loss = loss_l2(model_output, y_target)
my_opt = tf.train.GradientDescentOptimizer(learning_rate)
train_step = my_opt.minimize(loss)

# Graph execution

init = tf.global_variables_initializer()
sess.run(init)


for i in range(tot_iterations):
    sess.run(train_step, feed_dict={x_data: X, y_target: y})

theta_tf = sess.run(weights)
cur_loss = J(X,y, theta_tf)

print('Solution (Tensor flow): J={:.1f}, Theta=({:.2f}, {:.2f})'.format(cur_loss, theta_tf[0][0], theta_tf[1][0]))


#########################################################################
#   TResults Visualization
#########################################################################

plt.ion()
plt.figure(1)
plt.plot(X[:,0], y, 'o')
plt.plot([np.min(X[:,0]), np.max(X[:,0])],[theta_direct[0]*np.min(X[:,0])+theta_direct[1], theta_direct[0]*np.max(X[:,0])+theta_direct[1] ] ,'-r', label='Closed-form')
plt.plot([np.min(X[:,0]), np.max(X[:,0])],[theta_gd[0]*np.min(X[:,0])+theta_gd[1], theta_gd[0]*np.max(X[:,0])+theta_gd[1] ] ,'-g', label='Gradient Descent')
plt.plot([np.min(X[:,0]), np.max(X[:,0])],[theta_tf[0]*np.min(X[:,0])+theta_tf[1], theta_tf[0]*np.max(X[:,0])+theta_tf[1] ] ,'-b', label='Tensor flow')
plt.legend(loc='upper right')
plt.grid()
plt.show()
plt.pause(0.1)

input('Close app?')
