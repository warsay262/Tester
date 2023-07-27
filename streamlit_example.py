import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def load_data():
    # Load the dataset from the CSV file
    data = pd.read_csv("state-population.csv")
    return data

def main():
    # Add a title to the app
    st.title('USA Population Comparison by State')

    # Load the data from the CSV file
    df = load_data()

    # Get unique states and years for the dropdowns
    states = df['state/region'].unique()
    years = df['year'].unique()

    # Add dropdown widgets for state, year, and population type
    selected_state = st.selectbox('Select State:', states)
    selected_year = st.selectbox('Select Year:', years)
    selected_population_type = st.selectbox('Select Population Type:', ['total', 'under18'])

    # Filter the dataset for the 'USA' state/region and the selected year and population type
    df_usa = df[(df['state/region'] == 'USA') & (df['year'] == selected_year) & (df['ages'] == selected_population_type)]

    # Filter the dataset for the selected state/region and the selected year and population type
    df_selected_state = df[(df['state/region'] == selected_state) & (df['year'] == selected_year) & (df['ages'] == selected_population_type)]

    # Create a bar chart using matplotlib and display it using Streamlit
    fig, ax = plt.subplots()
    ax.bar('USA', df_usa['population'].values[0], label='USA')
    ax.bar(selected_state, df_selected_state['population'].values[0], label=selected_state)
    ax.set_xlabel('State/Region')
    ax.set_ylabel('Population')
    ax.set_title(f'Comparison of {selected_state} Population with USA - Year {selected_year}')
    ax.legend()
    st.pyplot(fig)

if __name__ == '__main__':
    main()
