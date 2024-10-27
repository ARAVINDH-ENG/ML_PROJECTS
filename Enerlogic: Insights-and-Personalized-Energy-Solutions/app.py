from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import pickle

app = Flask(__name__)

# Load the trained model and preprocessing pipeline
with open('model_with_preprocessing.pkl', 'rb') as file:
    model, preprocessor = pickle.load(file)

@app.route('/')
def index():
    return render_template('yoyo.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Extract data from form submission
        age = int(request.form['age'])
        monthly_energy = float(request.form['monthlyEnergy'])
        peak_usage = float(request.form['peakUsage'])
        off_peak_usage = float(request.form['offPeakUsage'])
        annual_income = float(request.form['annualIncome'])
        home_size = float(request.form['homeSize'])
        clv = float(request.form['clv'])
        gender = request.form['gender']
        location = request.form['location']
        building_type = request.form['buildingType']
        renewable_energy = float(request.form['renewableEnergy'])
        education_level = request.form['educationLevel']
        employment_status = request.form['employmentStatus']

        # Create a DataFrame from the form data
        input_data = pd.DataFrame({
            'Age': [age],
            'Monthly Energy Consumption (kWh)': [monthly_energy],
            'Peak Usage (kWh)': [peak_usage],
            'Off-Peak Usage (kWh)': [off_peak_usage],
            'Annual Income ($)': [annual_income],
            'Home Size (sqft)': [home_size],
            'Customer Lifetime Value (CLV)': [clv],
            'Gender': [gender],
            'Location': [location],
            'Building Type': [building_type],
            'Renewable Energy Usage': [renewable_energy],
            'Education Level': [education_level],
            'Employment Status': [employment_status]
        })

        # Apply preprocessing to input data

        # Make prediction
        prediction = model.predict(input_data)

        # Return prediction to user
        return jsonify({'Predicted Satisfaction Score': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)
