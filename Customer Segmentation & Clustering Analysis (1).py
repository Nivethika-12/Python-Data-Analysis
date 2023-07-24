#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import warnings 
warnings.filterwarnings('ignore')


# In[2]:


df = pd.read_csv("C:/Users/HP/Downloads/Mall_Customers.csv")


# In[3]:


df.head()


# In[4]:


df.describe()


# In[5]:


sns.displot(df['Annual Income (k$)'])


# In[6]:


df.columns


# In[7]:


columns = [ 'Age', 'Annual Income (k$)','Spending Score (1-100)']


# In[8]:


for i in columns:
    plt.figure()
    sns.displot(df[ i])


# In[9]:


sns.kdeplot(df,x = "Annual Income (k$)",hue="Gender", shade = True)


# In[10]:


for i in columns:
    plt.figure()
    sns.kdeplot(df,x =i,hue="Gender", shade = True)


# In[11]:


columns = [ 'Age', 'Annual Income (k$)','Spending Score (1-100)']
for i in columns:
    plt.figure()
    sns.boxplot (data = df, x = 'Gender', y= df[i])


# In[12]:


df['Gender'].value_counts(normalize = True)


# In[13]:


sns.scatterplot(data = df , x ='Annual Income (k$)', y = 'Spending Score (1-100)')


# In[14]:


#df = df.drop("CustomerID", axis= 1)
sns.pairplot(df, hue = "Gender")


# In[15]:


df.groupby(["Gender"])[ 'Age', 'Annual Income (k$)','Spending Score (1-100)'].mean()


# In[16]:


df.corr()


# In[17]:


sns.heatmap(df.corr(),annot=True,cmap='coolwarm')


# In[37]:


clustering = KMeans(n_clusters = 3)


# In[38]:


clustering.fit(df[['Annual Income (k$)']])


# In[39]:


clustering.labels_


# In[40]:


df['income Cluster'] = clustering.labels_
df.head()


# In[41]:


df['income Cluster'].value_counts()


# In[42]:


clustering.inertia_


# In[43]:


inertia_score = []
for i in range(1,11):
    kmeans = KMeans(n_clusters = i)
    kmeans.fit(df[['Annual Income (k$)']])
    inertia_score.append( kmeans.inertia_)


# In[44]:


inertia_score


# In[45]:


plt.plot(range(1,11),inertia_score)


# In[47]:


df.columns


# In[49]:


df.groupby('income Cluster')['Age', 'Annual Income (k$)',
       'Spending Score (1-100)'].mean()


# In[50]:


clustering1 = KMeans(n_clusters=5)
clustering1.fit(df[['Annual Income (k$)','Spending Score (1-100)']])
df['Spending and Income Cluster'] =clustering1.labels_
df.head()


# In[51]:


intertia_scores2=[]
for i in range(1,11):
    kmeans2=KMeans(n_clusters=i)
    kmeans2.fit(df[['Annual Income (k$)','Spending Score (1-100)']])
    intertia_scores2.append(kmeans2.inertia_)
plt.plot(range(1,11),intertia_scores2)


# In[52]:


centers =pd.DataFrame(clustering1.cluster_centers_)
centers.columns = ['x','y']


# In[53]:


plt.figure(figsize=(10,8))
plt.scatter(x=centers['x'],y=centers['y'],s=100,c='black',marker='*')
sns.scatterplot(data=df, x ='Annual Income (k$)',y='Spending Score (1-100)',hue='Spending and Income Cluster',palette='tab10')
plt.savefig('clustering_bivaraiate.png')


# In[54]:


pd.crosstab(df['Spending and Income Cluster'],df['Gender'],normalize='index')


# In[55]:


df.groupby('Spending and Income Cluster')['Age', 'Annual Income (k$)',
       'Spending Score (1-100)'].mean()


# In[56]:


from sklearn.preprocessing import StandardScaler


# In[57]:


scale = StandardScaler()


# In[58]:


df.head()


# In[59]:


dff = pd.get_dummies(df,drop_first=True)
dff.head()


# In[60]:


dff.columns


# In[61]:


dff = dff[['Age', 'Annual Income (k$)', 'Spending Score (1-100)','Gender_Male']]
dff.head()


# In[62]:


dff = scale.fit_transform(dff)


# In[63]:


dff = pd.DataFrame(scale.fit_transform(dff))
dff.head()


# In[64]:


intertia_scores3=[]
for i in range(1,11):
    kmeans3=KMeans(n_clusters=i)
    kmeans3.fit(dff)
    intertia_scores3.append(kmeans3.inertia_)
plt.plot(range(1,11),intertia_scores3)


# In[65]:


df


# In[66]:


df.to_csv('Clustering.csv')


# In[ ]:




