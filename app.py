
import streamlit as st
import pandas as pd 
import altair as alt


st.set_page_config(
    page_title = "itsMike Dashboard", 
    layout = "wide"
)

st.write("""

    # SALES DASHBOARD
    ##### built by **itsMike**

""")

data = pd.read_excel(
    io = "sample.xls",
    engine = "xlrd",
    sheet_name = "Orders",  
    nrows = 1000
)

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

# Displaying the modified dataframe
st.dataframe(data_selection)



# Charts

total_sales = int(data_selection['Sales'].sum())

average_sale = round(data_selection['Sales'].mean(), 2)

total_profit = int(data_selection['Profit'].sum())


l_column, m_column, r_column = st.columns(3)

with l_column:
    st.subheader("Total Sales:")
    st.subheader(f"US$ {total_sales:,}")
with m_column:
    st.subheader("Average Sale:")
    st.subheader(f"US$ {average_sale:,}")
with r_column:
    st.subheader("Total Profit:")
    st.subheader(f"US$ {total_profit:,}")