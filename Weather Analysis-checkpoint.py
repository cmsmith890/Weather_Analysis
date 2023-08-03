#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy
import scipy.stats
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use("bmh")

data = pd.read_csv("storm_data_search_results.csv")
data.head() 


# In[2]:


data.columns


# In[3]:


print(data.describe())

# Histogram of magnitudes
plt.hist(data['MAGNITUDE'], bins=20, edgecolor='black')
plt.xlabel('Magnitude')
plt.ylabel('Frequency')
plt.title('Distribution of Magnitudes')
plt.show()


# In[4]:


# Convert date strings to datetime objects
data['BEGIN_DATE'] = pd.to_datetime(data['BEGIN_DATE'])

# Plot the number of events over time
plt.plot(data['BEGIN_DATE'], data['MAGNITUDE'], marker='o', linestyle='-', label='Magnitude')
plt.xlabel('Date')
plt.ylabel('Magnitude')
plt.title('Magnitude Variation Over Time')
plt.legend()
plt.show()


# In[5]:


# Calculate correlation matrix
correlation_matrix = data.corr()

# Heatmap to visualize the correlation matrix
plt.figure(figsize=(12, 8))
plt.imshow(correlation_matrix, cmap='coolwarm', interpolation='nearest')
plt.colorbar()
plt.xticks(range(len(correlation_matrix)), correlation_matrix.columns, rotation=90)
plt.yticks(range(len(correlation_matrix)), correlation_matrix.columns)
plt.title('Correlation Matrix')
plt.show()


# In[6]:


# Check for missing values
print(data.isnull().sum())

# Remove rows with missing values
data.dropna(inplace=True)

# Or impute missing values with mean or median (if applicable)
data['MAGNITUDE'].fillna(data['MAGNITUDE'].mean(), inplace=True)

