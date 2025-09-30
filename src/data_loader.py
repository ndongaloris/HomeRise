# 📦 Import the pandas library, which provides powerful data structures
# and functions for data manipulation and analysis.
import pandas as pd

def load_data(path="data/raw/MapProjects_data.csv"):
    """
    Loads a CSV file containing housing project data into a pandas DataFrame.

    Parameters:
    ----------
    path : str
        The relative or absolute path to the CSV file. Defaults to the raw data folder.

    Returns:
    -------
    df : pandas.DataFrame
        A structured DataFrame containing the loaded dataset, ready for cleaning or visualization.
    
    Notes:
    ------
    - This function abstracts the file loading logic, making it reusable across scripts.
    - By setting a default path, it supports quick testing and avoids hardcoding in other modules.
    - If the file path changes or multiple datasets are introduced, this function can be extended
      with validation, logging, or error handling.
    """
    
    # 🧭 Read the CSV file from the specified path into a DataFrame.
    # This assumes the file is properly formatted with headers.
    df = pd.read_csv(path)
    
    # 🔁 Return the loaded DataFrame so it can be passed to downstream functions
    # like data cleaning, transformation, or visualization.
    return df
