#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Dependencies and Setup
import pandas as pd


# In[2]:


weather_data = pd.read_csv("./weather_data.csv")
weather_data.head()


# In[3]:


weather_data_cleaned = weather_data[['dt', 'dt_iso', 'temp', 'wind_speed', 'weather_main', 'pressure', 'humidity']]
weather_data_cleaned.sample(20)


# In[4]:


weather_data_cleaned['time_occ'] = weather_data_cleaned['dt_iso'].str[11:19]
weather_data_cleaned['occ_date'] = weather_data_cleaned['dt_iso'].str[8:10]+'/'+weather_data_cleaned['dt_iso'].str[5:7]+'/'+weather_data_cleaned['dt_iso'].str[0:4]
weather_data_cleaned.head()


# In[5]:


weather_data_cleaned.to_csv('weather_data_cleaned.csv', index=False)


# In[ ]:




