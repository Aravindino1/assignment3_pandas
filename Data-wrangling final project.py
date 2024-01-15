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


# In[5]:


column_of_interest=['continent','location','date','total_cases','total_deaths','gdp_per_capita','human_development_index']


# In[6]:


df=c_data[column_of_interest]


# In[ ]:


#5. Data Cleaning 
#a. Remove all duplicates observations 
#b. Find missing values in all columns 
#c. Remove all observations where continent column value is missing Tip : using subset parameter in dropna 
#d. Fill all missing values with 0


# In[8]:


df.shape


# In[9]:


df.drop_duplicates()


# In[20]:


df.isnull().sum()


# In[14]:


df.dropna(subset=['continent'], inplace=True)


# In[19]:


df.fillna(0, inplace = True)


# In[ ]:


#6. Date time format : 
#a. Convert date column in datetime format using pandas.to_datetime
#b. Create new column month after extracting month data from date column.


# In[23]:


df["date"].apply(pd.to_datetime)


# In[26]:


df["month"]=pd.DatetimeIndex(df['date']).month


# In[ ]:


#7. Data Aggregation: 
#a. Find max value in all columns using groupby function on 'continent' column Tip: use reset_index() after applying groupby 
#b. Store the result in a new dataframe named 'df_groupby'. (Use df_groupby dataframe for all further analysis)


# In[31]:


df1= df.groupby("continent").max()
df_groupby=df1.reset_index()


# In[32]:


df_groupby


# In[ ]:


#9.Feature Engineering : 
#a. Create a new feature 'total_deaths_to_total_cases' by ratio of 'total_deaths' column to 'total_cases'


# In[34]:


df_groupby["total_deaths_to_total_cases"]=df_groupby["total_deaths"]/df_groupby["total_cases"]


# In[35]:


df_groupby


# In[ ]:


#9. Data Visualization : 
#a. Perform Univariate analysis on 'gdp_per_capita' column by plotting histogram using seaborn dist plot. 
#b. Plot a scatter plot of 'total_cases' & 'gdp_per_capita' 
#c. Plot Pairplot on df_groupby dataset. 
#d. Plot a bar plot of 'continent' column with 'total_cases' . Tip : using kind='bar' in seaborn catplot


# In[36]:


import seaborn as sns


# In[38]:


sns.histplot(data=df_groupby, x="gdp_per_capita")


# In[39]:


sns.scatterplot(data=df_groupby, x="total_cases",y="gdp_per_capita")


# In[40]:


sns.pairplot(data=df_groupby)


# In[41]:


sns.catplot(data=df_groupby, x="continent",y="total_cases",kind="bar")


# In[43]:


#Save the df_groupby dataframe in your local drive using pandas.to_csv
df_groupby.to_csv("df_groupby")


# In[ ]:




