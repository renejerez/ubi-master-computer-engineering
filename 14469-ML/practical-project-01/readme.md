1. Consider the “Medical Cost Personal Dataset”, available at “Kaggle.com”. The data
consists of age, sex, BMI(body mass index), children, smoker, region and charges
features.
    The goal is to check whether the charges billed by health insurance can be predicted from
    the remaining features.

   
2. Exploratory Data Analysis.
    a) Convert all the data to numeric values - OK
    b) Check if there are any missing/NULL values - OK
    c) Obtain the histogram of each feature, using:
            a. Bar plots - OK
            b. Density estimates - OK
    d) Analyze the correlation between features:
            a. Observing the scatter plots between pairs of features. - OK
            b. Observing the scatter plots between each feature and the dependent variable - OK
   
3. Obtain Implement the “linear_regression.py” script, that obtains the best model,
according to gradient descent - ok

4. Implement functions to obtain performance measures according to a “k-fold” validation
scheme. Doing

5. Analyze the differences in performance between the models obtained for the different
folds.

6. Adapt the “linear_regression.py”script to fit a polynomial model (of order “p”) to your
data. Repeat the analysis of step 5.