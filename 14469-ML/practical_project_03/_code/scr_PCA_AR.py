import os
import numpy as np
import cv2
import shutil
import pickle
from scipy.linalg import eigh


input_folder = r'C:\Users\rene_\Downloads\ML\week07\AR'
output_folder = r'C:\Users\rene_\Downloads\ML\week07\AR_out'

if os.path.isdir(output_folder):
    shutil.rmtree(output_folder)

os.mkdir(output_folder)

files = os.listdir(input_folder)

proportion = 0.05

################################################################################################
#   STEP 1
#   Loading data and concatenate everything into a big matrix
################################################################################################

dataset = []
new_size = []
for f in files:
    if f.find('.jpg') == -1:
        continue
    print(f)
    img = cv2.imread(os.path.join(input_folder, f))
    img = cv2.resize(img, None, fx=proportion, fy=proportion)
    new_size = img.shape
    dataset.append(img.flatten())

dataset = np.asarray(dataset)

print('Dataset created: %d rows x %d columns' % (dataset.shape[0], dataset.shape[1]))


################################################################################################
#   STEP 2
#   Obtain mu, covariance matrix and eigen values/vectors.
################################################################################################

mu = np.mean(dataset, axis=0)

covar = np.cov(dataset.T)       #the "cov" function in numpy requires each instance in a different column

eig_values, eig_vectors = eigh(covar)



################################################################################################
#   STEP 3
#   Find the number of eigenvectors required to keep 99% of the information
################################################################################################

amount_information = 0.99

keep_inf = np.cumsum(np.flip(eig_values)) / np.sum(eig_values)  #This "eig" implementation returns the eigenvalues/eigenvectors
                                                                # in increasing order

pos = np.where(keep_inf >= amount_information)[0][0]

M = np.fliplr(eig_vectors[:, -pos:])                            #Select the top eigenvectors

################################################################################################
#   STEP 4
#   Write everything in file
################################################################################################

with open(os.path.join(output_folder, 'data.dat'), 'wb') as file:
    # Serialize and write the variable to the file
    pickle.dump([mu, covar, eig_vectors, eig_values, M, keep_inf], file)


################################################################################################
#   STEP 5
#   Write top-k eigenvectors
################################################################################################

k = 10
for i in range(k):
    img = np.reshape(M[:, i], new_size)
    img = ((cv2.normalize(img, None, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX,
                                dtype=cv2.CV_32F)) * 255).astype(np.uint8)

    img = cv2.resize(img, None, fx=1.0/proportion, fy=1.0/proportion)
    cv2.imwrite(os.path.join(output_folder, 'eigenvector_%d.png' % i), img)


################################################################################################
#   STEP 6
#   Project images into PCA space and remap them into the original space
################################################################################################

for i, elt in enumerate(dataset):

    #project
    projected = np.matmul(elt - mu, M)

    #remap
    remapped = np.clip(np.matmul(projected, M.T) + mu, 0, 255)

    img = np.reshape(remapped, new_size)
    img = cv2.resize(img, None, fx=1.0 / proportion, fy=1.0 / proportion)
    cv2.imwrite(os.path.join(output_folder, files[i]), img)             # To perceive how much information is kept/lost




input('ok...')