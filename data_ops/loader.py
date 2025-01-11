import os
import pandas as pd
from data_ops.utils import ensure_datadir_exists

def load_data(data_folder_path:str, file_name:str, file_type:str='csv') -> pd.DataFrame:
    # Ensure that data folder exists
    ensure_datadir_exists(data_folder_path)

    data_path = os.path.join(data_folder_path, file_name)

    if file_type == 'csv':
        data = pd.read_csv(data_path)

    return data