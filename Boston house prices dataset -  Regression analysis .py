#!/usr/bin/env python
# coding: utf-8

# In[42]:


from sklearn.datasets import load_boston
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np


# In[2]:


boston = load_boston()
print(boston.data.shape)


# In[3]:


dir(boston)


# In[4]:


print(boston.DESCR)


# In[5]:


boston.data


# In[6]:


type(boston.data)


# In[7]:


boston.data.shape


# In[8]:


boston.feature_names


# In[9]:


boston.target


# In[10]:


data = pd.DataFrame(data = boston.data, columns= boston.feature_names)
data ["PRICE"] = boston.target


# In[11]:


data.head()


# In[12]:


data.tail()


# In[13]:


data.count()


# In[14]:


pd.isnull(data).any()


# In[15]:


data.info()


# In[16]:


plt.figure(figsize = (10,6))
plt.hist(data["PRICE"], bins =50, ec = "black")
plt.xlabel(" price in 000s")
plt.ylabel ("no of houses")
plt.show()


# In[17]:


plt.figure(figsize = (10,6))
sns.distplot(data['PRICE'], bins = 50 , hist = True, kde= False)
plt.show()


# In[18]:


plt.figure(figsize = (10,6))
sns.distplot(data['RM'])
plt.xlabel(" Average number of rooms")
plt.ylabel ("no of houses")
plt.show()


# In[19]:


data['RM'].mean()


# In[20]:


plt.figure(figsize = (10,6))
sns.distplot(data['RAD'])
plt.xlabel(" Accecibility to high ways")
plt.ylabel ("no of houses")
plt.show()


# In[21]:


data['RAD']


# In[24]:


data['RAD'].value_counts()


# In[28]:


frequency = data['RAD'].value_counts()
plt.figure(figsize = (10,6))
plt.xlabel(" Accecibility to high ways")
plt.ylabel ("no of houses")
type(frequency)
frequency.index
plt.bar(frequency.index, height =frequency )
plt.show()


# In[29]:


data['CHAS'].value_counts()


# In[31]:


data['PRICE'].min()


# In[33]:


data['PRICE'].max()


# In[34]:


data.min()


# In[36]:


data.mean()


# In[37]:


data.median()


# In[38]:


data.describe()


# In[39]:


data['PRICE'].corr(data['RM'])


# In[40]:


data['PRICE'].corr(data['PTRATIO'])


# In[41]:


data.corr()


# In[49]:


mask = np.zeros_like(data.corr())
traingle_indicies = np.triu_indices_from(mask)
mask[traingle_indicies] = True
mask


# In[57]:


plt.figure(figsize =(16,10))
sns.heatmap(data.corr(), mask = mask, annot = True, annot_kws = {"size" : 14})
sns.set_style('white')
plt.show()


# In[ ]:




