import os
import pandas as pd
from datetime import date, datetime


def log(func):
    def wrapper(*args, **kwargs):
        original_result = func(*args, **kwargs)

        username = os.getlogin()
        func_name = func.__name__
        formatted_date = date.today().strftime("%d-%m-%Y")
        formatted_time = datetime.now().strftime("%H:%M:%S")
        
        if os.path.exists("logs.csv"):
            file_df = pd.read_csv('logs.csv')
            new_id = len(file_df)
            new_row = pd.DataFrame({
                'id': [new_id],
                'username': [username],
                'func_name': [func_name],
                'formatted_date': [formatted_date],
                'formatted_time': [formatted_time]
            })
            new_row.to_csv('logs.csv', mode='a', header=False, index=False)
        else:
            df = pd.DataFrame({
                'id': [0],
                'username': [username],
                'func_name': [func_name],
                'formatted_date': [formatted_date],
                'formatted_time': [formatted_time]
            })
            df.to_csv('logs.csv', index=False)

        return original_result
    return wrapper


@log
def hello():
    print('Hello')

hello()