import sys 
sys.path.append('..\Backend')

import streamlit as st 
import numpy as np 
import pandas as pd 
import string
import processing_functions

# Page configuration
st.set_page_config(page_title="Linguistic to Logic - Custom Databases", page_icon=":anchor:", layout="wide")
st.markdown('<h1 style="text-align: center;">LINGUISTIC TO LOGIC - THE SQL CONVERTER (LTL-SQL)</h1>', unsafe_allow_html=True)
st.markdown('')
st.markdown('')

def generate_random_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(np.random.choice(list(letters_and_digits), length))

def generate_random_strings(length_range, num_strings):
    min_length, max_length = length_range
    random_strings = []
    for _ in range(num_strings):
        length = np.random.randint(min_length, max_length + 1)
        random_strings.append(generate_random_string(length))
    return random_strings

st.markdown('<h2>Custom Database Creator</h2>', unsafe_allow_html=True)

st.markdown('<h3>Table Identification</h3>', unsafe_allow_html=True)
table_name = st.text_input("Enter the table name:")

if table_name:
    if not table_name.isalpha():
        st.warning("Table name should contain only alphabets without spaces.")
    else:
        st.success(f"Table name '{table_name}' is valid.")
        st.markdown('<h3>Table Schema</h3>', unsafe_allow_html=True)
        num_attributes = st.number_input("Number of attributes:", min_value=1, step=1)

        if num_attributes:
            attribute_names = []
            attribute_types = []
            
            for i in range(num_attributes):
                col1, col2 = st.columns(2)
                with col1:
                    attribute_name = st.text_input(f"Attribute {i+1} name:")
                    attribute_names.append(attribute_name)
                with col2:
                    options = {'Integer' : 'INT',
                        'Decimal' : 'FLOAT',
                        'Text' : 'VARCHAR',
                        'Image' : 'BLOB'
                    }
                    attribute_type = st.selectbox(
                        f"Attribute {i+1} type:", 
                        list(options.keys())
                    )
                    attribute_types.append(options[attribute_type])
            
            table_str = 'CREATE TABLE ' + table_name + ' ('
            for i in range(num_attributes-1):
                table_str += attribute_names[i] + ' ' + attribute_types[i] + ', '
            table_str += attribute_names[-1] + ' ' + attribute_types[-1] + ')'
            
            st.markdown("<hr>", unsafe_allow_html=True)
            
            st.markdown('<h2>Sample Table Structure</h2>', unsafe_allow_html=True)
                
            st.markdown('<h3>Table Creator</h3>', unsafe_allow_html=True)
            st.text_area(
                'The create command is as follows: ',
                value=table_str,
                height=16
            )

            st.markdown('<h3>Table Displayer</h3>', unsafe_allow_html=True)
            sample_data = {attribute_names[i]: np.random.rand(5)*100 if attribute_types[i] == 'FLOAT' 
                            else np.random.randint(0, 100, 5) if attribute_types[i] == 'INT'
                            else generate_random_strings((4,16), 5) if attribute_types[i] == 'VARCHAR'
                            else [b'sample_blob']*5 for i in range(num_attributes)}
            
            st.write("The table is displayed below: ")
            sample_table = pd.DataFrame(sample_data)
            st.dataframe(sample_table, width=256*num_attributes)
            
            st.markdown('<h3>Questions</h3>', unsafe_allow_html=True)
            question = st.text_input("Enter your question:")
            
            if st.button("Generate SQL Query"):
                output = processing_functions.generate_final_custom_output(table_name, question, table_str)
                st.markdown("<hr>", unsafe_allow_html=True)
                st.markdown('<h2>Outputs Section</h2>', unsafe_allow_html=True)
                
                if output['General'] is not None:
                    st.markdown('<h3>General Output</h3>', unsafe_allow_html=True)
                    st.text_area(
                        'The SQL command to extract the data is as follows: ',
                        value = output['General']['SQL Query'],
                        height = 32 
                    )
                    st.text_area(
                        'The output statement describing the data is as follows: ',
                        value = output['General']['Statement'],
                        height = 32 
                    )
                        
                if output['Image'] is not None:
                    st.markdown('<h3>Image Output</h3>', unsafe_allow_html=True)
                    st.text_area(
                        'The SQL command to extract the image is as follows: ',
                        value = output['Image']['SQL Query'],
                        height = 32 
                    )
                    st.text_area(
                        'The output statement describing the image is as follows: ',
                        value = output['Image']['Statement'],
                        height = 32 
                    )
                
                if output['Plot'] is not None:
                    st.markdown('<h3>Plot Output</h3>', unsafe_allow_html=True)
                    st.text_area(
                        'The SQL command to extract and process the plot is as follows: ',
                        value = output['Plot']['SQL Query'],
                        height = 32 
                    )
                    st.text_area(
                        'The output statement describing the plo0t is as follows: ',
                        value = output['Plot']['Statement'],
                        height = 32 
                    )
                    plot_details = f"Plot type: {output['Plot']['Plot type']} \nPlot title: {output['Plot']['Title']} \nX-label: {output['Plot']['Xlabel']} \nY-label: {output['Plot']['Ylabel']}"
                    st.text_area(
                        'The details regarding the plot are as follows: ',
                        value = plot_details,
                        height = 32 
                    )
                    
                if output['Comparison'] is not None:
                    st.markdown('<h3>Comparison Output</h3>', unsafe_allow_html=True)
                    st.text_area(
                        'The SQL command to extract the comparison is as follows: ',
                        value = output['Comparison'],
                        height = 32 
                    )
                
                if output['Summary'] is not None:
                    st.markdown('<h3>Summary Output</h3>', unsafe_allow_html=True)
                    st.text_area(
                        'The SQL command to extract the summary is as follows: ',
                        value = output['Summary'],
                        height = 32 
                    )