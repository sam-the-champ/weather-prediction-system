import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.multioutput import MultiOutputRegressor
from sklearn.linear_model import LinearRegression
import pickle

# Load data
data = pd.read_csv('data/lagos_climate_data.csv')

# Convert 'Date' to datetime format (optional)
data['Date'] = pd.to_datetime(data['Date'])

# Handle missing values by filling them with the column mean
data.fillna(data.mean(), inplace=True)

# Features and target variables
X = data[['Precipitation', 'Humidity', 'Windspeed']]  # Input features
y = data[['Temperature', 'Windspeed', 'Precipitation', 'Humidity']]  # Target variables

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Use a MultiOutputRegressor to handle multiple target variables
model = MultiOutputRegressor(LinearRegression())
model.fit(X_train, y_train)

# Save the trained model to a file
with open('models/weather_multioutput_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Multi-output model training complete and saved.")
