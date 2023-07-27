import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def load_data():
    # Load the dataset from the CSV file
    data = pd.read_csv("state-population.csv")
    return data

def main():
    # Add a title to the app
    st.title('USA Total Population by Year')

    # Load the data from the CSV file
    df = load_data()

    # Get unique states and years for the dropdowns
    states = df['state/region'].unique()
    years = df['year'].unique()

    # Add dropdown widgets for state, year, and population type
    selected_state = st.selectbox('Select State/Region:', states)
    selected_year = st.selectbox('Select Year:', years)
    selected_population_type = st.selectbox('Select Population Type:', ['total', 'under18'])

    # Filter the dataset based on user selections
    df_filtered = df[(df['state/region'] == selected_state) & (df['year'] == selected_year) & (df['ages'] == selected_population_type)]

    # Display the filtered data as a table
    st.write('Filtered Data:')
    st.write(df_filtered)

    # Create a bar chart using matplotlib and display it using Streamlit
    fig, ax = plt.subplots()
    ax.bar(df_filtered['ages'], df_filtered['population'])
    ax.set_xlabel('Population Type')
    ax.set_ylabel('Population')
    ax.set_title(f'{selected_state} Population - Year {selected_year}')
    st.pyplot(fig)

if __name__ == '__main__':
    main()
