#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns


# In[2]:


dataset = pd.read_csv('zomato.csv')


# In[3]:


dataset.info()


# In[4]:


dataset.columns


# In[5]:


dataset.isna().sum()


# In[6]:


dataset.nunique()


# In[7]:


dataset.head()


# In[8]:


dataset.sort_values(by = "res_id").head(8)


# In[9]:


dataset["establishment"]


# In[10]:


dataset["aggregate_rating"].unique()


# In[11]:


dataset["rating_text"].unique()


# In[12]:


dataset["photo_count"].nunique()


# In[13]:


dataset["takeaway"].unique()


# In[14]:


dataset["delivery"].unique()


# In[15]:


dataset["opentable_support"].unique()


# In[16]:


data = dataset.drop(['res_id','url','address','zipcode','country_id','locality_verbose','city','city_id','currency','rating_text','photo_count','takeaway','opentable_support','locality'], axis=1)


# In[17]:


data.head()


# In[18]:


data.isna().sum()


# In[19]:


data = data.dropna()


# In[20]:


data.info()


# In[21]:


data.to_csv('Data1.csv',index=False)

