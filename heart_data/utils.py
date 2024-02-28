import pickle
import numpy as np

def get_predicated_heart(age, sex, cp, trestbps, chol):
    
    model_file_path = r"/Users/pranaykumbhare/Desktop/vs.python/linear file/heart_data /logistic.pkl"
    
    with open(model_file_path, 'rb')as f:
        model = pickle.load(f)
    test_array = np.array([[age, sex, cp, trestbps, chol]])
    
    predicated_heart = model.predict(test_array)
    
    return predicated_heart