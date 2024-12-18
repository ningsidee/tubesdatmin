import streamlit as st
import numpy as np
import pandas as pd
from joblib import load

# Load the trained model
model = load("./decision_tree_model.joblib")

st.title("Sistem Prediksi Penyakit Jantung")
st.write("Dataset yang digunakan dalam proyek ini adalah kumpulan fitur terkait kesehatan dari pasien, dengan tujuan untuk memprediksi apakah seorang pasien memiliki penyakit jantung atau tidak.")
st.write("Modeling menggunakan dua algoritma yaitu Decision Tree untuk supervised learning dan K-means untuk clustering. Hasil clustering dapat dilihat pada bagian performa model")

def prediction_window():
    st.subheader("Heart Disease Prediction")

    age = st.number_input("Age:", min_value=1, max_value=120, value=30)
    sex = st.selectbox("Sex:", [0, 1], format_func=lambda x: "Female" if x == 0 else "Male")
    cp = st.selectbox("Chest Pain Type:", [1, 2, 3, 4], format_func=lambda x: {
        1: "Typical Angina", 
        2: "Atypical Angina", 
        3: "Non-Anginal Pain", 
        4: "Asymptomatic"
    }.get(x))

    restbp = st.number_input("Resting Blood Pressure (mm Hg):", min_value=50, max_value=200, value=120)
    chol = st.number_input("Cholesterol (mg/dl):", min_value=100, max_value=600, value=200)
    fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl:", [0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
    restcg = st.selectbox("Resting Electrocardiographic Results:", [0, 1, 2], format_func=lambda x: {
        0: "Normal", 
        1: "ST-T Wave Abnormality", 
        2: "Left Ventricular Hypertrophy"
    }.get(x))

    thalach = st.number_input("Maximum Heart Rate Achieved:", min_value=50, max_value=250, value=150)
    exang = st.selectbox("Exercise Induced Angina:", [0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
    oldpeak = st.number_input("ST Depression Induced by Exercise Relative to Rest:", min_value=0.0, max_value=10.0, value=1.0)
    slope = st.selectbox("Slope of Peak Exercise ST Segment:", [1, 2, 3], format_func=lambda x: {
        1: "Upsloping", 
        2: "Flat", 
        3: "Downsloping"
    }.get(x))
    
    ca = st.selectbox("Number of Major Vessels Colored by Fluoroscopy:", [0, 1, 2, 3])
    thal = st.selectbox("Thalassemia:", [3, 6, 7], format_func=lambda x: {
        3: "Normal", 
        6: "Fixed Defect", 
        7: "Reversible Defect"
    }.get(x))

    input_data = pd.DataFrame([[age, sex, cp, restbp, chol, fbs, restcg, thalach, exang, oldpeak, slope, ca, thal]], columns=[
        "age", "sex", "cp", "restbp", "chol", "fbs", "restcg", "thalach", "exang", "oldpeak", "slope", "ca", "thal"
    ])

    X_encoded = pd.read_csv("X_encoded.csv")

    input_data_encoded = input_data.reindex(columns=X_encoded.columns, fill_value=0)

    if st.button("Predict"):
        prediction = model.predict(input_data_encoded)
        prediction_label = "Has Heart Disease" if prediction[0] == 1 else "No Heart Disease"
        st.write(f"Prediction: **{prediction_label}**")

def performance_window():
    st.subheader("Model Performance")

    st.image("./confusion_matrix.png", caption="Confusion Matrix")
    st.image("./decision_tree.png", caption="Decision Tree")
    st.image("./K-means clustering.png", caption="PCA Clustering")

def main():
    # Create tabs for prediction and performance sections
    tab1, tab2 = st.tabs(["Prediksi Model", "Performa Model"])

    with tab1:
        prediction_window()

    with tab2:
        performance_window()

if __name__ == "__main__":
    main()
