import pickle
import os
model_path = os.path.join(os.path.dirname(__file__), 'random_forest_model.pkl')
with open(model_path, 'rb') as file:
    model = pickle.load(file)

def predict_glass_type(data):
    prediction = model.predict([data])
    return prediction[0]
