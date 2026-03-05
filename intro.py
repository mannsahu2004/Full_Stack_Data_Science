#Import streamlit
import streamlit as st

# Add a title to your app
st.title("My first streamlit app created by Mann Sahu")

# Add some text
st.write("Welcome! This app calculates the square of a number.")

# Create an interactive slider
st.header("Select a Number")
number = st.slider("Pick a number", 0, 100, 25) # min, max, default

# Calculate and diaplay the result
st.subheader("Result")
squared_number = number * number
st.write(f"The square of **{number}** is **{squared_number}**.")