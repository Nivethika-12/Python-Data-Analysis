#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import seaborn as sns
sns.set()


# In[4]:


raw_data = pd.read_csv("C:\\Users\\HP\\Downloads\\1.04.+Real-life+example (1).csv")
raw_data.head()


# In[6]:


raw_data.describe(include = "all")


# In[8]:


data = raw_data.drop(['Model'], axis=1)
data.describe(include = "all")


# In[10]:


data.isnull().sum()


# In[12]:


data_no_mv = data.dropna(axis = 0)
data_no_mv.describe(include="all")


# In[14]:


sns.displot(data_no_mv["Price"])


# In[16]:


q = data_no_mv["Price"].quantile(0.99)
data_1 = data_no_mv[data_no_mv["Price"]<q]
data_1.describe (include= "all")


# In[17]:


sns.displot(data_1["Price"])


# In[18]:


sns.displot(data_1["Mileage"])


# In[20]:


q = data_no_mv["Mileage"].quantile(0.99)
data_2 = data_no_mv[data_no_mv["Mileage"]<q]
sns.displot(data_2["Mileage"])


# In[21]:


sns.displot(data_no_mv["EngineV"])


# In[22]:


data_3 = data_2[data_2["EngineV"]<6.5]


# In[23]:


sns.displot(data_3["EngineV"])


# In[24]:


sns.displot(data_no_mv["Year"])


# In[26]:


q = data_3['Year'].quantile(0.01)
data_4 = data_3[data_3['Year']>q]


# In[27]:


sns.displot(data_4["Year"])


# In[28]:


data_cleaned = data_4.reset_index(drop = True)


# In[29]:


data_cleaned.describe(include="all")


# In[31]:


log_price = np.log(data_cleaned["Price"])
data_cleaned["Price"] = log_price
data_cleaned


# In[34]:


f, (ax1, ax2, ax3) = plt.subplots(1, 3, sharey=True, figsize =(15,3))
ax1.scatter(data_cleaned['Year'],data_cleaned['Price'])
ax1.set_title('Price and Year')
ax2.scatter(data_cleaned['EngineV'],data_cleaned['Price'])
ax2.set_title('Price and EngineV')
ax3.scatter(data_cleaned['Mileage'],data_cleaned['Price'])
ax3.set_title('Price and Mileage')


plt.show()


# In[ ]:




