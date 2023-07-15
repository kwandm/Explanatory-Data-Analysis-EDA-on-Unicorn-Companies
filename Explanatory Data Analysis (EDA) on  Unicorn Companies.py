#!/usr/bin/env python
# coding: utf-8

# ## Basic Explanatory on Data Unicorn Companies

# In[134]:


# import the necessary libraries
import numpy as np
import pandas as pd

# for visuals
import seaborn as sns
import matplotlib.pyplot as plt


# In[77]:


# Load and read data file
'''inside the quotation is a file path of the data file'''
unicorn_data = pd.read_csv(r'C:\Users\Admin\OneDrive\Desktop\Quantum Analytics April Cohort\Python\Python Dataset\Unicorn_Companies.csv') # pd.read_csv(r'') for csv file format and pd.read_excel(r'') for excel file format
unicorn_data


# In[78]:


# check the first 5 rows
unicorn_data.head()


# In[80]:


# check the last 5 rows
unicorn_data.tail()


# ## Data Inspection and Manipulation

# In[81]:


# view the shape of the data
unicorn_data.shape


# In[82]:


# view the columns
unicorn_data.columns


# In[83]:


# check the data types
unicorn_data.dtypes


# In[84]:


# view info about data
unicorn_data.info()


# In[85]:


# check for missing values
unicorn_data.isnull()


# In[86]:


unicorn_data.isna()


# In[87]:


unicorn_data.isnull().sum()


# In[88]:


# replace the null values with zeros
unicorn_data.replace(np.nan, "0", inplace = True)


# In[89]:


unicorn_data.isnull().sum()


# In[99]:


# check for rows or columns with null values
nan_df = unicorn_data[unicorn_data.isna().any(axis=1)]
nan_df.head()


# In[100]:


# visualise the missing values
plt.figure(figsize = (10, 5))
plt.title('Visualising Missing Values')
sns.heatmap(unicorn_data.isnull(), cbar = True, cmap = 'magma_r')
plt.show()


# In[91]:


# check for duplicated value
print(unicorn_data.duplicated().sum())


# In[92]:


# view the summary statistics of the dataset
unicorn_data.describe()


# In[93]:


unicorn_data.nunique()


# In[94]:


industry_counts = unicorn_data['Industry'].value_counts().head(5)
print(industry_counts)


# In[95]:


# Convert "Date Joined" column to datetime format
unicorn_data['Date Joined'] = pd.to_datetime(unicorn_data['Date Joined'], format='%Y-%m-%d')

# Change the date format to "dd-mm-yyyy"
unicorn_data['Date Joined'] = unicorn_data['Date Joined'].dt.strftime('%d-%m-%Y')

unicorn_data


# ## Exploratory Data Analysis: Relationship, Insights and Visualisation
# - Univariate Analysis, Bivariate Analysis and Multivariate Analysis

# In[101]:


unicorn_data.columns


# In[103]:


# how many listings are there per location
count_listing = unicorn_data['location'].value_counts()
count_listing


# In[105]:


# Countries that have the most unicorns
country_counts = unicorn_data['Country'].value_counts()
print(country_counts)


# In[126]:


# Visualize the countries that have the most unicorns

# Count the number of companies per country
country_counts = unicorn_data['Country'].value_counts().head(10)

# Plotting the bar graph
plt.figure(figsize=(10, 6))
sns.barplot(x=country_counts.index, y=country_counts.values)
plt.xlabel('Countries')
plt.ylabel('Number of Companies')
plt.title('Number of Companies per Country')
plt.xticks(rotation=45)
for i, v in enumerate(country_counts.values):
    plt.text(i, v, str(v), ha='center', va='bottom')
plt.show()


# ### Observation
# - United States has the highest number of Unicorn Companies totalling 562.

# In[ ]:





# In[199]:


# Cities that are industry hubs

city_counts = unicorn_data['City'].value_counts()
print(city_counts)


# In[202]:


# Top 10 cities that are industry hubs
city_counts = unicorn_data['City'].value_counts().head(10)
print(city_counts)


# In[207]:


# Visualize top 10 cities that are industry hubs

city_counts = unicorn_data['City'].value_counts().head(10)

# Create bar chart
plt.figure(figsize=(10, 6))
ax = city_counts.plot(kind='barh')
ax.set_xlabel('Number of Unicorns')
ax.set_ylabel('City')
ax.set_title('Top 10 Cities that are Industry Hubs')

# Add data labels
for p in ax.patches:
    ax.annotate(str(p.get_width()), (p.get_width(), p.get_y() + p.get_height() / 2), ha='left', va='center')

# Show the plot
plt.tight_layout()
plt.show()


# ### Observation
# - The city with the highest number of unicorn companies is San Francisco indicating its significance as an industry hub.

# In[ ]:





# In[205]:


# Last 10 cities that are industry hubs
city_counts = unicorn_data['City'].value_counts().tail(10)
print(city_counts)


# In[ ]:





# In[197]:


# top industries
industry_counts = unicorn_data['Industry'].value_counts().head(5)
print(industry_counts)


# In[128]:


# Visualize top three industries with the highest number of comapnies

top_industries = industry_counts.head(3)

# Plotting the pie chart
plt.figure(figsize=(8, 6))
plt.pie(top_industries, labels=top_industries.index, autopct='%1.1f%%', startangle=90)
plt.title('Top Three Industries with the Highest Number of Companies')
plt.axis('equal')

plt.show()


# ### Observation
# -The top industries among unicorn companies in the dataset are Fintech, Internet software & services, and E-commerce & direct-to-consumer.

# In[129]:


# Visualize top 3 countries
country_counts = unicorn_data['Country'].value_counts().head(5)
print(country_counts)


# In[130]:


# Visualize the top three countries witht e highest number of companies
top_countries = country_counts.head(3)

# Plotting the pie chart
plt.figure(figsize=(8, 6))
plt.pie(top_countries, labels=top_countries.index, autopct='%1.1f%%', startangle=90)
plt.title('Top Three Countries with the Highest Number of Companies')
plt.axis('equal')

plt.show()


# ### Observation
# -The top countries with the highest number of unicorn companies in the dataset are the United States, China, and India.

# In[234]:


# Top five companies by valuation

top_valuations = unicorn_data[['Company', 'Valuation']].sort_values('Valuation', ascending=False).head(5)
print(top_valuations)


# In[232]:


# Visualize the top five companies by valuation

# Define the colors for the bars
colors = ['blue', 'orange', 'green', 'red', 'purple']

# Sort the data by valuation in descending order and select the top five companies
top_companies = unicorn_data[['Company', 'Valuation']].sort_values('Valuation', ascending=False).head(5)

# Create a bar chart
plt.figure(figsize=(10, 6))
plt.bar(top_companies['Company'], top_companies['Valuation'], color=colors)
plt.xlabel('Company')
plt.ylabel('Valuation')
plt.title('Top 5 Companies by Valuation')

# Add data labels to the bars
for i, val in enumerate(top_companies['Valuation']):
    plt.text(i, val, f"${val}B", ha='center', va='bottom')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Display the chart
plt.show()


# ### Observation
# - The bar chart showcases the top five companies with the highest valuations, with Bytedance leading the pack, followed by SpaceX, SHEIN, Stripe, and Klarna.

# In[ ]:





# In[236]:


# Top five industries by valuation

top_industries = unicorn_data[['Industry', 'Valuation']].sort_values('Valuation', ascending=False).head(5)
print(top_industries)


# In[147]:


# Visualize top five industries by valuation


# Get the top industries
top_industries = unicorn_data['Industry'].value_counts().head(5)

# Create the donut chart
plt.figure(figsize=(8, 8))
plt.pie(top_industries, labels=top_industries.index, autopct='%1.1f%%', startangle=90, wedgeprops=dict(width=0.3))
plt.title('Distribution of Valuations Among Top Industries')
plt.axis('equal')

# Add labels
centre_circle = plt.Circle((0, 0), 0.5, color='white', linewidth=0.5)
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.show()


# ### Observation
# - The top valuation in the dataset belongs to Bytedance at $180 billion.

# In[ ]:





# In[237]:


# Relationship between funding and valuation for unicorn companies.

sns.scatterplot(data=unicorn_data, x='Funding', y='Valuation')
plt.xlabel('Funding')
plt.ylabel('Valuation')
plt.title('Valuation vs Funding')
plt.show()


# ### Observation 
# - There is a positive relationship between funding and valuation for unicorn companies.

# 

# In[219]:


# Valuation Distribution by Industry

top_industries = unicorn_data['Industry'].value_counts().nlargest(10).index

plt.figure(figsize=(10, 6))
sns.boxplot(data=unicorn_data[unicorn_data['Industry'].isin(top_industries)], x='Industry', y='Valuation')
plt.xlabel('Industry')
plt.ylabel('Valuation')
plt.title('Valuation Distribution by Top 10 Industries')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()


# ### Observation
# - The boxplot visualization indicates that the "Artificial intelligence" and "Fintech" industries have a wider range of valuations compared to other industries in the dataset.

# In[ ]:





# In[222]:


# Valuation by Country

# Top 10 Valuation by Country in Descending Order
top_10_countries = unicorn_data.groupby('Country')['Valuation'].sum().nlargest(10).index

plt.figure(figsize=(10, 6))
sns.barplot(data=unicorn_data[unicorn_data['Country'].isin(top_10_countries)], x='Country', y='Valuation', order=top_10_countries)
plt.xlabel('Country')
plt.ylabel('Valuation (in billions)')
plt.title('Top 10 Valuation by Country')
plt.xticks(rotation=45)
plt.tight_layout()


# ### Observation
# - The bar chart displays the top 10 countries with the highest valuations, with the United States having the highest total valuation followed by China and the United Kingdom.

# In[225]:


# Funding by Industry

top_10_industries = unicorn_data['Industry'].value_counts().nlargest(10).index

plt.figure(figsize=(10, 6))
sns.violinplot(data=unicorn_data[unicorn_data['Industry'].isin(top_10_industries)], x='Industry', y='Funding')
plt.xlabel('Industry')
plt.ylabel('Funding')
plt.title('Funding Distribution by Top 10 Industries')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()


# ### Observation
# - The violin plot shows the distribution of funding amounts across different industries, indicating the range and density of funding values for each industry category.

# In[ ]:





# In[226]:


# Valuation by Continent

plt.figure(figsize=(10, 6))
Which unicorn companies have had the biggest return on investment?sns.boxplot(data=unicorn_data, x='Continent', y='Valuation')
plt.xlabel('Continent')
plt.ylabel('Valuation')
plt.title('Valuation by Continent')
plt.show()


# ### Observation
# - The boxplot reveals that North America has the highest overall valuation range among unicorn companies, followed by Asia and Europe, while Oceania and South America have relatively lower valuations.

# In[ ]:





# In[181]:


# Unicorn companies that have had the biggest return on investment

# Convert 'Valuation' and 'Funding' columns to numeric data type
unicorn_data['Valuation'] = unicorn_data['Valuation'].replace('[\$,]', '', regex=True).astype(float)
unicorn_data['Funding'] = unicorn_data['Funding'].replace('[\$,]', '', regex=True).astype(float)

# Calculate ROI
unicorn_data['ROI'] = unicorn_data['Valuation'] / unicorn_data['Funding']

# Sort by ROI in descending order
top_roi_companies = unicorn_data.sort_values('ROI', ascending=False)

# Display top 10 companies with highest ROI
print(top_roi_companies[['Company', 'ROI']].head(10))


# In[ ]:





# In[185]:


# Visualize unicorn companies that have had the biggest return on investment
import matplotlib.pyplot as plt

# Data
companies = ['SHEIN', 'Stripe', 'Bytedance', 'Checkout.com', 'Revolut', 'FTX', 'SpaceX', 'Instacart', 'Databricks', 'Chime']
roi = [50.0, 47.5, 22.5, 20.0, 16.5, 16.0, 14.285714, 13.0, 12.666667, 12.5]

# Create a bar graph
plt.figure(figsize=(10, 6))
plt.bar(companies, roi)
plt.xlabel('Company')
plt.ylabel('ROI')
plt.title('Top 10 Companies with Highest ROI')
plt.xticks(rotation=45)
plt.tight_layout()

# Add labels to the bars
for i in range(len(companies)):
    plt.text(i, roi[i], str(roi[i]), ha='center', va='bottom')

plt.show()


# ### Observation
# - The top 10 unicorn companies with the highest return on investment (ROI) are SHEIN, Stripe, Bytedance, Checkout.com, Revolut, FTX, SpaceX, Instacart, Databricks, and Chime.

# In[ ]:





# In[227]:


# Convert 'Year Founded' column to datetime data type with the specified format
unicorn_data['Year Founded'] = pd.to_datetime(unicorn_data['Year Founded'], format='%d-%m-%Y')

# Convert 'Date Joined' column to datetime data type with the specified format
unicorn_data['Date Joined'] = pd.to_datetime(unicorn_data['Date Joined'], format='%d-%m-%Y')

# Calculate the duration between 'Year Founded' and 'Date Joined' in years
unicorn_data['Duration'] = (unicorn_data['Date Joined'] - unicorn_data['Year Founded']).dt.days / 365

# Calculate the average duration
average_duration = unicorn_data['Duration'].mean()

# Display the average duration
print("Average Duration (in years):", average_duration)


# In[192]:


# Visualize the distribution of duration to become a Unicorn Company

plt.figure(figsize=(10, 6))
plt.hist(unicorn_data['Duration'], bins=10, edgecolor='k')
plt.xlabel('Duration (years)')
plt.ylabel('Frequency')
plt.title('Distribution of Duration to Become a Unicorn')
plt.show()


# ### Observation
# - On average, it takes approximately 50 years for a company to become a unicorn.
# - The histogram reveals that the majority of companies take around 5-10 years to become unicorn companies.

# In[ ]:





# In[ ]:





# In[209]:


# Visualize investors that have funded the most unicorns.

# Count the occurrences of each investor
investor_counts = unicorn_data['Select Investors'].str.split(', ').explode().value_counts()

# Filter out empty values
investor_counts = investor_counts[investor_counts.index != '']

# Sort the investors in ascending order
investor_counts = investor_counts.sort_values(ascending=True)

# Top 10 investors with the most funding
top_investors = investor_counts.tail(10)

# Create bar chart
plt.figure(figsize=(10, 6))
ax = top_investors.plot(kind='barh')
ax.set_xlabel('Number of Unicorns')
ax.set_ylabel('Investor')
ax.set_title('Top 10 Investors Funding the Most Unicorns')

# Add data labels
for p in ax.patches:
    ax.annotate(str(p.get_width()), (p.get_width(), p.get_y() + p.get_height() / 2), ha='left', va='center')

# Show the plot
plt.tight_layout()
plt.show()


# ### Observation
# - The top 10 investors that have funded the most unicorns include Accel, Tiger Global Management, Andreessen Horowitz and so on indicating their significant involvement in funding successful unicorn companies.

# In[ ]:




