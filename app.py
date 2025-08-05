import streamlit as st
import pickle
import numpy as np
with open("student_pas_fail_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("Student Pass fail Prediction App")
st.write("enter the student details")

study_hours=st.number_input("enter study hours")

attendance=st.number_input("enter the attendance")
assignments=st.number_input("enter assignment submitted ")


if st.button("Predict"):
    input_data=np.array([[study_hours, attendance, assignments]])
    prediction=model.predict(input_data)

if prediction[0]==1:
    st.success("Your student is paas")
else:
    st.error("Your student is not paas")
