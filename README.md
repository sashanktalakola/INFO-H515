# INFO-H515 Project

[Application Link](https://h515-ox7ulvo3dq-uc.a.run.app/)
## Overview
The goal of this project is to develop a robust machine learning model capable of accurately predicting housing prices in the Melbourne housing market. Leveraging the rich dataset of over 30,000 entries, encompassing various features such as location, property type, number of rooms, land size, and more, the model aims to provide valuable insights to both home buyers and sellers.

## Data Description
The final iteration of the project uses features -
* Distance - Distance between the property and Melbourne CBD
* Landsize - Area of the property
* Lattitude and Longtitude
* Rooms - Number of Rooms
* Bathroom - Number of Bathrooms
* Bedroom - Number of Bedrooms
* Type - This variable signifies the type of property
    * h - House/Cottage/Villa
    * u - Single Unit/Duplex
    * t - Townhouse

* BedtoBath - This is a variable that is feature engineered, which represents the ration of No. of Bedrooms to No. of bathrooms

Certain outliers values from the variables, `Landsize`, `Rooms`, `Bathroom` and `Bedroom` have been removed

Since the variable `Landsize` was tail heavy it required log-transformatrion. Further, the numeric variables (`Landsize`, `Lattitude`, `Longtitude`, `BedtoBath`) require normalization using the `sklearn - StandardScaler`. While the categorical variables are one-hot encoded using `sklearn - OneHotEncoder`

## Algorithm Description
The deployed application uses Random Forest Regressor for prediction. The hyper-parameters of the model have been tuned and validated using extensive cross-validation and comparison with multiple evaluation metrics.

## Tools Used
* Python (`sklearn`, `pandas` & `seaborn`)
* Jupyter Notebooks
* Streamlit (Frontend)
* APIs (`geopy`)
* Google Cloud Run (Deployment)

## Ethical Concerns
* **Market Manipulation** - The predictions could be used to manipulate the housing market, leading to unfair advantages for certain buyers or sellers. This can be mitigated by monitoring the use of the model and establish guidelines to prevent misuse
* **Socioeconomic Disparities** - The model might exacerbate existing socioeconomic disparities by valuing properties in already affluent areas higher, thus increasing the wealth gap. This can be prevented by designing the model to consider factors that promote social equity.
* **Privacy Concerns** - The use of personal or sensitive data can lead to privacy violations, especially if data is not adequately anonymized. Therefore, strict data anonymization and de-identification practices must be followed.