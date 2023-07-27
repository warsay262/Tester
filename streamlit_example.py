import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
@st.cache
def load_data():
    df = pd.read_csv('state-population.csv')
    return df

df = load_data()

# Create the Streamlit app components
st.title('Interactive Population Dashboard')

# Create a dropdown for state/region selection
selected_state = st.selectbox('Select a State/Region', df['state/region'].unique())

# Create a radio button for population type selection
population_type = st.radio('Population Type', ['total', 'under18'])

# Filter the data based on user input
filtered_data = df[(df['state/region'] == selected_state) & (df['ages'] == population_type)]

# Plot the data as a line chart
fig, ax = plt.subplots()
ax.plot(filtered_data['year'], filtered_data['population'], marker='o', linestyle='-')
ax.set_xlabel('Year')
ax.set_ylabel('Population')
ax.set_title(f'{selected_state} - {population_type.capitalize()} Population from 1990 to 2012')
st.pyplot(fig)
