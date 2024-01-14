#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[1]:


import numpy as np
import pandas as pd


# In[ ]:


#1. Import the dataset using Pandas from above mentioned url.


# In[2]:


url ="https://raw.githubusercontent.com/SR1608/Datasets/main/covid-data.csv"


# In[3]:


c_data=pd.read_csv(url)


# In[5]:


# 2. High Level Data Understanding:
""" a. Find no. of rows & columns in the dataset
 b. Data types of columns.
 c. Info & describe of data in dataframe."""


# In[7]:


c_data.shape


# In[8]:


c_data.dtypes


# In[9]:


c_data.info()


# In[10]:


c_data.describe()


# In[ ]:


#3. Low Level Data Understanding :
""" a. Find count of unique values in location column.
 b. Find which continent has maximum frequency using values counts.
 c. Find maximum & mean value in 'total_cases'.
 d. Find 25%,50% & 75% quartile value in 'total_deaths'.
 e. Find which continent has maximum'human_development_index'.
 f. Find which continent has minimum 'gdp_per_capita'."""


# In[18]:


c_data["location"].nunique()


# In[25]:


c_data["continent"].value_counts()


# In[22]:


c_data["total_cases"].max()


# In[23]:


c_data["total_cases"].mean()


# In[26]:


c_data["total_deaths"].quantile(0.25)


# In[27]:


c_data["total_deaths"].quantile(0.50)


# In[28]:


c_data["total_deaths"].quantile(0.75)


# In[43]:


idx = c_data.groupby('continent')['human_development_index'].max()


# In[44]:


idx


# In[46]:


gdp=c_data.groupby('continent')['gdp_per_capita'].min()
gdp


# In[ ]:


#4. Filter the dataframe with only this columns['continent','location','date','total_cases','total_deaths','gdp_per_capita','human_development_index']


# In[47]:


column_of_interest=['continent','location','date','total_cases','total_deaths','gdp_per_capita','human_development_index']


# In[50]:


df=c_data[column_of_interest]


# In[ ]:





# In[ ]:




