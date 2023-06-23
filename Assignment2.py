import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("supermarket_sales.csv")

#chart to illustrate if gross income is increasing or decreasing over time
gross_income= df.groupby('Date')['gross income'].sum()
fig,ax=plt.subplots(figsize=(10,5))
plt.plot(gross_income.index,gross_income.values)
tick_dates=gross_income.index[::30]
plt.xticks(tick_dates,rotation=90)
plt.title('Gross Income over time')
plt.xlabel('Date')
plt.ylabel('Gross Income')
plt.show()

#chart to show if sales are increasing or decreasing over time
sales=df.groupby('Date')['Total'].sum()
fig,ax=plt.subplots(figsize=(10,5))
plt.plot(sales.index,sales.values)  
tick_dates=sales.index[::30]
plt.xticks(tick_dates,rotation=90)
plt.title('Sales over time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.show()

#chart to show how much each branch sells
branch_sales=df.groupby('Branch')['Total'].sum()
plt.bar(branch_sales.index,branch_sales.values)
plt.title('Sales by Branch')
plt.xlabel('Branch')
plt.ylabel('Sales')
plt.show()

#chart to demonstrate how much each branch and type of customer sells (To show how the type of customer affects their amount of sale)
branch_customer_sales=df.groupby(['Branch','Customer type'])['Total'].sum()
branch_customer_sales.unstack().plot(kind='bar')
plt.title('Sales by Branch and Customer Type')
plt.xlabel('Branch')
plt.ylabel('Sales')
plt.show()

#Make a chart to show the relationship between Gross income and city
sns.barplot(x='City',y='gross income',data=df)
plt.title('Gross Income and City')
plt.xlabel('City')
plt.ylabel('Gross Income')
plt.show()

#Create a graph that displays the average rate for each branch.
branch_rating=df.groupby('Branch')['Rating'].mean()
plt.bar(branch_rating.index,branch_rating.values)
plt.title('Average Rating by Branch')
plt.xlabel('Branch')
plt.ylabel('Rating')
plt.show()

#Make a chart to show the relationship between customer gender and customer rate.
sns.barplot(x='Gender',y='Rating',data=df)
plt.title('Relationship between Gender and Rating')
plt.show()

# Make a pie chart to display the gender distribution of the customers.
gender_counts = df['Gender'].value_counts()
plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%')
plt.title('Gender Distribution of Customers')
plt.axis('equal')
plt.show()

''' 
A pie chart to show your supermarket payment preferences (percentage of
each payment type). Which method of payment is the most popular?
'''
payment_counts = df['Payment'].value_counts()
plt.pie(payment_counts, labels=payment_counts.index, autopct='%1.1f%%')
plt.title('Payment Preferences')
plt.axis('equal')
plt.show()

# Make a chart to compare the payment type usage across the genders.
payment_gender=df.groupby(['Gender','Payment']).size()
payment_gender.unstack().plot(kind='bar')
plt.title('Payment Type Usage Across Genders')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.show()

# Make a chart to show sales per product.
product_sales=df.groupby('Product line')['Total'].sum()
fig,ax=plt.subplots(figsize=(10,5))
plt.bar(product_sales.index,product_sales.values)
tick_dates=product_sales.index[::1]
plt.xticks(tick_dates,rotation=90)
plt.title('Sales per Product')
plt.xlabel('Product')
plt.ylabel('Sales')
plt.show()






















