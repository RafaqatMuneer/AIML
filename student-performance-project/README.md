# Student Performance Prediction

This project predicts student grades using Multiple Linear Regression based on:

* Socioeconomic Score
* Study Hours
* Sleep Hours
* Attendance (%)

The project demonstrates a complete machine learning workflow including data analysis, model training, Flask API development, and Streamlit frontend integration.

## Dataset

The dataset contains the following features:

* Socioeconomic Score
* Study Hours
* Sleep Hours
* Attendance (%)
* Grades (Target Variable)

## Technologies Used

* Python
* Pandas
* Scikit-learn
* Flask
* Streamlit
* NumPy

## Model

Algorithm used:

* Multiple Linear Regression

Evaluation metrics:

* R² Score
* Mean Squared Error (MSE)
* Root Mean Squared Error (RMSE)

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Train the Model

```bash
python training/train_model.py
```

This generates:

```text
models/linear_model.pkl
```

## Run the Flask API

```bash
python app.py
```

The API runs on:

```text
http://127.0.0.1:5000
```

## Run the Streamlit Application

```bash
cd streamlit_app
streamlit run app.py
```

The application runs on:

```text
http://localhost:8501
```

## API Endpoint

### POST /predict

Example input:

```json
{
    "socioeconomic_score": 0.7,
    "study_hours": 6,
    "sleep_hours": 8,
    "attendance": 85
}
```

Example response:

```json
{
    "predicted_grade": 82.5
}
```
