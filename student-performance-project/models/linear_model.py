import pandas as pd 
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Loading the dataset after EDA
df = pd.read_csv(r"D:\AIML_ASSG\student-performance-project\data\grade_data.csv")

X = df[['Socioeconomic Score', 'Study Hours', 'Sleep Hours', 'Attendance (%)']]
y = df['Grades']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Selecting model apart from linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

