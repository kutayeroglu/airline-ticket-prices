# Predicting Airline Ticket Prices with Historical Time Series Data
Predict the price of airline ticket prices given day, time, location remaining days to flight etc.

# Environment and Library Versions

## **Environment**
- **Platform:** Google Colab  
  - Configured to treat a specific folder as the project root:  
    ```python
    sys.path.append('/content/drive/MyDrive/Colab Notebooks/cmpe540/final-project')
    ```

## **Library Versions**
- **Python:** `3.10.12`
- **Pandas:** `2.2.2`
- **Torch:** `2.5.1+cu121`
- **NumPy:** `1.26.4`
- **Scikit-learn:** `1.6.0`
- **Matplotlib:** `3.8.0`


# GPU and CUDA Driver Information

## **GPU Details**
```
+---------------------------------------------------------------------------------------+
| NVIDIA-SMI 535.104.05             Driver Version: 535.104.05   CUDA Version: 12.2     |
|-----------------------------------------+----------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |         Memory-Usage | GPU-Util  Compute M. |
|                                         |                      |               MIG M. |
|=========================================+======================+======================|
|   0  NVIDIA A100-SXM4-40GB          Off | 00000000:00:04.0 Off |                    0 |
| N/A   33C    P0              45W / 400W |      2MiB / 40960MiB |      0%      Default |
|                                         |                      |             Disabled |
+-----------------------------------------+----------------------+----------------------+

```

# Project Details

## **Dataset**
- [Flight Prices Dataset on Kaggle](https://www.kaggle.com/datasets/dilwong/flightprices/data)

## **Paper (Approach Reference)**
- [Predictive Approach Paper (Springer)](https://link.springer.com/chapter/10.1007/978-3-030-63823-8_86)

## **Report**
- [Overleaf Report Link](https://www.overleaf.com/read/jvsgnjvrrwgg#3084d4)



## **Source Code Overview**

### **data_subset.ipynb**
- **Purpose:** Downloads historical price data from Kaggle.
- **Process:** Filters for the top 5 most frequent flight routes.
- **Output:** Saves the filtered data to Google Drive.

### **data_preparation.ipynb**
- **Purpose:** Prepares the dataset for modeling.
- **Process:** Performs preprocessing, feature creation, and saves model-ready data.
- **Output:** Processed dataset saved to Google Drive.

### **baseline_model_train.ipynb**
- **Purpose:** Trains and evaluates a baseline model.
- **Model:** Random Forest Regressor.
- **Metrics:** Reports RMSE.

### **hybrid_model_train.ipynb**
- **Purpose:** Trains the hybrid model.
- **Model:** LSTM-CNN architecture.
- **Output:** Best performing model, loss over epoch plot, and training logs

### **model_evaluation.ipynb**
- **Purpose:** Evaluates the performance of the hybrid model.
- **Metrics:** Reports RMSE and accuracy.


