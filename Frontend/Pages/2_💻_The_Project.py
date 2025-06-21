import streamlit as st
from PIL import Image

# Page configuration
st.set_page_config(page_title="Linguistic to Logic - The Project", page_icon=":anchor:", layout="wide")
st.markdown('<h1 style="text-align: center;">LINGUISTIC TO LOGIC - THE SQL CONVERTER (LTL-SQL)</h1>', unsafe_allow_html=True)
st.markdown('')
st.markdown('')

# Project section
st.markdown('<h2>Project Overview</h2>', unsafe_allow_html=True)
st.markdown('<h3>About the Project</h3>', unsafe_allow_html=True)

st.markdown("""
**Linguistic to Logic - The SQL Converter (LTL-SQL)** is an innovative tool developed by us Code Syndicate to simplify the process of translating natural language queries into SQL queries. This tool is designed to bridge the gap between human language and database querying, making it easier for users to interact with complex databases without requiring extensive SQL knowledge.
""")
st.markdown("<hr>", unsafe_allow_html=True)

st.markdown('<h3>Key Features</h3>', unsafe_allow_html=True)
st.markdown("""
- **Natural Language Processing (NLP):** Converts natural language questions into SQL queries.
- **Built-in Databases:** Supports three pre-configured databases, allowing users to start querying immediately.
- **Custom Database Support:** Users can also integrate their own databases for personalized querying.
- **Database Summary:** Provides an overview of the database structure and contents.
- **Visualizations:** Generates images and plots based on database content for better insights.
- **Comparisons:** Enables comparative analysis of different datasets within the database.
""")
st.markdown("<hr>", unsafe_allow_html=True)

st.markdown('<h3>Use Cases</h3>', unsafe_allow_html=True)
st.markdown("""
- **Non-Technical Users:** Allows users with no SQL experience to interact with databases using plain language.
- **Data Analysts:** Facilitates quick querying and visualization of database information.
""")
