# STAT4365E Final Project
The exploration and modeling of Telco customer churn records

## Table of Contents
* [Project Overview](#project-overview)
* [Dataset](#dataset)
* [Project Structure](#project-structure)
* [Setup & Installation](#setup--installation)
* [Notebook Walkthrough](#notebook-walkthrough)
* [Key Findings](#key-findings)
* [Technologies Used](#technologies-used)

## Project Overview
## Dataset
The [Telco Customer Churn](https://www.kaggle.com/datasets/blastchar/telco-customer-churn) dataset contains customer data about Telco, a company that provides home phone and internet services to 7043 customers. Each observation (row) represents one customer, and the target variable is the churn column, True if the customer has decided to no longer purchase services from the company and False if not. For each observation, there is also demographic information, information on the services they have, and account information.

## Project Structure
<!--TODO-->

## Setup & Installation
```bash
git clone https://github.com/liatlas/CustomerChurnPrediction/tree/main
cd CustomerChurnPrediction
pip install -r requirements.txt
```
## Notebook Walkthrough
### Data_Wrangling_7_7.ipynb
Loading the data for the first time. Checks for issues with the dataset like:
* Improper column names
* Incorrect data types
* Missing data

Then:
* Renames columns to snake casing
* Corrects data types
* Drops 11 observations
* Saves cleaned data to data/clean/dataset.csv for later exploration
### Data_Exploration_7_8.ipynb

## Key Findings
<!--TODO-->
## Technologies Used
<!--TODO-->
