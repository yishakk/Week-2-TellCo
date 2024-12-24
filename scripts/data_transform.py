import numpy as np

def transform_dat(data):
    print("Data Transformation ...")

    if 'size_in_bytes' in data.columns:
        data['size_in_mb'] = data['size_in_bytes'] / (1024 * 1024)

    if 'value_column' in data.columns:
        data['log_value'] = np.log1p(data['value_column'])

    print("Data Transformation Done.")
    return data