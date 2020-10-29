#!/usr/bin/env python
# coding: utf-8

# In[55]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[56]:


dataset = pd.read_csv("Data1.csv")


# In[57]:


dataset.head()


# <h3>Establishment stuff</h3>

# In[58]:


est = dataset[['name','establishment']]
est.head()


# In[59]:


est['establishment'].unique()


# In[60]:


est_list = []
for i in est['establishment'].unique() :
    if len(i)>2:
        est_list.append(i[2:-2])
print(est_list)


# In[61]:


#def func1(x,i):
#    if len(x)>2 :
#        if x[2:-2]==i:
#            return 1
#    return 0
#for i in est_list :
#    est[i] =  est['establishment'].apply(lambda x : func1(x,i))
def func1(x):
    if len(x)>2 :
        return x[2:-2]
    return ''
dataset['establishment'] =  est['establishment'].apply(lambda x : func1(x))


# In[62]:


dataset.head()


# <h3>Highlights Stuff</h3>

# In[63]:


hlts = dataset["highlights"]
hlts.head()


# In[64]:


hlts.nunique()


# In[65]:


h_set = set({})
for i in hlts.unique():
    for j in i[1:-1].split(','):
        h_set.add(j.strip()[1:-1])


# In[66]:


len(h_set)


# In[68]:


def func2(x):
    return [ i.strip()[1:-1] for i in x[1:-1].split(',')]
dataset["highlights"] = dataset["highlights"].apply(func2)


# In[69]:


dataset.head()


# <h3>Getting Rating Based On Data Types</h3>

# In[87]:


mappings = pd.DataFrame(columns=["establishment","highlights","count","mean","std","min","max","25%","50%","75%"])
mappings.head()


# In[93]:


def filtering(establishment, highlight):
    return dataset[(dataset["establishment"]==establishment) & (dataset["highlights"].apply(lambda x : highlight in x))][["aggregate_rating"]].describe()


# In[109]:


i = "Quick Bites"
j = "Lunch"
res = filtering(i,j)["aggregate_rating"]
print(res)
mappings.append({"establishment":i,"highlights":j,"count":res["count"],"mean":res["mean"],"std":res["std"],"min":res["min"],"max":res["max"],"25%":res["25%"],"50%":res["50%"],"75%":res["75%"]}, ignore_index=True)


# In[110]:


for i in est_list :
    for j in list(h_set):
        res = filtering(i,j)["aggregate_rating"]
        mappings = mappings.append({"establishment":i,"highlights":j,"count":res["count"],"mean":res["mean"],"std":res["std"],"min":res["min"],"max":res["max"],"25%":res["25%"],"50%":res["50%"],"75%":res["75%"]}, ignore_index=True)

mappings.head()


# In[111]:


mappings.info()


# In[112]:


mappings.to_csv("mapping_est_hlts.csv")

