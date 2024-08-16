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

basic_scatter_plot = px.scatter(iris_df, x='sepal_width', y='sepal_length', color='species',
                                size='petal_length', symbol='species', hover_data=['petal_width'])
st.subheader("Iris Dataset: Basic Scatter Plot")
st.plotly_chart(basic_scatter_plot)

#user axis selection
x_axis = st.selectbox('choose a variable for the x-axis', iris_df.columns, index=0)
y_axis = st.selectbox('choose a variable for the y-axis', iris_df.columns, index=1)

#create buble chart with color, different symbols, and hover data
colored_buble_hover_fig = px.scatter(iris_df, x=x_axis, y=y_axis, color='species',
                                     size='petal_length',hover_data=['petal_width'])

#mostrar a figura em streamlit
st.subheader('Iris Dataset: Buble Chart with Selectable Axes')

colored_buble_hover_fig.update_layout(
    font_family="Courier New",
    title = 'Iris Dataset Buble Chart',
    xaxis_title=x_axis,
    yaxis_title=y_axis,
    legend_title='Species'
)

st.plotly_chart(colored_buble_hover_fig)


