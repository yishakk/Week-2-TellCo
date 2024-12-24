import pandas as pd

def read_csv(file_path):
    print("Reading CSV ...")
    try:
      data = pd.read_csv(file_path)
      print("Reading CSV Done.")
      return data
    except Exception as e:
      print(f"Error during data extraction: {e}")
      return None