from pathlib import Path
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_validate
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score
import pandas as pd


# data path to training data: mean median and standard deviation of the valve cycles
data_file_path = Path(__file__).parent/"processed_data.csv"

# read the data
data = pd.read_csv(data_file_path)

# Target Values is the classification group column 100,90,80,73
x = data.drop(columns=['Target Values'])
y = data['Target Values']

#split training and testing data stratify ensures there are the same % of each group
# random state ensures the results of training remain the same for testing and evaluation purposes
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=40,stratify=y)

# train, test, and predict using Random Forest Classifier
rfc = RandomForestClassifier(random_state=40, class_weight="balanced")
rfc.fit(x_train,y_train)
y_predictions = rfc.predict(x_test)

# cross validation
# compare results against baseline
k_fold = StratifiedKFold(n_splits=10, shuffle=True ,random_state=40)
cv = cross_validate(rfc,x_train,y_train,cv=k_fold, scoring=["accuracy", "f1_macro", "f1_weighted"])

# scores from Random Forest Classifier
print("Baseline Scores")
print("  Accuracy:   ", round(accuracy_score(y_test, y_predictions), 3))
print("  Macro F1:   ", round(f1_score(y_test, y_predictions, average="macro"), 3))
print("  Weighted F1:", round(f1_score(y_test, y_predictions, average="weighted"), 3))

# scores after cross validation
print("Cross-Validation Scores")
print("  Accuracy:   ", round(cv["test_accuracy"].mean(), 3))
print("  Macro F1:   ", round(cv["test_f1_macro"].mean(), 3))
print("  Weighted F1:", round(cv["test_f1_weighted"].mean(), 3))