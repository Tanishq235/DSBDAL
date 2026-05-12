# Import all the python Libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Load the Dataset into pandas data frame

pd.read_csv(r"C:\Users\tanis\Downloads\titanic_train.csv")

# Display complete dataset
df


# Display top 5 rows

df.head()   # It's showing top 5 result


# Display bottom 5 rows

df.tail()   # It's showing bottom 5 result


# Calculating missing values

df.isnull().sum()   # Calculating the Null values


# Visualizing missing values using Heatmap

sns.heatmap(df.isnull(),
            yticklabels=False,
            cbar=False,
            cmap='viridis')


# Calculating missing values in Age column

df['Age'].isnull().sum()


# Calculating missing values in Cabin column

df['Cabin'].isnull().sum()


# Get some initial statistics

df.describe()


# Dataset information

df.info()


# Check dimensions of dataset

df.shape


# Check data types

df.dtypes
