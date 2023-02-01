
import streamlit as st
import pandas as pd 
import plotly.express as px

st.set_page_config(
    page_title = "itsMike Dashboard", 
    layout = "wide"
)

st.write("""

    # SALES DASHBOARD
    ##### built by **itsMike**

""")
@st.cache()
def read_excel():
    data = pd.read_excel(
        io = "sample.xls",
        engine = "xlrd",
        sheet_name = "Orders",  
        nrows = 1000
    )
    return data

data = read_excel()
# Sidebar (filtering)

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
# st.dataframe(data_selection) 

# Sales description

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


# Charts

# Sales by category
sales_by_category = (
    data_selection.groupby(by=['Category']).sum()['Sales']
)

fig_sales_by_category = px.bar(
    sales_by_category,
    x='Sales', 
    y=sales_by_category.index, 
    orientation='h', 
    title='Total Sales by Category', 
    template = "plotly_white"
)

sales_by_region = (
    data_selection.groupby(by=['Region']).sum()['Sales']
)

fig_sales_by_region = px.bar(
    sales_by_region,
    x=sales_by_region.index,
    y="Sales", 
    title="Total Sales by Region",
    template="plotly_white"
)

l_column, r_column = st.columns(2)

l_column.plotly_chart(fig_sales_by_category, use_container_width=True)
r_column.plotly_chart(fig_sales_by_region, use_container_width=True)