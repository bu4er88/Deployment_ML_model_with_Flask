import pickle
import numpy as np


knn = pickle.load(open('model/model.pkl', 'rb'))

class Model():
    def __init__(self, model=knn):
        self.model = model

    def predict(self, age, sex_male, sex_female):
        prediction = self.model.predict(np.array([[age, sex_male, sex_female]]))
        return prediction
