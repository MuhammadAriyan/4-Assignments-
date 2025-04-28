import streamlit as st
import pandas as pd
st.set_page_config(page_title="BMI Calculator", page_icon="🏋️", layout="centered")
st.title("BMI Calculator")

height = st.slider("Height (cm)", 100, 250, 175)
weight = st.slider("Height (cm)", 40, 200, 70)

bmi = weight / ((height / 100) ** 2)
st.write(f"Your BMI is: {bmi:.2f}")

st.write("BMI Categories:")
st.write("Underweight: < 18.5")
st.write("Normal weight: 18.5–24.9")
st.write("Overweight: 25–29.9")
st.write("Obesity: BMI ≥ 30")
st.write("You are in the ", end="")
if bmi < 18.5:
    st.write("Underweight")
elif 18.5 <= bmi < 25:
    st.write("Normal weight")
elif 25 <= bmi < 30:
    st.write("Overweight")
else:
    st.write("Obesity")