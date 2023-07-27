import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

@st.cache
def load_data():
    df = pd.read_csv('state-population.csv')
    return df

# Load the data from the CSV file
df = load_data()

# Add a title to the app
st.title('Interactive Population Dashboard')

# Create a dropdown for state/region selection
selected_state = st.selectbox('Select a State/Region', df['state/region'].unique())

# Create a radio button for population type selection
population_type = st.radio('Population Type', ['total', 'under18'])

# Filter the dataset based on user selections
filtered_data = df[(df['state/region'] == selected_state) & (df['ages'] == population_type)]

# Display the filtered data as a table
st.write('Filtered Data:')
st.write(filtered_data)

# Create a bar chart using matplotlib and display it using Streamlit
# Plot the data as a line chart
fig, ax = plt.subplots()
ax.plot(filtered_data['year'], filtered_data['population'], marker='o', linestyle='-')
ax.set_xlabel('Year')
ax.set_ylabel('Population')
ax.set_title(f'{selected_state} - {population_type.capitalize()} Population from 1990 to 2012')
st.pyplot(fig)
