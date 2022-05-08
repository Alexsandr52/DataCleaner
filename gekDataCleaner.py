# openpyxl pandas numpy
import pandas as pd
import numpy as np

def get_dataframe(dataframe, col_name = None):
    """get dataframe for easy use of the library

    Args:
        dataframe (string or pandas.DataFrame, required): required
        col_name (int, optional): to output a specific column. Defaults to None.
    Returns:
        pandas.DataFrame: returns a DataFrame for further use by other functions
    """
    
    if type(dataframe) == pd.core.frame.DataFrame:
        result = dataframe
    
    elif type(dataframe) == str:
        try:
            if dataframe[-3:] == 'csv':
                dataframe = pd.read_csv(dataframe)
            elif dataframe[-4:] == 'xlsx':
                dataframe = pd.read_excel(dataframe)
            else:
                print(f'Can\' read {dataframe}. Try to unpack yourself ...')
                return False

            result = dataframe

        except FileNotFoundError:
            return print(f'file {dataframe} not found, or the path to the file is incorrect')
        except ImportError:
            return print('Required modules not installed (pandas, numpy, openpyxl(if data is in excel file))')
    
    if type(col_name) == str and col_name in result.columns or type(col_name) == list and all(el in result.columns for el in col_name):
        return result[col_name]

    return result

# 'exsel_test.xlsx'
df = pd.read_csv('housing.csv')
print(get_dataframe('housing.csv', ['longitude', 'housing_median_age']))