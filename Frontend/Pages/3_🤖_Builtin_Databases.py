import sys 
sys.path.append('..\Backend')

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import processing_functions
import database_functions

st.set_page_config(page_title="Linguistic to Logic - Builtin Databases", page_icon=":anchor:", layout="wide")
st.markdown('<h1 style="text-align: center;">LINGUISTIC TO LOGIC - THE SQL CONVERTER (LTL-SQL)</h1>', unsafe_allow_html=True)
st.markdown('')
st.markdown('')

# Sample DataFrames for demonstration
def display_sample_table(table_name):
    table = database_functions.execute_query('SELECT * FROM ' + table_name + ' LIMIT 5')
    st.dataframe(table)

# Create a dictionary for easy table selection
tables = {
    'Real Estate': 'RealEstate',
    'Student': 'Student',
    'Medical Record': 'MedicalRecord'
}

# Main Page
def main_page():
    st.markdown('<h2>Builtin Databases</h2>', unsafe_allow_html=True)

    # Select Table Dropdown
    st.markdown('<h3>Select it !</h3>', unsafe_allow_html=True)
    selected_table = st.selectbox("Select from a builtin database in order to experience additional functionalities:", list(tables.keys()))

    # Display Sample Table
    st.markdown('<h3>Table Structure</h3>', unsafe_allow_html=True)
    display_sample_table(tables[selected_table])
    st.markdown("<hr>", unsafe_allow_html=True)
    
    # Enter the Question
    st.markdown('<h2>SQL Query Retriever</h2>', unsafe_allow_html=True)
    st.markdown('<h3>Questions</h3>', unsafe_allow_html=True)
    question = st.text_input("Enter your question regarding the selected database:")

    if st.button("Submit"):
        
        st.markdown("<hr>", unsafe_allow_html=True)
        output = processing_functions.generate_final_prototype_output(tables[selected_table], question)
        st.markdown('<h2>Outputs Section</h2>', unsafe_allow_html=True)
        
        if output['General'] is not None:
            st.markdown('<h3>General Output</h3>', unsafe_allow_html=True)
            st.text_area(
                'The SQL command to extract the data is as follows: ',
                value = output['General']['SQL Query'],
                height = 32 
            )
            st.markdown('<h4>' + output['General']['Statement'] + '</h4>', unsafe_allow_html=True)
            data = output['General']['Data']
            st.dataframe(data)
                
        if output['Image'] is not None:
            if output['Image']['SQL Query'] is not None:
                st.markdown('<h3>Image Output</h3>', unsafe_allow_html=True)
                st.text_area(
                    'The SQL command to extract the image is as follows: ',
                    value = output['Image']['SQL Query'],
                    height = 32 
                )
                st.markdown('<h4>' + output['Image']['Statement'] + '</h4>', unsafe_allow_html=True)
                img = output['Image']['Image']
                st.image(img)
            else:
                st.markdown('<h3>Image Output</h3>', unsafe_allow_html=True)
                st.text_area(
                    "The sopecified table doesn't contain an image field, so the following was generated: ",
                    value = 'ERROR: '+output['Image']['Statement'],
                    height = 32 
                )
        
        if output['Plot'] is not None:
            st.markdown('<h3>Plot Output</h3>', unsafe_allow_html=True)
            st.text_area(
                'The SQL command to extract and process the plot is as follows: ',
                value = output['Plot']['SQL Query'],
                height = 32 
            )
            st.markdown('<h4>' + output['Plot']['Statement'] + '</h4>', unsafe_allow_html=True)
            img = output['Plot']['Plot']
            st.image(img)
            
        if output['Comparison'] is not None:
            st.markdown('<h3>Comparison Output</h3>', unsafe_allow_html=True)
            st.text_area(
                'The SQL command to extract the comparison is as follows: ',
                value = output['Comparison']['SQL Query'],
                height = 32 
            )
            st.markdown('<h4> The table data is as follows: </h4>', unsafe_allow_html=True)
            data_table = output['Comparison']['Comparison table']
            st.dataframe(data_table)
            st.markdown('<h4> The text comparison is as follows: </h4>', unsafe_allow_html=True)
            text_comparison = output['Comparison']['Comparison summary']
            st.markdown(text_comparison)
        
        if output['Summary'] is not None:
            st.markdown('<h3>Summary Output</h3>', unsafe_allow_html=True)
            st.text_area(
                'The SQL command to extract the summary is as follows: ',
                value = output['Summary']['SQL Query'],
                height = 32 
            )
            st.markdown('<h4> The summary with statistics is as follows: </h4>', unsafe_allow_html=True)
            data_table = output['Summary']['Summary description']
            st.dataframe(data_table)
            st.markdown('<h4> The text summary is as follows: </h4>', unsafe_allow_html=True)
            text_summary = output['Summary']['Summary text']
            st.markdown(text_summary) 

if __name__ == "__main__":
    main_page()