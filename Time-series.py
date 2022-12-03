#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
data = pd.read_csv('C:/Users/HP/Downloads/DailyDelhiClimateTest.csv')
data


# In[7]:


data['meantemp'].plot()


# In[8]:


data['new'] = data['meantemp'].mean()
data


# In[ ]:


data=data.drop(['moving_avg'],axis=1)
data


# In[58]:


data=data.drop(['new'],axis=1)
data


# In[9]:


from datetime import date,time,datetime
from datetime import timedelta


# In[10]:


data.isnull().sum()


# In[11]:


data.info()


# In[12]:


import matplotlib.pyplot as plt
x = data['date']
y = data['meantemp']
plt.plot(x,y)


# In[13]:


x = data['date']
y = data['humidity']
plt.plot(x,y,color='red')


# In[14]:


x = data['date']
y = data['wind_speed']
plt.plot(x,y,color='orange')


# In[15]:


data['moving_avg_meantemp']=data['meantemp'].rolling(window=3).mean()
data


# In[17]:


plt.plot(data['date'],data['moving_avg_meantemp'],color = 'red')


# In[20]:


data['date']=pd.to_datetime(data['date'])
data


# In[68]:


data.info()


# In[19]:


data['date_month'] = data['date'].dt.to_period('M')
data


# In[21]:


data1 = data[['date_month','moving_avg_meantemp']]
data1


# In[79]:


data1.info()


# In[22]:


plt.plot(data['date'],data['meantemp'],label = 'meantemp')
plt.plot(data['date'],data['moving_avg_meantemp'],label = 'moving_avg_meantemp')
plt.legend()
plt.show()


# In[ ]:





# In[23]:


data.info()


# In[24]:


import seaborn as sns


# In[25]:


dff = data[['meantemp','humidity']]
sns.heatmap(dff.corr(),annot=True)


# In[26]:


dff = data[['meantemp','wind_speed']]
sns.heatmap(dff.corr(),annot=True)


# In[27]:


dff = data[['meantemp','meanpressure']]
sns.heatmap(dff.corr(),annot=True)


# In[28]:


dff = data[['humidity','meanpressure']]
sns.heatmap(dff.corr(),annot=True, color='red')


# In[ ]:




