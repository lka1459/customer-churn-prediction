# Olist Customer Analytics and Churn Prediction

A SQL and machine learning project using the Olist Brazilian E-Commerce dataset.

This project explores customer purchasing behaviour using SQLite, SQL queries, pandas, and machine learning. The goal is to practise working with relational databases, performing feature engineering with SQL, and building customer churn prediction models from raw transactional data.

## Project Overview

The project builds a local SQLite database from the Olist dataset and uses SQL to extract customer-level features for machine learning.

The workflow includes:

1. Loading the Olist CSV files into SQLite.
2. Exploring customer, order, review, and product data using SQL.
3. Performing feature engineering to create a customer-level dataset.
4. Creating churn labels based on customer inactivity.
5. Building and evaluating machine learning models.
6. Comparing different classification algorithms.

## Dataset

The dataset used in this project is the Olist Brazilian E-Commerce dataset from Kaggle.

Source:

https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

The dataset contains multiple related tables, including:

* Customers
* Orders
* Order Items
* Products
* Payments
* Reviews
* Sellers

These tables are joined together to create customer-level features for machine learning.

## Features Engineered

Examples of engineered features include:

* Total number of orders
* Total spending
* Average order value
* Average review score
* Average delivery lateness
* Freight costs
* Number of product categories purchased
* Days since last purchase
* Customer location

Customer churn labels are generated based on purchase inactivity.

## Machine Learning Models

The project currently experiments with:

* XGB Booster 
* LightGBM Classifier

Models are implemented using scikit-learn pipelines and ColumnTransformers.

## Technologies Used

* Python
* SQLite
* SQL
* pandas
* NumPy
* scikit-learn
* LightGBM
* XGBoost
* matplotlib
* seaborn
* Jupyter Notebook

## Project Structure

```text
Raw CSV files
↓
SQLite database
↓
SQL analysis
↓
Feature engineering
↓
Customer-level dataset
↓
Churn label generation
↓
Machine learning pipelines
↓
Model evaluation
```

## Project Purpose

This project was created to practise the complete workflow used in many real-world machine learning applications, including database management, SQL querying, feature engineering, classification, and model evaluation.
