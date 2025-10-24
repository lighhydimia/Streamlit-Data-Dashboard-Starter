import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 Simple Data Dashboard")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("Data Preview")
    st.write(df.head())

    st.subheader("Summary Statistics")
    st.write(df.describe())

    col_options = df.columns.tolist()
    x_axis = st.selectbox("Select X-axis", col_options)
    y_axis = st.selectbox("Select Y-axis", col_options)

    chart_type = st.selectbox("Chart Type", ["Line", "Bar", "Scatter"])

    fig, ax = plt.subplots()

    if chart_type == "Line":
        ax.plot(df[x_axis], df[y_axis])
    elif chart_type == "Bar":
        ax.bar(df[x_axis], df[y_axis])
    else:
        ax.scatter(df[x_axis], df[y_axis])

    st.subheader("Visualization")
    st.pyplot(fig)
else:
    st.info("Please upload a CSV file to begin.")
