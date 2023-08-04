#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install ipython-sql


# In[2]:


get_ipython().run_line_magic('load_ext', 'sql')


# In[10]:


import csv, sqlite3

con = sqlite3.connect("socioeconomic.db")
cur = con.cursor()


# In[9]:


get_ipython().system('pip install -q pandas==1.1.5')


# In[4]:


get_ipython().run_line_magic('sql', 'sqlite:///socioeconomic.db')


# In[5]:


import pandas
df = pandas.read_csv('https://data.cityofchicago.org/resource/jcxq-k9xf.csv')
df.to_sql("chicago_socioeconomic_data", con, if_exists='replace', index=False,method="multi")


# In[6]:


get_ipython().run_line_magic('sql', 'SELECT * FROM chicago_socioeconomic_data limit 5;')


# In[18]:


get_ipython().run_line_magic('pinfo', 'dataset')


# In[7]:


get_ipython().run_line_magic('sql', 'SELECT COUNT(*) FROM chicago_socioeconomic_data;')


# In[ ]:


#How many community areas in Chicago have a hardship index greater than 50.0?


# In[8]:


get_ipython().run_line_magic('sql', 'SELECT COUNT(*) FROM chicago_socioeconomic_data WHERE hardship_index > 50.0;')


# In[19]:


#What is the maximum value of hardship index in this dataset?


# In[11]:


get_ipython().run_line_magic('sql', 'SELECT MAX(hardship_index) FROM chicago_socioeconomic_data;')


# In[12]:


#Which community area which has the highest hardship index?¶


# In[13]:


get_ipython().run_line_magic('sql', 'select community_area_name from chicago_socioeconomic_data where hardship_index = ( select max(hardship_index) from chicago_socioeconomic_data )')


# In[14]:


# Which Chicago community areas have per-capita incomes greater than $60,000?


# In[15]:


get_ipython().run_line_magic('sql', 'SELECT community_area_name FROM chicago_socioeconomic_data WHERE per_capita_income_ > 60000;')


# In[ ]:


# scatter plot using the variables per_capita_income_ and hardship_index. Explain the correlation between the two variables.


# In[16]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns

income_vs_hardship = get_ipython().run_line_magic('sql', 'SELECT per_capita_income_, hardship_index FROM chicago_socioeconomic_data;')
plot = sns.jointplot(x='per_capita_income_',y='hardship_index', data=income_vs_hardship.DataFrame())


# In[ ]:




