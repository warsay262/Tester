import streamlit as st

def load_data():
    df = pd.read_csv('state-population.csv')
    return df

df = st.cache_data(allow_output_mutation=True)(load_data)()

st.title('Interactive Population Dashboard')

# Create a dropdown for state/region selection
selected_state = st.selectbox('Select a State/Region', df['state/region'].unique())

# Create a radio button for population type selection
population_type = st.radio('Population Type', ['total', 'under18'])

filtered_data = df[(df['state/region'] == selected_state) & (df['ages'] == population_type)]

fig, ax = plt.subplots()
ax.bar(filtered_data['year'], filtered_data['population'])
ax.set_xlabel('Year')
ax.set_ylabel('Population')
ax.set_title(f'{selected_state} - {population_type.capitalize()} Population from 1990 to 2012')
st.pyplot(fig)
