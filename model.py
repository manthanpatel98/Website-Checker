import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

# Loading the Data
data = pd.read_csv('data.csv')

# Arranging Data
X = data.drop(columns=['Result'])
y = data['Result']


# Feature Selection
from sklearn.ensemble import ExtraTreesClassifier
import matplotlib.pyplot as plt
model = ExtraTreesClassifier()
model.fit(X,y)

print(model.feature_importances_)
col_imp = pd.Series(model.feature_importances_, index=X.columns)
col_imp.nlargest(15).plot(kind='barh')
plt.show()

#Picking Final Columns
X_sel = X[['Prefix_Suffix','web_traffic','URL_of_Anchor','SSLfinal_State']]

# Train-Test Split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X_sel, y, test_size=0.25, random_state=42)

#Applying RandomForestClassifier
from sklearn.ensemble import RandomForestClassifier
RFC_classifier = RandomForestClassifier() 
RFC_classifier.fit(X_train,y_train)
y_pred = RFC_classifier.predict(X_test)

# Calculating Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)

# Calculate the Accuracy
from sklearn.metrics import accuracy_score
score=accuracy_score(y_pred,y_test)
print(score)

# Dumping the model
import pickle
pickle.dump(RFC_classifier,open('model.pkl','wb'))
