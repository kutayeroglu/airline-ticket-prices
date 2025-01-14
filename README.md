# airline-ticket-prices
Predict the price of airline ticket prices given day, time, location, etc.

**Dataset**
- https://www.kaggle.com/datasets/dilwong/flightprices/data

**Environment**
- Google Colab
    - sys.path.append('/content/drive/MyDrive/Colab Notebooks/cmpe540/final-project') allows treating the folder as the root of the project.

- Library Versions
    - pandas==2.2.2

**Data Processing**
Departure and arrival time are transformed from 24 h to decimal (e.g., 19.50 means 19:30).

The attributes constitute a part of the 36-dimensional input vector
- First 6 values are:
    - Departure time The departure time in 24h
    - Arrival time : The arrival time in 24h
    - Departure date : A certain date in the days investigated 
    - Days to departure (ndo) : Number of days booking tickets before departure

- 30 values come from the reshaped ticket price sequence




In the paper, they have ndo 1-30 price information for 135 days
but I only have this data for 55 days

