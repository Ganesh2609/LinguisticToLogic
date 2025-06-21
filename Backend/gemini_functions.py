import sys
sys.path.append('..\Backend')

import os 
import json 
from dotenv import load_dotenv
import google.generativeai as genai
import prompts



# Function to select the key and activate key rotation
def setup_api_key():
    
    # Loading the key to use
    load_dotenv()
    num_keys = 11   # Number of api keys
    
    # Load the key
    with open('..\Backend\key_rotation.json', 'r') as f:
        rot_config = json.load(f)
    curr_rotation = rot_config['CURRENT_ROTATION']
    
    # Loading env variables and configuring the api key for gemini pro
    key_name = "GOOGLE_API_KEY_" + str(curr_rotation)
    genai.configure(api_key=os.getenv(key_name))

    # Updating to use the next key
    next_rotation = (curr_rotation+1)%num_keys
    rot_config['CURRENT_ROTATION'] = next_rotation
    with open('..\Backend\key_rotation.json', 'w') as f:
        json.dump(rot_config, f, indent=4)
        
        

# Function to get the response from gemini-1.0-pro
def get_gemini_10_response(question:str, prompt:str):
    setup_api_key()
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt, question])
    return response.text

# Function to get the response from gemini-1.5-pro
def get_gemini_15_response(question:str, prompt:str):
    setup_api_key()
    model = genai.GenerativeModel('gemini-1.5-pro')
    response = model.generate_content([prompt, question])
    return response.text



# Function to generate the field values from the input question
def generate_field_values(question:str):
    prompt = prompts.analysis_prompt()
    response = get_gemini_10_response(question=question, prompt=prompt)
    return response  

#Function to generate the general response
def generate_general_output(table_name:str, question:str, structure:str=None):
    prompt = prompts.general_prompt(table_name=table_name, structure=structure)
    response = get_gemini_10_response(question=question, prompt=prompt)
    return response

# Function to generate image response
def generate_image_output(table_name:str, question:str, structure:str=None):
    prompt = prompts.image_prompt(table_name=table_name, structure=structure)
    response = get_gemini_10_response(question=question, prompt=prompt)
    return response

# Function to generate plot response
def generate_plot_output(table_name:str, question:str, structure:str=None):
    prompt = prompts.plot_prompt(table_name=table_name, structure=structure)
    response = get_gemini_10_response(question=question, prompt=prompt)
    return response

# Function to generate comparison response
def generate_summary_output(data, question:str):
    prompt = prompts.summary_prompt(data=data)
    response = get_gemini_10_response(question=question, prompt=prompt)
    return response

# Function to generate the statement for general responses
def generate_statement_general(data, question:str):
    prompt = prompts.data_prompt(data)
    response = get_gemini_10_response(question=question, prompt=prompt)
    return response

# Function to generate the query for summary
def generate_summary_sql_output(table_name:str, question:str, structure:str=None):
    prompt = prompts.summary_sql_prompt(table_name=table_name, structure=structure)
    response = get_gemini_10_response(question=question, prompt=prompt)
    return response