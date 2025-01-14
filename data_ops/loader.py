import os
import pandas as pd
from data_ops.utils import ensure_datadir_exists

def load_data(data_folder_path:str, file_name:str, file_type:str='csv') -> pd.DataFrame:
    # Ensure that data folder exists
    ensure_datadir_exists(data_folder_path)

    if file_type not in file_name: 
        file_name = file_name + '.' + file_type
    data_path = os.path.join(data_folder_path, file_name)

    if file_type == 'csv':
        data = pd.read_csv(data_path)

    print(f"\nData loaded from {data_path}")
    print(f"Data shape: {data.shape}")

    return data