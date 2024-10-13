import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set the page layout
st.set_page_config(layout="wide")

# Title of the Streamlit app
st.title('Imports and Exports Data Dashboard')

# Load the dataset
data = pd.read_csv("C:\\Users\\Rajiv Ranjan\\Downloads\\Imports_Exports_Dataset.csv")

# Handle missing data (optional, based on the file)
data = data.dropna(subset=['Country', 'Product', 'Import_Export', 'Category', 'Shipping_Method', 'Supplier', 'Payment_Terms'])

# Sidebar filters
st.sidebar.header("Filters")
country_filter = st.sidebar.multiselect('Select Country', options=data['Country'].unique(), default=data['Country'].unique())
product_filter = st.sidebar.multiselect('Select Product', options=data['Product'].unique(), default=data['Product'].unique())

# Filter the data based on selections
filtered_data = data[(data['Country'].isin(country_filter)) & (data['Product'].isin(product_filter))]

# Bar Plot: Count of transactions by Country
st.subheader('Number of Transactions by Country')
fig1, ax1 = plt.subplots(figsize=(10, 6))
sns.countplot(y='Country', data=filtered_data, order=filtered_data['Country'].value_counts().index, palette='coolwarm', ax=ax1)
ax1.set_title('Number of Transactions by Country')
ax1.set_xlabel('Number of Transactions')
ax1.set_ylabel('Country')
st.pyplot(fig1)

# Bar Plot: Count of transactions by Product
st.subheader('Number of Transactions by Product')
fig2, ax2 = plt.subplots(figsize=(10, 6))
sns.countplot(y='Product', data=filtered_data, order=filtered_data['Product'].value_counts().index, palette='Set2', ax=ax2)
ax2.set_title('Number of Transactions by Product')
ax2.set_xlabel('Number of Transactions')
ax2.set_ylabel('Product')
st.pyplot(fig2)

# Pie Chart: Distribution of Import/Export
st.subheader('Distribution of Import vs Export')
fig3, ax3 = plt.subplots(figsize=(8, 8))
import_export_counts = filtered_data['Import_Export'].value_counts()
ax3.pie(import_export_counts, labels=import_export_counts.index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette('pastel'))
ax3.set_title('Distribution of Import vs Export')
st.pyplot(fig3)

# Bar Plot: Count of transactions by Category
st.subheader('Number of Transactions by Category')
fig4, ax4 = plt.subplots(figsize=(10, 6))
sns.countplot(y='Category', data=filtered_data, order=filtered_data['Category'].value_counts().index, palette='muted', ax=ax4)
ax4.set_title('Number of Transactions by Category')
ax4.set_xlabel('Number of Transactions')
ax4.set_ylabel('Category')
st.pyplot(fig4)

# Pie Chart: Distribution of Shipping Method
st.subheader('Distribution of Shipping Methods')
fig5, ax5 = plt.subplots(figsize=(8, 8))
shipping_method_counts = filtered_data['Shipping_Method'].value_counts()
ax5.pie(shipping_method_counts, labels=shipping_method_counts.index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette('Set3'))
ax5.set_title('Distribution of Shipping Methods')
st.pyplot(fig5)

# Bar Plot: Number of Transactions by Supplier
st.subheader('Number of Transactions by Supplier')
fig6, ax6 = plt.subplots(figsize=(10, 6))
sns.countplot(y='Supplier', data=filtered_data, order=filtered_data['Supplier'].value_counts().index, palette='dark', ax=ax6)
ax6.set_title('Number of Transactions by Supplier')
ax6.set_xlabel('Number of Transactions')
ax6.set_ylabel('Supplier')
st.pyplot(fig6)

# Pie Chart: Distribution of Payment Terms
st.subheader('Distribution of Payment Terms')
fig7, ax7 = plt.subplots(figsize=(8, 8))
payment_terms_counts = filtered_data['Payment_Terms'].value_counts()
ax7.pie(payment_terms_counts, labels=payment_terms_counts.index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette('Paired'))
ax7.set_title('Distribution of Payment Terms')
st.pyplot(fig7)
