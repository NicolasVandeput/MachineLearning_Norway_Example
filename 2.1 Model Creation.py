# - Import module from sklearn
from sklearn.tree import DecisionTreeRegressor
 
# - Instantiate a Decision Tree Regressor
tree = DecisionTreeRegressor(max_depth=5,max_features=11,min_samples_leaf=5)
 
# - Fit the tree to the training data
tree.fit(X_train,Y_train)