import streamlit as st
import pandas as pd


st.title("Contact Details Data Analysis")

@st.cache
def load_data():
    data = pd.read_csv("contact_details (1).csv")
    return data

df = load_data()


st.write("Shape of the dataset:", df.shape)
st.write("Dataset head:", df.head())

if st.checkbox("Show summary statistics"):
    st.write(df.describe())

if st.checkbox("Show missing values count"):
    st.write(df.isnull().sum())

if st.checkbox("Show value count by contact designation"):
    contact_value_counts = df['contact_designation'].value_counts()
    st.bar_chart(contact_value_counts)

if st.checkbox("Show value count by fax number"):
    fax_value_counts = df['fax_number'].value_counts()
    st.bar_chart(fax_value_counts)

if st.checkbox("Show value count by email-id"):
    unique_email_id = df["email_id"].value_counts()
    st.bar_chart(unique_email_id)
    
