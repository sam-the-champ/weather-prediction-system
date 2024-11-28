import pickle
import numpy as np
from datetime import datetime
import logging

# Load the trained multi-output model
with open('models/weather_multioutput_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Function to simulate getting weather features based on a date
def get_weather_features_from_date(date_str):
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    
    # Example: Extract features based on the date
    # Simulate fetching previous weather conditions (these should be replaced with real historical data)
    previous_temperature = np.random.uniform(20, 30)  # Random value between 20 and 30 degrees Celsius
    previous_humidity = np.random.uniform(50, 90)      # Random humidity between 50% and 90%
    previous_windspeed = np.random.uniform(0, 20)      # Random windspeed between 0 and 20 km/h

    # Return only the features expected by the model (3 features)
    return np.array([[previous_temperature, previous_humidity, previous_windspeed]]).reshape(1, -1)

def predict_weather(date_str):
    # Get the features for the selected date
    features = get_weather_features_from_date(date_str)
    
    # Log the features used for prediction
    logging.debug(f"Features for prediction: {features}")

    # Predict all target variables (Temperature, Windspeed, Precipitation, Humidity)
    prediction = model.predict(features)
    
    # Return a dictionary of predictions
    return {
        'Temperature': prediction[0][0],
        'Windspeed': prediction[0][1],
        'Precipitation': prediction[0][2],
        'Humidity': prediction[0][3]
    }
