from flask import Flask, request, jsonify
import pickle
import numpy as np

# intiating Flask app
app = Flask(__name__)

with open("models/linear_model.pkl", "rb") as f:
    model = pickle.load(f)

# creating home
@app.route("/")
def home():
    return {"message": "Student Grade Prediction API"}

# creating prediction endpoint of the API
@app.route("/predict", methods = ["POST"])

def predict():
    # getting json data from front end or postman for testing

    data = request.json

    features = np.array([
        [
            data["socioeconomic_score"],
            data["study_hours"],
            data["sleep_hours"],
            data["attendance"]
        ]
    ])

    prediction = model.predict(features)

    # Return data to the front end

    return jsonify({
        "predicted_grade": round(float(prediction[0]), 2)
    })

if __name__ == "__main__":
    app.run(debug=True)
