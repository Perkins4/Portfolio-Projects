#!/usr/bin/env python
# coding: utf-8

# ### Importing data and packages

# In[1]:


import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import numpy as np
import matplotlib.mlab as mlab
data = pd.read_csv('world-happiness-report-2021.csv')


# ### Taking a look at the dataset info

# In[2]:


data.head()


# In[7]:


data.tail()


# In[8]:


data.info()


# In[9]:


data.describe()


# ### Cleaning the data

# #### First I am going to take out columns that wont be needed for my analysis. The Standard error of ladder score, upperwhisker, lowerwhisker, and "Explained by" columns will be dropped. 

# In[23]:


data.drop(['Standard error of ladder score', 'upperwhisker','lowerwhisker'], axis = 1)


# #### Checking for null data

# In[3]:


data.isna().sum()


# In[6]:


# Are there any Outliers?
data.boxplot(column=['Ladder score'])


# #### no null data to clean so I will procede to data analysis
# #### First I will look into which countries have the highest and lowest happiness scores

# In[12]:


High20 = data.groupby('Country name')['Ladder score'].sum().sort_values(ascending = False).head(20)


# In[13]:


High20


# In[38]:


Low20 = data.groupby('Country name')['Ladder score'].sum().sort_values().head(20)


# In[40]:


Low20


# #### From listing the top/low 20 it is clear that European countries are high on the happiness score and African/middle eastern countries are low. There are the exceptions to this claim, such as Canada/US and India. Going forward I will conduct correlation tests to see which factors have signifiance on the Ladder score. 

# In[8]:


sns.regplot(x = "Logged GDP per capita", y = "Ladder score", data = data)


# In[17]:


Plot = data.plot.scatter(x = 'Social support' , y = 'Ladder score', c = 'Freedom to make life choices', cmap = 'coolwarm')


# #### we can see here the amount of social support positively impacts the 'Ladder score'. Also the Freedom to make choices is positively impacting the Ladder score with a few outliers.

# ### Correlation matrix

# In[10]:


corrdata = data.drop(['Explained by: Log GDP per capita','Explained by: Social support','Explained by: Healthy life expectancy','Explained by: Freedom to make life choices', 'Explained by: Generosity','Explained by: Perceptions of corruption', 'Dystopia + residual', 'Ladder score in Dystopia', 'lowerwhisker', 'upperwhisker', 'Standard error of ladder score'], axis =1)


# In[11]:


corrdata.corr(method='pearson').style.format("{:.2}").background_gradient(cmap=plt.get_cmap('coolwarm'), axis=1)


# In[12]:


corrdata.corr(method = 'spearman')


# #### With this correlation matrix we can answer which factors have the most influence on others. Suprisingly generousity has a low correlation with all columns. the amount of giving around people does not significantly affect their happiness. From this data the Freedom to choose is a large factor. A factor that would help in this dataset would be population density. It would be a interesting find to see if having a large population density plays a role in happiness rankings.  

# In[34]:


regionplot = sns.relplot(
    data=data,
    x="Healthy life expectancy", y="Ladder score",
    hue="Regional indicator",
    palette='coolwarm', sizes=(40, 400),
)


# In[36]:


regionplot = sns.relplot(
    data=data,
    x="Perceptions of corruption", y="Ladder score",
    hue="Regional indicator",
    palette='coolwarm', sizes=(40, 400),
)


# #### Mapping out data

# In[13]:


GDP_map = dict(type = 'choropleth',
            locations = data['Country name'].to_list(),
            locationmode = 'country names',
            colorscale= 'Portland',
            text= data['Country name'].to_list(),
            z=(data['Logged GDP per capita']).to_list(),
            colorbar = {'title':'GDP per capita', 'len':250,'lenmode':'pixels' })


# In[14]:


gdp_map = go.Figure(data = [GDP_map])


# In[32]:


gdp_map.show()


# In[15]:


SS_map = dict(type = 'choropleth',
            locations = data['Country name'].to_list(),
            locationmode = 'country names',
            colorscale= 'Portland',
            text= data['Country name'].to_list(),
            z=(data['Social support']).to_list(),
            colorbar = {'title':'Social support', 'len':250,'lenmode':'pixels' })


# In[16]:


ssmap = go.Figure(data = [SS_map])


# In[17]:


ssmap.show()


# In[21]:


Top20temp = data.sort_values(by=['Healthy life expectancy'], ascending=False)[:20]


LE_map = dict(type = 'choropleth',
            locations = Top20temp['Country name'].to_list(),
            locationmode = 'country names',
            colorscale= 'Portland',
            text= Top20temp['Country name'].to_list(),
            z=(Top20temp['Healthy life expectancy']).to_list(),
            colorbar = {'title':'Life expectancy', 'len':250,'lenmode':'pixels' })


# In[22]:


le_map = go.Figure(data = [LE_map])


# In[23]:


le_map.show()


# In[24]:


Bottom20temp = data.sort_values(by=['Healthy life expectancy'])[:20]


BLE_map = dict(type = 'choropleth',
            locations = Bottom20temp['Country name'].to_list(),
            locationmode = 'country names',
            colorscale= 'Portland',
            text= Bottom20temp['Country name'].to_list(),
            z=(Bottom20temp['Healthy life expectancy']).to_list(),
            colorbar = {'title':'Life expectancy', 'len':250,'lenmode':'pixels' })


# In[25]:


ble_map = go.Figure(data = [BLE_map])
ble_map.show()


# In[27]:


sns.swarmplot(x="Ladder score", y="Logged GDP per capita", data=data)


# In[ ]:




