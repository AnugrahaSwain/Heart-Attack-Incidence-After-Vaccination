import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import base64
st.set_page_config(page_title="Heart Attack & Vaccine Analysis", layout="wide")
# Function to set background image
def set_background(image_file):
    with open(image_file, "rb") as image:
        encoded = base64.b64encode(image.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
set_background(r"C:\Users\anugr\OneDrive\Desktop\Projects\covid19.jpg") 
# Loading dataset
df = pd.read_csv(r"C:\Users\anugr\OneDrive\Desktop\Projects\heart_attack_vaccine_data.csv")
st.title("💉 Heart Attack Incidence After Vaccination")
# Basic Overview
st.header("Dataset Overview")
st.dataframe(df.head())
st.markdown(f"**Total Records:** {df.shape[0]}")
st.markdown(f"**Heart Attack Cases Reported:** {df['Heart Attack Date'].notna().sum()}")
# Sidebar Filters
st.sidebar.header("Filters")
gender_filter = st.sidebar.multiselect("Gender", options=df["Gender"].unique(), default=df["Gender"].unique())
dose_filter = st.sidebar.multiselect("Vaccine Dose", options=df["Vaccine Dose"].unique(), default=df["Vaccine Dose"].unique())
filtered_df = df[df["Gender"].isin(gender_filter) & df["Vaccine Dose"].isin(dose_filter)]
# Visualization: Age distribution
st.header("Age Distribution")
fig, ax = plt.subplots()
sns.histplot(filtered_df['Age'], kde=True, ax=ax, bins=20)
st.pyplot(fig)
# Visualization: Heart Attack by Gender
st.header("Heart Attacks by Gender")
heart_attacks = filtered_df[filtered_df['Heart Attack Date'].notna()]
fig, ax = plt.subplots()
sns.countplot(data=heart_attacks, x='Gender', ax=ax)
st.pyplot(fig)
# Visualization: Heart Attack vs Vaccine Dose
st.header("Heart Attacks by Vaccine Dose")
fig, ax = plt.subplots()
sns.countplot(data=heart_attacks, x='Vaccine Dose', ax=ax)
st.pyplot(fig)
# BMI Analysis
st.header("BMI Analysis")
filtered_df['Heart Attack Occurred'] = filtered_df['Heart Attack Date'].notna()
fig, ax = plt.subplots()
sns.boxplot(data=filtered_df, x='Heart Attack Occurred', y='BMI', ax=ax)
ax.set_xticklabels(["No Heart Attack", "Heart Attack"])
ax.set_title("BMI Distribution by Heart Attack Occurrence")
st.pyplot(fig)
# Cholesterol and Blood Pressure Correlation
st.header("Cholesterol & Blood Pressure in Heart Attack Cases")
fig, ax = plt.subplots()
sns.boxplot(data=heart_attacks, x='Blood Pressure', y='Cholesterol Level', ax=ax)
st.pyplot(fig)
# Summary
st.header("Key Observations")
st.markdown("- Most heart attack cases were observed in Females.")
st.markdown("- Patients with high cholesterol and elevated blood pressure showed higher heart attack occurrence.")
st.markdown("- First dose shows slightly more reported cases compared to Second dose.")
