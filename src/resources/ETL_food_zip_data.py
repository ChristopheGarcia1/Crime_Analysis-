#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Dependencies and Setup
import pandas as pd


# In[2]:


food_data = pd.read_csv("./food_desert.csv")
food_data.head()


# In[3]:


zip_data = pd.read_csv("./zip_tract.csv")
zip_data.head()


# In[4]:


food_data.dropna()


# In[5]:


food_data_clean = food_data[['CensusTract', 'State', 'County', 'Urban', 'LILATracts_1And10', 'LILATracts_halfAnd10', 'LILATracts_1And20', 'LILATracts_Vehicle']]
food_data_clean.head()


# In[6]:


zip_data_clean = zip_data[['ZIP']]
zip_data_clean['CensusTract'] = zip_data[['TRACT']]
zip_data_clean.head()


# In[7]:


food_final = food_data_clean.merge(zip_data_clean, how='inner', on='CensusTract')
food_final.head(10)


# In[8]:


food_final_tx = food_final.loc[food_final['State'] == 'Texas']
food_final_tx.head(10)


# In[9]:


food_final_tx.to_csv('food_final_tx.csv', index=False)


# In[ ]:




