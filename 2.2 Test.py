# Create a prediction based on our model
Y_pred_tree = tree.predict(X_test)

# Computes the Mean Absolute Error of the model
MAE_tree = np.mean(abs(Y_test - Y_pred_tree))/np.mean(Y_test)

# Print the results
print("Tree MAE%:",round(MAE_tree*100,1))