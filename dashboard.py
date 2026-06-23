import streamlit as st
import pandas as pd
import plotly.express as px

def load_data():
    data = {
        'Year': [2022, 2022, 2023, 2023, 2024, 2024],
        'Department': ['HR', 'Finance', 'IT', 'HR', 'IT', 'Finance'],
        'Projects_Completed': [10, 15, 12, 8, 18, 14],
        'Budget_Utilized (%)': [85, 90, 80, 75, 95, 88],
        'Issue_Resolution_Time (Days)': [5, 7, 6, 8, 4, 6]
    }
    return pd.DataFrame(data)

# Load Data
df = load_data()

# Streamlit UI
st.title("Executive Dashboard for Performance Measurement")

# Filters
year_filter = st.selectbox("Select Year", options=df['Year'].unique())
department_filter = st.selectbox("Select Department", options=df['Department'].unique())

filtered_df = df[(df['Year'] == year_filter) & (df['Department'] == department_filter)]

# KPI Display
st.subheader("Key Performance Indicators")
st.metric(label="Projects Completed", value=int(filtered_df['Projects_Completed'].values[0]))
st.metric(label="Budget Utilized (%)", value=f"{filtered_df['Budget_Utilized (%)'].values[0]}%")
st.metric(label="Avg Issue Resolution Time (Days)", value=int(filtered_df['Issue_Resolution_Time (Days)'].values[0]))

# Visualization
st.subheader("Performance Trends")
fig = px.bar(df[df['Year'] == year_filter], x='Department', y='Projects_Completed', color='Department', title="Projects Completed by Department")
st.plotly_chart(fig)

# Download Report
st.subheader("Download Report")
report_csv = filtered_df.to_csv(index=False).encode('utf-8')
st.download_button("Download CSV Report", data=report_csv, file_name="performance_report.csv", mime='text/csv')