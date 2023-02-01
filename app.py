
import streamlit as st
import pandas as pd 
import altair as alt


st.set_page_config(
    page_title = "itsMike Dashboard", 
    layout = "wide"
)

st.write("""

    # My first app!
    Hello world!

""")

data = pd.read_excel(
    io = "sample.xls",
    engine = "xlrd",
    sheet_name = "Orders",  
    nrows = 1000
    )

st.dataframe(data)


# Sidebar 

st.sidebar.header("Available filters: ")
region = st.sidebar.multiselect(
    "Select the region: ",
    options = data['Region'].unique(), 
    default = data['Region'].unique()
)

category = st.sidebar.multiselect(
    "Select the category: ",
    options = data['Category'].unique(), 
    default = data['Category'].unique()
)

shipping_mode = st.sidebar.multiselect(
    "Select the shipping mode: ",
    options = data['Ship_Mode'].unique(), 
    default = data['Ship_Mode'].unique()
)

data_selection = data.query(
    "Region == @region & Category == @category & Ship_Mode == @shipping_mode"
)