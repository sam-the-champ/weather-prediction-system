from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from backend import predict_weather
from datetime import datetime
import logging

app = Flask(__name__)
CORS(app)

# Set up logging
logging.basicConfig(level=logging.DEBUG)

# Route for the homepage
@app.route('/')
def index():
    return render_template('index.html')

def validate_date(date_str):
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

# Route for making predictions
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        date = data['date']

        # Validate the date input
        if not date:
            return jsonify({'error': 'Date is required'}), 400

        # Validate date format
        if not validate_date(date):
            return jsonify({'error': 'Invalid date format. Please use YYYY-MM-DD.'}), 400
        
        # Predict weather for the given date
        prediction = predict_weather(date)

        if prediction is None or len(prediction) != 4:  # Ensure correct prediction structure
            return jsonify({'error': 'Prediction failed'}), 500
        
        # Prepare a response with all predicted values
        response = {
            'Temperature': f'{prediction["Temperature"]:.2f} °C',
            'Windspeed': f'{prediction["Windspeed"]:.2f} km/h',
            'Precipitation': f'{prediction["Precipitation"]:.2f} mm',
            'Humidity': f'{prediction["Humidity"]:.2f} %'
        }

        return jsonify(response)
    except Exception as e:
        logging.error(f"Error occurred: {str(e)}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
