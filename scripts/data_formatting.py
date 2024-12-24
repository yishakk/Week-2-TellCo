import pandas as pd

def format_data(data):
    print("Formatting data ...")
    
    data = data.rename(columns={
        "column1": "new_column1",
        "column2": "new_column2"
    })

    if 'date_column' in data.columns:
        data['date_column'] = pd.to_datetime(data['date_column'], errors='coerce')
    
    print("Formatting data Done.")
    return data