# Import pandas library for data handling and analysis
import pandas as pd

# Import numpy library for numerical operations
import numpy as np

# Import seaborn library for data visualization
import seaborn as sns

# Read the iris dataset from CSV file
df = pd.read_csv(r"C:\Users\tanis\Downloads\iris.csv")

# Display first 5 rows of the dataset
df.head()

# Show dataset information like columns and data types
df.info()

# Check for missing values in each column
df.isnull().sum()

# Display number of rows and columns
df.shape

# Display all column names
df.columns

# Show unique flower varieties
df['variety'].unique()

# Calculate mean values for each variety
df.groupby('variety').mean(numeric_only=True)

# Calculate median values for each variety
df.groupby('variety').median(numeric_only=True)

# Find minimum values for each variety
df.groupby('variety').min()

# Find maximum values for each variety
df.groupby('variety').max()

# Calculate standard deviation for each variety
df.groupby('variety').std(numeric_only=True)

# Create list of sepal length values for Setosa flowers
setosa = df[df['variety'] == 'Setosa']['sepal.length'].tolist()

# Display Setosa sepal length list
setosa

# Create list of sepal length values for Versicolor flowers
versicolor = df[df['variety'] == 'Versicolor']['sepal.length'].tolist()

# Display Versicolor sepal length list
versicolor

# Create list of sepal length values for Virginica flowers
virginica = df[df['variety'] == 'Virginica']['sepal.length'].tolist()

# Display Virginica sepal length list
virginica

# Filter dataset for Setosa flowers
setosa_data = df[df['variety'] == 'Setosa']

# Show statistical summary of Setosa data
setosa_data.describe()

# Filter dataset for Versicolor flowers
versicolor_data = df[df['variety'] == 'Versicolor']

# Show statistical summary of Versicolor data
versicolor_data.describe()

# Filter dataset for Virginica flowers
virginica_data = df[df['variety'] == 'Virginica']

# Show statistical summary of Virginica data
virginica_data.describe()

# Calculate 25th, 50th and 75th percentiles
df.quantile([0.25, 0.50, 0.75], numeric_only=True)

# Plot histogram of petal length values
sns.histplot(df['petal.length'], kde=True)
