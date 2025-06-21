import sys
sys.path.append('..\Backend')

import gemini_functions
import database_functions


# Function to get field value outputs
def generate_final_field_values(question:str):
    
    # Passing through the model
    model_output = gemini_functions.generate_field_values(question=question)
    
    # Splitting the string
    split_token = '<split-token>'
    parts = model_output.split(split_token)
    
    # Run until it is in the correct format
    while len(parts) != 4:
        model_output = gemini_functions.generate_field_values(question=question)
        parts = model_output.split(split_token)
    
    # Process for dict
    image = parts[0].strip().lower() == 'true'
    plot = parts[1].strip().lower() == 'true'
    comparison = parts[2].strip().lower() == 'true'
    summary = parts[3].strip().lower() == 'true'
    
    # Create and return the dictionary
    return {
        "Image": image,
        "Plot": plot,
        "Comparison": comparison,
        "Summary": summary
    }
    
    
    
    
# Function to get general output
def generate_final_general_output(table_name:str, question:str, structure:str=None):
    model_output = gemini_functions.generate_general_output(table_name=table_name, question=question, structure=structure)
    data = database_functions.execute_query(model_output)
    statement = gemini_functions.generate_statement_general(data=data, question=question)
    return {
        'SQL Query' : model_output,
        'Statement' : statement,
        'Data' : data
    }
    
    
    
# Function to get custom general output
def generate_custom_general_output(table_name:str, question:str, structure:str=None):
    model_output = gemini_functions.generate_general_output(table_name=table_name, question=question, structure=structure)
    statement = gemini_functions.generate_statement_general(data=data, question=question)
    return {
        'SQL Query' : model_output,
        'Statement' : statement,
    }


# Function to get image output
def generate_final_image_output(table_name:str, question:str, structure:str=None):
    
    # Getting output and splitting it
    model_output = gemini_functions.generate_image_output(table_name=table_name, question=question, structure=structure)
    split_token = '<split-token>'
    parts = model_output.split(split_token)
    
    # Run until it is in the correct format
    while len(parts) != 2:
        model_output = gemini_functions.generate_image_output(table_name=table_name, question=question, structure=structure)
        parts = model_output.split(split_token)
    
    # Process for dict
    query = parts[0].strip()
    statement = parts[1].strip()
    if query.lower() == 'none':
        query = None 
    
    # Create and return dictionary
    return {
        'SQL Query' : query,
        'Statement' : statement
    }
    
    

# Function to process plot outputs
def generate_final_plot_output(table_name:str, question:str, structure:str=None):
    
    # Getting output and splitting it
    model_output = gemini_functions.generate_plot_output(table_name=table_name, question=question, structure=structure)
    split_token = '<split-token>'
    parts = model_output.split(split_token)
    
    # Run until it is in the correct format
    while len(parts) != 6:
        model_output = gemini_functions.generate_plot_output(table_name=table_name, question=question, structure=structure)
        parts = model_output.split(split_token)
    
    # Process for dict
    plots = ['histogram', 'bar-plot', 'line-plot', 'pie-chart', 'scatter-plot']
    query = parts[0].strip()
    plot_type = parts[1].strip().lower()
    title = parts[2].strip()
    xlabel = parts[3].strip()
    ylabel = parts[4].strip()
    statement = parts[5].strip()
    
    if plot_type == 'pie-chart':
        xlabel = None
        ylabel = None
    
    # Create and return dictionary
    return {
        'SQL Query' : query,
        'Plot type' : plot_type,
        'Title' : title,
        'Xlabel' : xlabel,
        'Ylabel' : ylabel,
        'Statement' : statement
    }
    
    

# Function to generate the comparisons
def generate_final_comparison_output(table_name:str, question:str, structure:str=None):
    model_output = gemini_functions.generate_general_output(table_name=table_name, question=question, structure=structure)
    data = database_functions.execute_query(model_output)
    comparison_output = gemini_functions.generate_summary_output(data=data, question=question)
    return {
        'SQL Query' : model_output,
        'Comparison table' : data,
        'Comparison summary' : comparison_output
    }



# Function to generate the custom comparisons
def generate_custom_comparison_output(table_name:str, question:str, structure:str=None):
    model_output = gemini_functions.generate_general_output(table_name=table_name, question=question, structure=structure)
    return model_output
    


# Function to generate the summary
def generate_final_summary_output(table_name:str, question:str, structure:str=None):
    model_output = gemini_functions.generate_summary_sql_output(table_name=table_name, question=question, structure=structure)
    data = database_functions.execute_query(model_output)
    summary1 = data.describe()
    summary2 = gemini_functions.generate_summary_output(data=data, question=question)
    return {
        'SQL Query' : model_output,
        'Summary description' : summary1,
        'Summary text' : summary2
    }
    
    
    
    
# Function to generate the custom summary
def generate_custom_summary_output(table_name:str, question:str, structure:str=None):
    model_output = gemini_functions.generate_summary_sql_output(table_name=table_name, question=question, structure=structure)
    return model_output
    
    
    
    
# Function to generate all the final outputs
def generate_final_prototype_output(table_name:str, question:str, structure:str=None):
    
    # Finding field values
    field_values = generate_final_field_values(question=question) 
    
    # For image
    if field_values['Image']:
        img_model = generate_final_image_output(table_name=table_name, question=question, structure=structure)
        if img_model['SQL Query'] is None:
            img_output = img_model
        else:
            output_img = database_functions.retrieve_images(img_model['SQL Query'])
            img_output = {
                'SQL Query' : img_model['SQL Query'],
                'Statement' : img_model['Statement'],
                'Image' : output_img
            }
    else:
        img_output = None
    
    # For plots
    if field_values['Plot']:
        plot_model = generate_final_plot_output(table_name=table_name, question=question, structure=structure)
        output_plot = database_functions.execute_plots(plot_model)
        plot_output = {
            'SQL Query' : plot_model['SQL Query'],
            'Statement' : plot_model['Statement'],
            'Plot' : output_plot
        }
    else:
        plot_output = None
    
    # For comparison
    if field_values['Comparison']:
        comparison_output = generate_final_comparison_output(table_name=table_name, question=question, structure=structure)
    else:
        comparison_output = None
    
    # For summary
    if field_values['Summary']:
        summary_output = generate_final_summary_output(table_name=table_name, question=question, structure=structure)
    else:
        summary_output = None
    
    # For general outputs
    if not(field_values['Image'] or field_values['Plot'] or field_values['Comparison'] or field_values['Summary']):
        general_output = generate_final_general_output(table_name=table_name, question=question, structure=structure)
    else:
        general_output = None
    
    
    # Final output
    final_output = {
        'Field Values' : field_values,
        'General' : general_output,
        'Image' : img_output,
        'Plot' : plot_output,
        'Comparison' : comparison_output,
        'Summary' : summary_output
    }
    
    return final_output 
    
    
    
    
# Function to generate all the final custom outputs
def generate_final_custom_output(table_name:str, question:str, structure:str=None):
    
    # Finding field values
    field_values = generate_final_field_values(question=question) 
    
    # For image
    if field_values['Image']:
        img_output = generate_final_image_output(table_name=table_name, question=question, structure=structure)
    else:
        img_output = None
    
    # For plots
    if field_values['Plot']:
        plot_output = generate_final_plot_output(table_name=table_name, question=question, structure=structure)
    else:
        plot_output = None
    
    # For comparison
    if field_values['Comparison']:
        comparison_output = generate_custom_comparison_output(table_name=table_name, question=question, structure=structure)
    else:
        comparison_output = None
    
    # For summary
    if field_values['Summary']:
        summary_output = generate_custom_summary_output(table_name=table_name, question=question, structure=structure)
    else:
        summary_output = None
    
    # For general outputs
    if not(field_values['Image'] or field_values['Plot'] or field_values['Comparison'] or field_values['Summary']):
        general_output = generate_custom_general_output(table_name=table_name, question=question, structure=structure)
    else:
        general_output = None
    
    
    # Final output
    final_output = {
        'Field Values' : field_values,
        'General' : general_output,
        'Image' : img_output,
        'Plot' : plot_output,
        'Comparison' : comparison_output,
        'Summary' : summary_output
    }
    
    return final_output 