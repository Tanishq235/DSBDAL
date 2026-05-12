# Importing required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv(r"C:\Users\tanis\Downloads\iris.csv")

# Display first 5 rows
df.head()

# Dataset information
df.info()

# Checking missing values
df.isnull().sum()

# Dataset dimensions
df.shape

# Display column names
df.columns

# Unique variety names
df['variety'].unique()

# Mean values grouped by variety
df.groupby('variety').mean(numeric_only=True)

# Median values grouped by variety
df.groupby('variety').median(numeric_only=True)

# Minimum values grouped by variety
df.groupby('variety').min()

# Maximum values grouped by variety
df.groupby('variety').max()

# Standard deviation grouped by variety
df.groupby('variety').std(numeric_only=True)

# Numeric list for Setosa
setosa = df[df['variety'] == 'Setosa']['sepal.length'].tolist()
setosa

# Numeric list for Versicolor
versicolor = df[df['variety'] == 'Versicolor']['sepal.length'].tolist()
versicolor

# Numeric list for Virginica
virginica = df[df['variety'] == 'Virginica']['sepal.length'].tolist()
virginica

# Statistical details for Setosa
setosa_data = df[df['variety'] == 'Setosa']
setosa_data.describe()

# Statistical details for Versicolor
versicolor_data = df[df['variety'] == 'Versicolor']
versicolor_data.describe()

# Statistical details for Virginica
virginica_data = df[df['variety'] == 'Virginica']
virginica_data.describe()

# Percentiles for dataset
df.quantile([0.25, 0.50, 0.75], numeric_only=True)

# Histogram of petal length
sns.histplot(df['petal.length'], kde=True)

plt.title("Petal Length Distribution")

plt.show()
