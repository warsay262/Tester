import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Read the dataset
df = pd.read_csv('state-population.csv')

# Create a Streamlit app
st.title('US State Population Dashboard')

# Sidebar widgets for user interaction
state = st.sidebar.selectbox('Select a state/region:', df['state/region'].unique())
year = st.sidebar.selectbox('Select a year:', df['year'].unique())
population_type = st.sidebar.radio('Choose population type:', ['total', 'under18'])

# Filter the data based on user selection
filtered_data = df[(df['state/region'] == state) & (df['year'] == year) & (df['ages'] == population_type)]

# Display the selected data in a table
st.table(filtered_data)

# Create and display the bar chart
plt.figure(figsize=(10, 6))
plt.bar(filtered_data['ages'], filtered_data['population'])
plt.xlabel('Population Type')
plt.ylabel('Population')
plt.title(f'{population_type.capitalize()} Population in {state} ({year})')
st.pyplot(plt)
