#Lending Club machine learning script
import os, sys, math
import pandas as pd
os.chdir('C:\Users\Noble\Desktop\UNC\Data Analytics\LendingClub')
#raw = pd.read_csv("Cleaned_LoanStats_v2 - Rec Columns only.csv")
raw = pd.read_csv("cleanedloan.csv")
raw.convert_objects(convert_numeric=True)
#this is depreciated, need to find a better method to convert all objects to numerics
from sklearn.cross_validation import train_test_split
from sklearn import tree

#splitting columns and rows into training and test sets

raw = raw[raw.home_2ership != 'ANY']
#onetime strip out of a single row, can clean this up earlier
raw = raw.fillna(0)
#filling in NaNs with 0s
train, test, y_train, y_test = train_test_split(raw.ix[:,:-1], raw['Default?'],test_size=0.33,random_state=1)
#from sklearn.ensemble import RandomForestRegressor
#model = RandomForestRegressor(n_estimators=100,min_samples_leaf=10)
#model.fit(train,y_train)
clf = tree.DecisionTreeClassifier()
clf.fit(train,y_train)
predictions = clf.predict(test)
#testing predictive power
from sklearn.metrics import mean_squared_error
mean_squared_error(predictions, y_test)
from sklearn import metrics
metrics.accuracy_score(y_test,predictions)

from sklearn.externals.six import StringIO
dot_date = StringIO()
tree.export_graphviz(clf)

graph = pydot.Dot()
dot_data = StringIO()
tree.export_graphviz(clf, out_file=dot_data)
graph = pydot.graph_from_dot_data(dot_data.getvalue())
import Image
