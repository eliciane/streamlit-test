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

chart_type = st.radio("Select chart type:", ('Scatter Plot', 'Line Chart', 'Bar Chart', 'Histogram',
                                             'Box Plot', 'Pie Chart', '3D Scatter Plot'))

#visualizar o relacionamento entre sepal length and sepal width, colored by spicies
if chart_type == 'Scatter Plot':
    fig = px.scatter(iris_df, x='sepal_length', y='sepal_width', color='species', title='Iris Scatter Plot')
    st.plotly_chart(fig)

#a linha do chart requer time-series data,
#vamos simular uma linha do chart usando o iris dataset index as a faux time-axis
elif chart_type == 'Line Chart':
    iris_df_sorted=iris_df.sort_values(by='sepal_length').reset_index()
    fig = px.line(iris_df_sorted, x=iris_df_sorted, y='sepal_length', color='species', title='Iris Sepal Length Line Chart')
    st.plotly_chart(fig)

#mostre a média sepal length de cada especies usando a bar chart
elif chart_type == 'Bar Chart':
    avg_sepal_length = iris_df.groupby('species')['sepal_length'].mean().reset_index()
    fig = px.bar(avg_sepal_length, x='species', y='sepal_length', title='Average Sepal Length of Iris Species')
    st.plotly_chart(fig)

#mostrar a distribuição da sepal lengths mediante as especies
elif chart_type == 'Histogram':
    fig = px.histogram(iris_df, x='sepal_length', title='Sepal Length Distribution')
    st.plotly_chart(fig)

# mostrar a distribuição da sepal lengths para cada especie usando box plot
elif chart_type == 'Box Plot':
    fig = px.box(iris_df, x='species', y='sepal_length', title='Sepal Length by Species')
    st.plotly_chart(fig)

#mostrar a distribuição das especies no dataseet
elif chart_type == 'Pie Chart':
    species_count = iris_df['species'].value_counts().reset_index()
    fig = px.pies(species_count, values='species', names='index', title='Iris Species Distribution')
    st.plotly_chart(fig)

# criar a 3D scatter plot showing the sepal length, sepal width, and petal length, colored by species
elif chart_type == '3D Scatter Plot':
    fig = px.scatter_3d(iris_df, x='sepal_length', y='sepal_width', z='petal_length', color='species',
                        title='3D scatter plot of Iris Dataset')
    st.plotly_chart(fig)

import plotly.graph_objects as go
import pandas as pd

#calcular a matrix de correlação
corr = iris_df.iloc[:, :4].corr()

#Criar a heatmap
fig= go.Figure(data=go.Heatmap(
    z=corr,
    x=corr.columns,
    y=corr.columns
))
fig.update_layout(title='Heatmap of Iris Features Correlation')
st.plotly_chart(fig)


