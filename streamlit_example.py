import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
data = pd.read_csv('state-population.csv')

def main():
    st.title('State Population Analysis')
    
    # Display the loaded data (optional)
    st.write("Data Preview:")
    st.dataframe(data)

    # Filter the data based on user selection (total or under18 population)
    population_type = st.radio('Select Population Type:', ['total', 'under18'])
    filtered_data = data[data['ages'] == population_type]

    # Group the data by state/region and calculate the total population for each
    state_population = filtered_data.groupby('state/region')['population'].sum()

    # Display the bar chart
    st.bar_chart(state_population)

if __name__ == "__main__":
    main()
