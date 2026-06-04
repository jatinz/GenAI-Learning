import streamlit as st
import pandas as pd
import numpy as np
import os

st.title("All about Streamlit")
st.write("This is basically a very simple yet cool project.")

df = pd.DataFrame({
    'Name':["Jatin","Sushree","Jack","Mary"],
    'Age':[32,23,45,31],
    'Gender':["M","F","M","F"]
})

name = st.text_input("Enter name")
age = st.text_input("Enter age")
gender = st.text_input("Enter gender")

df.loc[len(df)] = [name, age, gender]

st.write("Here is an example of dataframe :")

st.write(df)

data = os.listdir("C:/Education")

dir_data = pd.DataFrame(data)
st.write(dir_data)