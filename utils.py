from math import radians, sin, cos, sqrt, atan2
import joblib
import pandas as pd


def calculate_distance(selected_point):
    
    melbourne_cbd = (-37.81246595358802, 144.96216389711412)
    lat1, lon1 = map(radians, selected_point)
    lat2, lon2 = map(radians, melbourne_cbd)
    
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    
    R = 6371.0
    distance = R * c
    
    return distance

def property_type_formatter(label):
    formatter_dict = {
        "h": "House/Cottage/Villa",
        "u": "Single Unit/Duplex",
        "t": "Townhouse"
    }
    
    return formatter_dict[label]

def preprocess_data(submitted_data):
    preprocessor = joblib.load("joblib-files/preprocessor.pkl")
    
    processed_data = preprocessor.transform(pd.DataFrame(submitted_data, index=[0, ]))
    return processed_data

def predict(submitted_data, model_path="joblib-files/decision-tree.pkl"):
    processed_data = preprocess_data(submitted_data)
    
    model = joblib.load(model_path)
    prediction = model.predict(processed_data)
    
    return prediction