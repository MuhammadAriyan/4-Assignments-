import streamlit as st 
import pandas as pd 

st.title("Simple Data Dashboard")

upload_file = st.file_uploader("choose a CSV file", type="csv")

if upload_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader('Data preview')
    st.write(df.head())
    
    st.subheader("Data Summary")
    st.write(df.describe())

    st.subheader("Filter Data")
    columns = df.column.tolist()
    selected_columns = st.selectbox("Select column to filter by", columns)
    unique_values = df[selected_columns].unique()
    selected_value =  st.selectbox["Select Value", unique_values]

    # filter
    filtered_df = df[df[selected_column] == selected_value ]
    st.write(filtered_df)

    st.subheader("Plot Data")
    x_column = st.selectbox("select x-axis column", column)
    y_column = st.selectbox("select y-axis column", column)

    if st.button("Generate Plot"):
        st.line_chart(filtered_df.set_index(x_column)[y_column])

else:
    st.write('waiting on file upload!! ')   