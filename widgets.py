import streamlit as st
import pandas as pd

st.title("Streamlit Text Input")
name=st.text_input("Enter your name")
age=st.slider("Select your age",0,100,25)
opt=["python","java","c++","javascript"]
choice=st.selectbox("your favorite language",opt)
if name:
    st.write(f"Hello {name}")
if age:
    st.write(f"ypur age is {age}")
if choice:
    st.write(f"your favorite language is {choice}")
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'Age': [25, 30, 22, 28],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}
df=pd.DataFrame(data)
df.to_csv("sampledata.csv")
st.write(df)
upload_file=st.file_uploader("uplaod a csv file",type="csv")
if upload_file is not None:
    df=pd.read_csv(upload_file)
    st.write(df)