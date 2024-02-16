import pandas as pd
import numpy as np
import json

def read_followers_JSON(uploaded_file):
    '''
    """
    Reads followers_1.json file provided by the user (downloaded from instagram) 
    and return the dataframe with user_id, user_link, and timestamp.

    Params:
    uploaded_file -- file obj provided by streamlit.file_uploader

    Returns:
    dataframe -- pandas dataframe with user_id, user_link, and timestamp
    """
    '''
    # Load the JSON file into a Python object
    data = json.load(uploaded_file)
    # Create a Pandas DataFrame from the Python object
    dataframe = pd.json_normalize(data, record_path='string_list_data')
    # Convert the Unix time column to Pandas datetime
    dataframe['timestamp'] = pd.to_datetime(dataframe['timestamp'], unit='s')

    # Rename columns
    dataframe.columns = ['user_link', 'user_id', 'timestamp']
    # Reorder the columns
    dataframe = dataframe[['user_id', 'user_link','timestamp']]

    return dataframe

def read_following_JSON(uploaded_file):
    '''
    """
    Reads following.json file provided by the user (downloaded from instagram) 
    and return the dataframe with user_id, user_link, and timestamp.

    Params:
    uploaded_file -- file obj provided by streamlit.file_uploader

    Returns:
    dataframe -- pandas dataframe with user_id, user_link, and timestamp
    """
    '''
    # Load the JSON file into a Python object
    data = json.load(uploaded_file)
    # Create an empty list to store the string_list_data
    temp_data = []

    # Loop through the relationships_following key in the data dictionary
    for item in data["relationships_following"]:
        # Append the string_list_data value to the list
        temp_data.append(item["string_list_data"])

    # Flatten the list of lists into a single list
    temp_data = [x for sublist in temp_data for x in sublist]

    # Convert the list into a pandas dataframe
    dataframe = pd.DataFrame(temp_data)

    # Convert the Unix time column to Pandas datetime
    dataframe['timestamp'] = pd.to_datetime(dataframe['timestamp'], unit='s')

    # Rename columns
    dataframe.columns = ['user_link', 'user_id', 'timestamp']
    # Reorder the columns
    dataframe = dataframe[['user_id', 'user_link','timestamp']]

    return dataframe