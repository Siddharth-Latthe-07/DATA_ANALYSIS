import streamlit as st
import pandas as pd


st.title("Address Details Data Analysis")

@st.cache
def load_data():
    data = pd.read_csv("address (1).csv")
    return data

df = load_data()

st.write("Shape of the dataset:", df.shape)
st.write("Dataset head:", df.head())

if st.checkbox("Show summary statistics"):
    st.write(df.describe())

if st.checkbox("Show missing values count"):
    st.write(df.isnull().sum())

if st.checkbox("Show value count by country"):
    country_value_counts = df['country'].value_counts()
    st.bar_chart(country_value_counts)

if st.checkbox("Show value count by state"):
    state_value_counts = df['state'].value_counts()
    st.bar_chart(state_value_counts)
if st.checkbox("Show value count by taluka"):
    city_value_counts = df['taluka'].value_counts()
    st.bar_chart(city_value_counts)
if st.checkbox("Show value count by district"):
    city_value_counts = df['district'].value_counts()
    st.bar_chart(city_value_counts)
if st.checkbox("Show value count by division"):
    city_value_counts = df['division'].value_counts()
    st.bar_chart(city_value_counts)
if st.checkbox("Show value count by landmark"):
    city_value_counts = df['landmark'].value_counts()
    st.bar_chart(city_value_counts)
if st.checkbox("Show value count by street"):
    city_value_counts = df['street_name'].value_counts()
    st.bar_chart(city_value_counts)
if st.checkbox("Show value count by locality"):
    city_value_counts = df['locality'].value_counts()
    st.bar_chart(city_value_counts)
if st.checkbox("Show value count by building name"):
    city_value_counts = df['building name'].value_counts()
    st.bar_chart(city_value_counts)

if st.checkbox("Show value count by village"):
    city_value_counts = df['village'].value_counts()
    st.bar_chart(city_value_counts)

if st.checkbox("Show value count by postal code"):
    postal_code_value_counts = df['pincode'].value_counts()
    st.bar_chart(postal_code_value_counts)


