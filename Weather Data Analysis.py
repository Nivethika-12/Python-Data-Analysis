#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[4]:


data  =  pd.read_csv("C:\\Users\\HP\\Downloads\\1. Weather Data.csv")


# In[6]:


data.head()


# In[7]:


data.shape


# In[10]:


data.index


# In[13]:


data.columns


# In[14]:


data.dtypes


# In[17]:


data['Weather'].unique()


# In[18]:


data.nunique()


# In[19]:


data.count()


# In[22]:


data['Weather'].value_counts()


# In[23]:


data.info()


# In[26]:


# Unique wind speed


# In[27]:


data.head(1)


# In[30]:


data['Wind Speed_km/h'].unique()


# In[31]:


data['Wind Speed_km/h'].nunique()


# In[32]:


# Number of times Weather is exactly clear


# In[39]:


data[data.Weather == "Clear"].count()


# In[40]:


# Times wind speed was extractly 4Km/h


# In[41]:


data.head(1)


# In[51]:


data[data['Wind Speed_km/h'] == 4].count()


# In[53]:


# Null Values


# In[56]:


data.isnull().sum()


# In[52]:


# Mean value of visibility


# In[57]:


data.Visibility_km.mean()


# In[58]:


# Standard Deviation Press_kPa


# In[59]:


data.Press_kPa.std()


# In[60]:


# Variance of Rel Hum_%


# In[61]:


data['Rel Hum_%'].var()


# In[62]:


# All the instances snow was recorded


# In[63]:


data.Weather.value_counts()


# In[67]:


data[data.Weather == "Snow"].count()


# In[68]:


# Wind Speed above 24  and visibility 25


# In[72]:


data[(data['Wind Speed_km/h'] > 24) & (data.Visibility_km == 25)].count()


# In[74]:


##Mean Value of each column against weather condition


# In[77]:


data.groupby('Weather').mean()


# In[78]:


# Minimum & Maximum Value of each column


# In[79]:


data.groupby('Weather').min()


# In[80]:


data.groupby('Weather').max()


# In[81]:


# Weather condition is clear 
# humidity grater than 40
# visibility above 40


# In[82]:


data.head(1)


# In[84]:


data[(data.Weather == "Clear") & (data["Rel Hum_%"] > 40) & (data.Visibility_km < 40)]


# In[ ]:




