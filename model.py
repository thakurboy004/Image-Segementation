import pickle
import numpy as np
import sklearn

model_predict = pickle.load(open('model.pkl', 'rb'))
def predict(input_data):
  X_test = np.array(input_data).reshape(1, -1)
  y_pred = model_predict.predict(X_test)
  if(y_pred[0] == 1):
    return "The image is a brickface"
  elif(y_pred[0] == 2):
    return "The image is a sky"
  elif(y_pred[0] == 3):
    return "The image is a Foliage"
  elif(y_pred[0] == 4):
    return "The image is a Cement"
  elif(y_pred[0] == 5):
    return "The image is a Window"
  elif(y_pred[0] == 6):
    return "The image is a Path"
  elif(y_pred[0] == 7):
    return "The image is a Grass"
  else:
    return "Cannot classify the image"