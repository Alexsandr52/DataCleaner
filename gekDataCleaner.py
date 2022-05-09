# openpyxl pandas numpy
import pandas as pd
import numpy as np

def get_dataframe(dataframe, col_name=None, sep=None):
    """get dataframe for easy use of the library

    Args:
        dataframe (dataframe/path): dataframe or path for dataframe 
        col_name (int, optional): to output a specific column. Defaults to None.
        sep (str, optional): to read csv files if sep is not normal. 
    Returns:
        pandas.DataFrame: returns a DataFrame for further use by other functions
    """

    if type(dataframe) == pd.core.frame.DataFrame:
        result = dataframe

    elif type(dataframe) == str:
        # try to open dataframe
        try:
            if dataframe[-3:] == 'csv':
                if sep is not None and len(sep) != 0: dataframe = pd.read_csv(dataframe, sep = sep)
                else: dataframe = pd.read_csv(dataframe)

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

    # to retern selected columns
    if type(col_name) == str and col_name in result.columns or type(col_name) == list and all(el in result.columns for el in col_name):
        result = result[col_name]

    return result



def reduce_mem_usage(dataframe, copy=True, logs=True):
    """reduce memory usage

    Args:
        dataframe (dataframe/path): dataframe or path for dataframe 
        copy (bool, optional): write changes to original dataframe. Defaults to True.
        logs (bool, optional): show logs about memory usage. Defaults to True.

    Returns:
        dataframe: new dataframe or original dataframe with changes
    """
    # not to get an error
    dataframe = get_dataframe(dataframe)

    if type(dataframe) != pd.core.frame.DataFrame:
        return False

    # to see the result but not change the original dataframe
    if copy:
        df = dataframe.copy()
    else:
        df = dataframe

    start_mem = df.memory_usage().sum() / 1024**2

    for col in df.columns:
        col_type = df[col].dtype
        
        if col_type != object:
            c_min = df[col].min()
            c_max = df[col].max()
            if str(col_type)[:3] == 'int':
                if c_min > np.iinfo(np.int8).min and c_max < np.iinfo(np.int8).max:
                    df[col] = df[col].astype(np.int8)
                elif c_min > np.iinfo(np.int16).min and c_max < np.iinfo(np.int16).max:
                    df[col] = df[col].astype(np.int16)
                elif c_min > np.iinfo(np.int32).min and c_max < np.iinfo(np.int32).max:
                    df[col] = df[col].astype(np.int32)
                elif c_min > np.iinfo(np.int64).min and c_max < np.iinfo(np.int64).max:
                    df[col] = df[col].astype(np.int64)  
            else:
                if c_min > np.finfo(np.float16).min and c_max < np.finfo(np.float16).max:
                    df[col] = df[col].astype(np.float16)
                elif c_min > np.finfo(np.float32).min and c_max < np.finfo(np.float32).max:
                    df[col] = df[col].astype(np.float32)
                else:
                    df[col] = df[col].astype(np.float64)
        else:
            df[col] = df[col].astype('category')

    end_mem = df.memory_usage().sum() / 1024**2

    if logs:
        print(f'Memory usage of dataframe is {round(start_mem,2)} MB')
        print(f'Memory usage after optimization is: {round(end_mem,2)} MB')
        print(f'Decreased by {round(100 * (start_mem - end_mem) / start_mem, 1)}%')
    
    return df





# 'exsel_test.xlsx'
# df = pd.read_csv('housing.csv')
print(reduce_mem_usage('data\exsel_test.xlsx'))
# print(get_dataframe('data\exsel_test.xlsx', 'age'))
