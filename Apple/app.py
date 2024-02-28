from flask import Flask, render_template, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load the trained Logistic Regression model
model = joblib.load('logistic_regression_model.pkl')

# Homepage API
@app.route('/')
def homepage():
    return render_template('index.html')

# Prediction API
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the input data from the HTML form
        input_data = {
            'A_id': float(request.form['A_id']),
            'Size': float(request.form['Size']),
            'Weight': float(request.form['Weight']),
            'Sweetness': float(request.form['Sweetness']),
            'Crunchiness': float(request.form['Crunchiness']),
            'Juiciness': float(request.form['Juiciness']),
            'Ripeness': float(request.form['Ripeness']),
            'Acidity': float(request.form['Acidity'])
        }

        # Convert input data to a DataFrame for prediction
        input_df = pd.DataFrame([input_data])

        # Make prediction using the model
        prediction = model.predict(input_df)[0]

        # Return the predicted quality
        return render_template('result.html', prediction=prediction)

    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run(host= '0.0.0.0', port = 5005, debug=False)
