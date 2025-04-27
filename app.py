import streamlit as st
import pandas as pd
import seaborn as sns

st.title("Student Performance Dashboard")
df = pd.read_csv("StudentsPerformance.csv")

# Interactive filters
gender_filter = st.selectbox("Filter by gender:", ["All"] + list(df["gender"].unique()))
if gender_filter != "All":
    df = df[df["gender"] == gender_filter]

# Visualizations
st.subheader("Math Score Distribution")
sns.histplot(df["math score"], kde=True)
st.pyplot()

st.subheader("Scores by Gender")
sns.boxplot(x="gender", y="math score", data=df)
st.pyplot()
# THis is changed