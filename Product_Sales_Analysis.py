#!/usr/bin/env python
# coding: utf-8

# In[1]:


#The dataset gives us electronics sales data at Amazon. 
#The dataset is available at https://www.kaggle.com/datasets/edusanketdk/electronics


# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime


# In[3]:


dataset = pd.read_csv('C:\\Users\\HP\\Downloads\\electronics.csv')


# In[4]:


dataset.head(2)


# In[5]:


dataset.shape


# In[6]:


dataset.info()


# In[7]:


pd.to_datetime(dataset['timestamp'])


# In[66]:


dataset['brand'] = dataset['brand'].astype(str)


# In[67]:


dataset['user_attr'] = dataset['user_attr'].astype(str)


# In[68]:


dataset['rating'] = dataset['rating'].astype(float)


# In[69]:


dataset['category'] = dataset['category'].astype(str)


# In[70]:


dataset['user_id'] = dataset['user_id'].astype(str)


# In[71]:


dataset['user_id'] = dataset['user_id'].astype(str)


# In[80]:


dataset['item_id'] = dataset['item_id'].astype(str)


# In[81]:


dataset.replace('nan', np.nan, inplace=True)


# In[73]:


dataset.describe()


# In[74]:


dataset.nunique()


# In[84]:


dataset1 = dataset.dropna()


# In[85]:


dataset1.drop_duplicates()


# In[86]:


# The distribution of ratings 

sns.countplot(x='rating', data=dataset1)


# In[87]:


# what was the best year of sales

dataset1['year'] = pd.DatetimeIndex(dataset1['timestamp']).year

dataset1.groupby('year')['rating'].count().plot(kind='bar')


# In[89]:


# what brand sold the most in 2015

dataset_2015 = dataset1[dataset1['year'] == 2015]

dataset_2015.groupby('brand')['rating'].count().sort_values(ascending=False).head(10).plot(kind='bar')


# In[54]:


# what product sold the most in 2016

dataset1[dataset1['year'] == 2016].groupby('brand')['rating'].count().sort_values(ascending=False).head(10).plot(kind='bar')


# In[55]:


# what product sold the most in 2017

dataset1[dataset1['year'] == 2017].groupby('brand')['rating'].count().sort_values(ascending=False).head(10).plot(kind='bar')


# In[56]:


# what product sold the most in 2018

dataset1[dataset1['year'] == 2018].groupby('brand')['rating'].count().sort_values(ascending=False).head(10).plot(kind='bar')


# In[57]:


# How much was made in sales in the year 2015

dataset1[dataset1['year'] == 2015].groupby('year')['rating'].count().plot(kind='bar')


# In[98]:


get_ipython().run_line_magic('pinfo', 'most')


dataset1.groupby('brand')['rating'].count().sort_values(ascending=False).head(10).plot(kind='bar')


# In[94]:


# What product by category sold the most?

dataset1.groupby('category')['rating'].count().sort_values(ascending=False).head(10).plot(kind='bar')


# In[93]:


# What product by brand name sold the least?

dataset1.groupby('brand')['rating'].count().sort_values(ascending=True).head(10).plot(kind='bar')


# In[92]:


# What product by category sold the least?

dataset1.groupby('category')['rating'].count().sort_values(ascending=True).head(10).plot(kind='bar')


# In[91]:


# category percentage sales

dataset1.groupby('category')['rating'].count().sort_values(ascending=False).head(10).plot(kind='pie')


# In[90]:


# brand percentage sales

dataset1.groupby('brand')['rating'].count().sort_values(ascending=False).head(10).plot(kind='pie')   


# In[ ]:


# conclusion of our analysis

# We can see that the year 2015 had the best sales.

# The month of January had the best sales.

# We can see that the brands Bose and Logitech sold the most

# We can see that the category of Headphones sold the most.

# We can see that the brand name of EINCAR sold the least followed closely with DURAGADGET.

# We can see that the category of Security and Surveillance sold the least.

