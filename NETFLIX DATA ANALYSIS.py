#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
data = pd.read_csv("C:\\Users\\HP\\Downloads\\8. Netflix Dataset.csv")
data.head()


# In[2]:


data.tail(2)


# In[3]:


data.shape


# In[4]:


data.size


# In[5]:


data.columns


# In[6]:


data.dtypes


# In[7]:


data.info()


# In[8]:


# Remove Duplicates


# In[9]:


data[data.duplicated()]


# In[10]:


data.drop_duplicates(inplace = True)


# In[11]:


data.isnull().sum()


# In[12]:


import seaborn as sns


# In[13]:


sns.heatmap(data.isnull())


# In[14]:


# House of Cards 
# Show ID and director


# In[15]:


data[data['Title'].isin(['House of Cards'])]


# In[16]:


data[data['Title'].str.contains('House of Cards')]


# In[17]:


# Year of Highest Tv Shows and Movies Released


# In[18]:


data.dtypes


# In[19]:


data['Date_N'] = pd.to_datetime(data['Release_Date'])


# In[20]:


data.head()


# In[28]:


data['Date_N'].dt.year.value_counts()


# In[22]:


data['Date_N'].dt.year.value_counts().plot(kind = 'bar')


# In[23]:


# Total TV shows & Movies


# In[29]:


data.groupby('Category').Category.count()


# In[25]:


# all movies released In INDIA


# In[44]:


data[(data['Category'] == 'TV Show') & (data["Country"] == "India" )]


# In[43]:


data[(data['Category'] == 'TV Show') & (data["Country"] == "India" )]["Title"]


# In[45]:


#Top 10 Directors of netflix


# In[48]:


data['Director'].value_counts().head(10)


# In[49]:


#all Movies comedy + uk


# In[50]:


data[(data['Category'] == 'Movie') & (data['Type']=='Comedies')]


# In[51]:


# DIFFRENT RATINGS CASTED 


# In[53]:


data['Rating'].nunique()


# In[54]:


data['Rating'].unique()


# In[55]:


# how many tv shows got R ratings after year 2018


# In[57]:


data[(data['Category'] == 'TV Show') & (data['Rating'] == 'R') & (data['Year'] > 2000)]


# In[ ]:




