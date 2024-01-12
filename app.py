from flask import Flask, render_template, request
import pickle
import joblib
import numpy as np
import pandas as pd

app = Flask(__name__)
data = pd.read_csv('Final Cleaned data.csv')

# Load your trained model
model = joblib.load('Model\Aamchi_Mumbai_joblib.pkl')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict')
def predict():
    locations = sorted(data['Address'].unique())
    return render_template('predict.html', locations=locations)

@app.route('/prediction', methods=['POST'])
def prediction():
    if request.method == 'POST':
        # Get user input
        locations = request.form.get('Address')
        ar = float(request.form.get('area'))
        bed = int(request.form.get('Bedrooms'))
        bath = int(request.form.get('Bathrooms'))

        # Preprocess the input data
        # input_data = np.array([[loc, ar, bed, bath]])
        input_data = pd.DataFrame([[locations, ar, bed, bath]], columns=['Address', 'area', 'Bedrooms', 'Bathrooms'])

        # Make prediction using the loaded model
        prediction = model.predict(input_data)
        n = prediction[0]
        n = f'{n:,}'
        res = ""

        for i in n:
            if(i != '.'):
                res+=i
            else:
                break

        # Display the prediction on a new page
        return render_template('result.html', location=locations, prediction=res)

# if __name__ == '__main__':
#     app.run()