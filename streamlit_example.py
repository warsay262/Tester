import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Read the dataset
df = pd.read_csv('state-population.csv')

def main():
    st.title('State Population Comparison')
    st.sidebar.title('Select States/Regions')
    
    # Get a list of unique states/regions from the data
    states = data['state/region'].unique().tolist()
    
    # Allow users to select multiple states/regions from the sidebar
    selected_states = st.sidebar.multiselect('Select States/Regions', states)
    
    if not selected_states:
        st.warning('Please select at least one state/region.')
        return
    
    # Filter the data based on the selected states/regions
    filtered_data = data[data['state/region'].isin(selected_states)]
    
    # Display the data table
    st.write('Selected State/Region Population Data:')
    st.dataframe(filtered_data)
    
    # Create and display the bar chart
    fig, ax = plt.subplots()
    for state in selected_states:
        state_data = filtered_data[filtered_data['state/region'] == state]
        ax.bar(state_data['year'], state_data['population'], label=state)
    
    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.title('Population Comparison by State/Region')
    plt.legend()
    
    st.write('Population Comparison Bar Chart:')
    st.pyplot(fig)

if __name__ == '__main__':
    main()

