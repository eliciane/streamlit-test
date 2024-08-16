import streamlit as st
import plotly.express as px

# Set the app title
st.title('My First Streamlit App')
# Add a welcome message
st.write('Welcome to my Streamlit app!')
# Create a text input
widgetuser_input = st.text_input('Enter a custom message:', 'Hello, Streamlit!')
# Display the customized message
st.write('Customized Message:', 'user_input')

#importar iris dataset
iris_df = px.data.iris()
print (iris_df.head())

st.subheader("Iris Dataset")
st.dataframe(iris_df)
