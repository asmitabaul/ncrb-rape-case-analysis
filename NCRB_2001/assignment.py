# importing required libraries
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# loading data
data = pd.read_csv('/Users/asmitabaul/Desktop/files/NCRB_2001_Table_28.csv')
data.sample(5)

#sample preview
data.info()

#identify null values
Total = data.isnull().sum()
Total

#reoplace null with mean values
data.fillna(data.mean(numeric_only=True), inplace=True)
total_after = data.isnull().sum()
total_after

#identify duplicates
duplicate = data.duplicated()
total_duplicates = duplicate.sum()
total_duplicates

#delete duplicates
data.drop_duplicates(inplace = True)
data

# Plot a bar chart for total rape cases by state
plt.figure(figsize=(12, 8))
sns.barplot(x='States/UTs/Cities', y='No. of Victims (Total Rape Cases) - Total Victims', data=data)
plt.xticks(rotation=90)
plt.title('Total rape cases by state in 2018')
plt.xlabel('State')
plt.ylabel('Number of rape cases')
plt.tight_layout()
plt.show()
    
# Plot a pie chart showing the distribution of rape cases by state
plt.figure(figsize=(20, 20))
state_counts = data['States/UTs/Cities'].value_counts()
plt.pie(state_counts, labels=state_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Distribution of Rape Cases by State in 2018')
plt.axis('equal')
plt.show()


# Plot a heatmap to visualize correlations between numeric columns
# Select only the numeric columns for correlation calculation
numeric_data = data.select_dtypes(include=[float, int])
# Compute the correlation matrix for numeric columns only
correlation_matrix = numeric_data.corr()
# Plot the heatmap
plt.figure(figsize=(20, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix of Rape Cases Data')
plt.show()

# Plot a box plot to identify outliers in 'Rape(Total)'
plt.figure(figsize=(8, 6))
sns.boxplot(x=data['No. of Victims (Total Rape Cases) - Total Victims'])
plt.title('Box Plot of Total Rape Cases')
plt.xlabel('Number of Rape Cases')
plt.show()
