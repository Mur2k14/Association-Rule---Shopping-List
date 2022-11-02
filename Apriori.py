#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


pip install apriori


# In[4]:


pip install apyori


# In[7]:


dataset = pd.read_csv("/Users/muralik/Desktop/Datasets/Market_Basket_Optimisation.csv",header=None)
dataset


# In[8]:


transactions = []
for i in range(0,7501):
    transactions.append([str(dataset.values[i,j]) for j in range(0,20)])


# In[34]:


from apyori import apriori
rules = apriori(transactions= transactions,min_support=0.003,min_confidence=0.2,min_lift=3,min_length= 2,max_length=2)


# In[35]:


results = list(rules)
results


# In[29]:


left = tuple(result[0][2][0][1])
right = tuple(result[0][2][0][0])
print(f"Left hand side: {left} and Right hand side : {right}")


# In[36]:


def inspect(results):
    lhs         = [tuple(result[2][0][0])[0] for result in results]
    rhs         = [tuple(result[2][0][1])[0] for result in results]
    supports    = [result[1] for result in results]
    confidences = [result[2][0][2] for result in results]
    lifts       = [result[2][0][3] for result in results]
    return list(zip(lhs, rhs, supports, confidences, lifts))
resultsinDataFrame = pd.DataFrame(inspect(results), columns = ['Left Hand Side', 'Right Hand Side', 'Support', 'Confidence', 'Lift'])


# In[37]:


resultsinDataFrame


# In[38]:


resultsinDataFrame.nlargest(n=10,columns="Lift")


# # **ECLAT MODEL**

# In[39]:


def inspect(results):
    lhs         = [tuple(result[2][0][0])[0] for result in results]
    rhs         = [tuple(result[2][0][1])[0] for result in results]
    supports    = [result[1] for result in results]
    return list(zip(lhs, rhs, supports))
resultsinDataFrame = pd.DataFrame(inspect(results), columns = ['Product 1', 'Product 2', 'Support'])


# In[40]:


resultsinDataFrame.nlargest(n=10,columns="Support")


# In[ ]:




