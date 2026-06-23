# Executive Dashboard for Performance Measurement

A comprehensive Streamlit dashboard application for tracking and analyzing executive performance metrics across different departments and years.

## Features

- **Interactive Filters**: Select specific years and departments to view relevant data
- **Key Performance Indicators (KPIs)**: Display important metrics including:
  - Projects Completed
  - Budget Utilized (%)
  - Average Issue Resolution Time (Days)
- **Data Visualization**: Interactive bar charts showing projects completed by department
- **Report Generation**: Download filtered data as CSV reports

## Installation

1. Install the required dependencies:
```bash
pip install --break-system-packages -r requirements.txt
```

2. Run the application:
```bash
export PATH="/home/ubuntu/.local/bin:$PATH"
streamlit run dashboard.py
```

## Usage

1. **Select Year**: Use the dropdown to filter data by year (2022, 2023, 2024)
2. **Select Department**: Choose from HR, Finance, or IT departments
3. **View KPIs**: Monitor key performance indicators for the selected filters
4. **Analyze Trends**: Review the interactive bar chart for visual insights
5. **Download Reports**: Export filtered data as CSV for further analysis

## Data Structure

The dashboard uses sample data containing:
- **Year**: 2022, 2023, 2024
- **Department**: HR, Finance, IT
- **Projects_Completed**: Number of projects completed
- **Budget_Utilized (%)**: Percentage of budget utilized
- **Issue_Resolution_Time (Days)**: Average time to resolve issues

## Technology Stack

- **Streamlit**: Web application framework
- **Pandas**: Data manipulation and analysis
- **Plotly Express**: Interactive data visualization

## Files

- `dashboard.py`: Main Streamlit application
- `requirements.txt`: Python dependencies
- `README.md`: This documentation file