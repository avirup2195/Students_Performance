#!/usr/bin/env python
# coding: utf-8

# In[3]:


import os
os.getcwd()


# In[17]:


os.chdir("F:/datasets/students_performance")


# In[25]:


import pandas as pd
data=pd.read_csv("StudentsPerformance.csv")
import numpy as np


# In[21]:



data.info()


# In[44]:


data['Total_Marks']=data['math score']+data['reading score']+data['writing score']
data


# In[40]:


avg_math=np.mean(data['math score'])
avg_read=np.mean(data['reading score'])
avg_write=np.mean(data['writing score'])
avg_score=np.mean(data['Total_Marks'])


# In[41]:


print("average math score :",avg_math)
print("average reading score :",avg_read)
print("average writing score :",avg_write)
print("average  score :",avg_score)


# In[48]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
from pandas import Series,DataFrame
obj=(data.iloc[:,5:9])
obj


# In[58]:


import seaborn as sns
plt.figure(figsize=(18,8))
plt.subplot(1, 4, 1)
plt.title('MATH SCORES')
sns.boxplot(y='math score',data=data,palette='magma')
plt.subplot(1, 4, 2)
plt.title('READING SCORES')
sns.boxplot(y='reading score',data=data,palette='cool')
plt.subplot(1, 4, 3)
plt.title('WRITING SCORES')
sns.boxplot(y='writing score',data=data,palette='YlOrRd')
plt.subplot(1,4,4)
plt.title("Total_Marks")
sns.boxplot(y='Total_Marks',data=data)
plt.show()


# In[57]:


plt.figure(figsize=(18,8))
plt.subplot(1, 4, 1)
sns.barplot(x='test preparation course',y='math score',data=data,hue='gender')
plt.title('MATH SCORES')
plt.subplot(1, 4, 2)
sns.barplot(x='test preparation course',y='reading score',data=data,hue='gender')
plt.title('READING SCORES')
plt.subplot(1, 4, 3)
sns.barplot(x='test preparation course',y='writing score',data=data,hue='gender')
plt.title('WRITING SCORES')
plt.subplot(1,4,4)
plt.title('Total Marks')
sns.barplot(x='test preparation course',y='Total_Marks',data=data,hue='gender')
plt.show()


# In[61]:


plt.figure(figsize=(20,8))
plt.subplot(1, 4, 1)
sns.barplot(x='test preparation course',y='math score',data=data,hue='lunch',palette='viridis')
plt.title('MATH SCORES')
plt.subplot(1, 4, 2)
sns.barplot(x='test preparation course',y='reading score',data=data,hue='lunch',palette='viridis')
plt.title('READING SCORES')
plt.subplot(1, 4, 3)
sns.barplot(x='test preparation course',y='writing score',data=data,hue='lunch',palette='viridis')
plt.title('WRITING SCORES')
plt.subplot(1,4,4)
plt.title('TOTAL MARKS')
sns.barplot(x='test preparation course',y='Total_Marks',data=data,hue='lunch',palette='viridis')
plt.show()


# In[64]:


data[(data['math score'] > 90) & (data['reading score'] > 90) & (data['writing score']>90)].sort_values(by=['Total_Marks'],ascending=False)


# In[ ]:


### The first two students are either brilliant or they have resort to some unfair means since their test preparation is zero


# In[67]:


plt.figure(figsize=(20,10))
plt.subplot(1, 4, 1)
plt.title('MATH SCORES')
sns.barplot(x='race/ethnicity',y='math score',data=data,hue='gender')
plt.subplot(1, 4, 2)
plt.title('READING SCORES')
sns.barplot(x='race/ethnicity',y='reading score',data=data,hue='gender')
plt.subplot(1, 4, 3)
plt.title('WRITING SCORES')
sns.barplot(x='race/ethnicity',y='writing score',data=data,hue='gender')
plt.subplot(1,4,4)
plt.title('Total Marks')
sns.barplot(x='race/ethnicity',y='Total_Marks',data=data,hue='gender',palette='Paired')
plt.show()


# In[ ]:





# In[70]:


fig,ax=plt.subplots()
sns.countplot(x='parental level of education',data=data)
plt.tight_layout()
fig.autofmt_xdate()


# In[ ]:


### Performance of students(Total Marks) depends on their parental level of education


# In[72]:


fig,ax=plt.subplots()
sns.barplot(x=data['parental level of education'],y='Total_Marks',data=data)
fig.autofmt_xdate()

