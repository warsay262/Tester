import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def main():
    st.title('State Population Comparison')
    st.sidebar.header('Select States/Regions')

    # Load the data from the CSV file
    data = pd.read_csv('state-population.csv')

    # Get a list of unique states/regions from the 'state/region' column
    states = data['state/region'].unique()

    # Allow users to select up to 5 states/regions using checkboxes in the sidebar
    selected_states = st.sidebar.multiselect('Select States/Regions', states, default=states[:5])

    # Filter the data based on the selected states/regions
    filtered_data = data[data['state/region'].isin(selected_states)]

    # Create a bar chart to compare the populations
    st.bar_chart(filtered_data.pivot_table(index='year', columns='state/region', values='population'))

if __name__ == '__main__':
    main()
