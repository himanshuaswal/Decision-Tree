# Import libraries necessary for this project
import numpy as np
import pandas as pd
from IPython.display import display # Allows the use of display() for DataFrames

# Set a random seed
import random
random.seed(42)

# Load the dataset
in_file = 'titanic_data.csv'

# Store the 'Survived' feature in a new variable and remove it from the dataset
outcomes = full_data['Survived']
features_raw = full_data.drop('Survived', axis = 1)

#preprocess the data
features = pd.get_dummies(features_raw)
features = features.fillna(0.0)
display(features.head

#splitting the dataset
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(features, outcomes, test_size=0.2, random_state=42)
#Train the model
new_model= DecisionTreeClassifier(max_depth=,min_samples_leaf=5)
new_model.fit(X_train,y_train)

#Make predictions
ytrainpred = new_model.predict(X_train)
ytestpred = new_model.predict(X_test)

#Calculate the accuracy
from sklearn .metrics import accuracy_score
trainaccuracy = accuracy_score(y_train, ytrainpred)
testaccuracy = accuracy_score(y_test, ytestpred)
print('training accuracy',trainaccuracy)
print('testing accuracy', testaccuracy)
