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

    # Filter the dataset for the 'total' rows and the 'USA' state/region
    df_usa = df[(df['state/region'] == 'USA') & (df['ages'] == 'total')]

    # Create a bar chart using matplotlib and display it using Streamlit
    fig, ax = plt.subplots()
    ax.bar(df_usa['year'], df_usa['population'])
    ax.set_xlabel('Year')
    ax.set_ylabel('Total Population')
    ax.set_title('USA Total Population by Year')
    st.pyplot(fig)

if __name__ == '__main__':
    main()
