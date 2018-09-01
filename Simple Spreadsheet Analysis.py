
# coding: utf-8

# The team wants to find the month they're likely to contact the most clients, so they can schedule a product upgrade announcement. Which month does the team tend to contact the greatest percentage of its clients?

# In[1]:


import numpy as np
import pandas as pd


# In[5]:


#loading dataset 
df=pd.read_csv(r'C:\Users\fangc\Documents\Udacity\DataAnalyst.csv')


# In[6]:


#take a look dateset
df.head()


# In[7]:


#checking datatype
df.info()


# In[8]:


#change columns name
df.rename(columns=lambda x:x.strip().lower().replace(" ","_"),inplace=True)


# In[11]:


# fixing data type
df.date_of_contact=pd.to_datetime(df.date_of_contact)


# In[12]:


df.info()


# In[18]:


# extracting month from data 
df['month']=df.date_of_contact.dt.month


# In[35]:


#groupby month and then conunt the number for contact
df.groupby('month',as_index=False)['date_of_contact'].count()


# According of the result, October is the month to contact the greatest percentage of its clients 
