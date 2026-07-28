# STAT4365E Final Project
A machine learning pipeline for predicting customer churn using the Tel Customer Churn dataset.

## Table of Contents
* [Project Overview](#project-overview)
* [Dataset](#dataset)
* [Project Structure](#project-structure)
* [Setup & Installation](#setup--installation)
* [Notebook Walkthrough](#notebook-walkthrough)
* [Key Findings](#key-findings)
* [Technologies Used](#technologies-used)

## Project Overview
Customer churn is one of the most important business metrics for subscription-based companies. Being able to predict which customers are likely to leave allows companies to proactively retain customers through trageted marketing or customer support.

This project builds several machine learning models to classify whether a customer will churn based on demographic information, services subscribed, and account information.

The project was developed using Jupyter notebooks and later refactored into a reproducible Python pipeline.

## Dataset
The [Telco Customer Churn](https://www.kaggle.com/datasets/blastchar/telco-customer-churn) dataset contains information about 7,043 customers of a telecommunications company.

Each customer includes:
* Demographic information
* Services Subscribed To
* Billing Information
* Contract Information

Target Variable:
Churn:
* 0 = customer stayed
* 1 = customer left

The raw dataset contains one-missing value issue in total_charges, which is handled during data cleaning.

## Project Structure
```
CustomerChurnPrediction/
├── data
│   ├── clean
│       └── dataset.csv
├── notebooks
│   ├── Data_Exploration_7_8.ipynb
│   ├── Data_Wrangling_7_7.ipynb
│   └── Feature_and_Model_Selection_7_22.ipynb
├── outputs
│   ├── figures
│   │   ├── churn_distribution.png
│   │   ├── contract_churn.png
│   │   ├── dependents_churn.png
│   │   ├── device_protection_churn.png
│   │   ├── gender_churn.png
│   │   ├── heatmap.png
│   │   ├── internet_service_churn.png
│   │   ├── monthly_charges_by_churn.png
│   │   ├── online_backup_churn.png
│   │   ├── online_security_churn.png
│   │   ├── partner_churn.png
│   │   ├── payment_method_churn.png
│   │   ├── senior_citizen_churn.png
│   │   ├── tech_support_churn.png
│   │   ├── tenure_by_churn.png
│   │   ├── tenure_vs_monthly_charges.png
│   │   ├── tenure_vs_total_charges.png
│   │   └── total_charges_by_churn.png
│   └── models
│       ├── gradient_boosting.joblib
│       ├── logistic_regression.joblib
│       ├── random_forest.joblib
│       ├── scaler.joblib
│       ├── selector.joblib
│       └── svm.joblib
├── ProjectProposal_MSP02.pdf
├── README.md
├── requirements.txt
└── src
    ├── data.py
    ├── exploration.py
    ├── __init__.py
    ├── main.py
    ├── modeling.py
    └── wrangling.py
```
## Setup & Installation
Clone the repository
```bash
git clone https://github.com/liatlas/CustomerChurnPrediction/tree/main
cd CustomerChurnPrediction
```
Create a virtual environment (recommended)
```bash
python -m venv .venv
source .venv/bin/activate
```
Install dependencies
```bash
pip install -r requirements.txt
```
### Running the Pipeline
Execute the complete workflow
```bash
cd src
python main.py
```
The pipeline performs the following steps:
1. Downlodads the dataset from Kaggle.
2. Cleans and preprocesses the data.
3. Saves the cleaned dataset.
4. Generates exploratory data analysis visualizations
5. Trains multiple machine learning models.
6. Evaluates each model.
7. Saves trained models for future use.
The trained models are saved in 
```
outputs/models/
```
and all visualizations are saved in 
```
outputs/figures/
```

## Notebook Walkthrough
### Data_Wrangling_7_7.ipynb
This notebook performs data cleaning and preprocessing.
Tasks include:
* Loading the raw dataset
* Renaming columns to snake_case
* Removing unnecessary columns
* Handling missing values  
* Converting data types
* Encoding binary variables
* Saving the cleaned dataset

### Data_Exploration_7_8.ipynb
Exploratory Data Analysis_7_8.ipynb includes:
* Churn distribution
* Tenure distribution
* Monthly and total charges
* Correlation heatmap 
* Scatter plots
* Boxplots
* Churn by contract type
* Churn by internet service
* Churn by additional services

### Feature_and_Model_Selection_7_22.ipynb
This notebook focuses on feature engineering and machine learning
The workflow includes:
* One-hot encoding categorical variables
* Train/Test split
* Feature scaling
* Mutual Information feature selection
* Modeling training
* Model evaluation
* Feature importance analysis

models evaluated:
* logistic regression 
* random forest 
* gradient boosting 
* support vector machine

### Model Performance:
| model | precision | recall | f1-score |
| logistic regression | 0.79 | 0.8 | 0.79 |
| SVC | 0.77 | 0.79 | 0.77 |
| Gradient Boosting | 0.77 | 0.78 | 0.77 |
| Random Forest | 0.75 | 0.76 | 0.79 |

Out of the models that were evaluated, logistic regression had the best recall, 0.8, on the test set.

## Key Findings
* Customer tenure is strongly associated with churn
* Customers with month-to-month contracts are considerably more likely to churn than customers with longer-term contracts
* Monthly chrages are positively associated with churn
* Customers lacking services such as Tech Support and Online Security have higher churn rates
* Logistic Regression provided the best overall predictive performance among the evaluated models.
* Gradient Boosintg and SVM achieved comparable performance while Random Forest performed slightly worse on this dataset

## Technologies Used
### Languages
* Python
### Data Analysis 
* pandas
* NumPy
### Visualization
* Matplotlib
* Seaborn
### Machine Learning
* scikit-learn
### Data Acquisition
* Kaggle
### Development
* Jupyter
* uv

