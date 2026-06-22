import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns', None)

sales_df = pd.read_csv("Data/Sales_data.csv")
print(sales_df.head())
print()
sales_df.info()
print()
print(sales_df.isnull().sum())
print()
print(sales_df.describe())
print()

sales_df = sales_df.drop(columns=["Postal Code"])
sales_df["Order Date"] = pd.to_datetime(sales_df["Order Date"], format="%d/%m/%Y", errors="coerce")
sales_df["Ship Date"] = pd.to_datetime(sales_df["Ship Date"], format="%d/%m/%Y", errors="coerce")
sales_df["Shipping Duration"] = (sales_df["Ship Date"] - sales_df["Order Date"]).dt.days

total_sales = sales_df["Sales"].sum()
print(f"Total sales: {total_sales}")
average_sales = total_sales/sales_df["Sales"].count()
print(f"Average sales: {average_sales}\n")

sns.barplot(x="Category", y="Sales", data=sales_df)
plt.title("Sales by Category")
plt.show()
print("'Technology' category has the most sales, while 'Office Supplies' category has the least sales.\n")

sns.barplot(x="Sales", y="Sub-Category", data=sales_df.sort_values(by="Sales", ascending=False))
plt.title("Sales by Sub-Category")
plt.show()
print("'Copiers' is the top category by sales, and 'machine' is the second-most top category by sales.\n")

sns.barplot(x="Region", y="Sales", data=sales_df)
plt.title("Sales by Region")
plt.show()
print("While average sales are relatively uniform across East, Central, and West regions, the South region leads in sales volume but also carries a significantly higher standard deviation.\n")

sns.barplot(x="Sales", y="State", data=sales_df.sort_values(by="Sales", ascending=False).head(10))
plt.title("Sales by State")
plt.show()
print("The state with the highest sales is 'Florida', followed by 'Indiana'.\n")

sns.barplot(x="Sales", y="City", data=sales_df.sort_values(by="Sales", ascending=False).head(10))
plt.title("Sales by City")
plt.show()
print("The city with the highest sales is 'Jacksonville', followed by 'Lafayette'.\n")

segment_sales = sales_df.groupby('Segment')['Sales'].sum()
plt.pie(segment_sales, labels=segment_sales.index, startangle=140, autopct="%.2f %%", colors=["#509fff", "#ff605b", "#a2d43d"], pctdistance=0.7, explode=[0.01,0.01,0.01])
plt.title("Sales by  Segment")
plt.show()
print("The Consumer segment dominates with over half of all sales (50.8%), followed by Corporate (30.4%) and Home Office (18.8%).\n")

sns.countplot(x="Ship Mode", data=sales_df, hue="Ship Mode", palette="magma")
plt.title("Customer's Use of Ship Mode")
plt.show()
print("Most customers use the 'Standard Class' ship mode, while 'Same Day' ship mode is used the least by customers.\n")

sns.barplot(x="Ship Mode", y="Sales", hue="Ship Mode", data=sales_df, palette="Blues")
plt.title("Sales by Ship Mode")
plt.show()
print("Average sales are highly consistent across all ship modes, with 'Same Day' showing the highest average and variability, while 'Standard Class' is the lowest and most consistent.\n")

sns.barplot(x="Sales", y="Customer Name", data=sales_df.loc[sales_df["Customer Name"].duplicated()].sort_values(by="Sales", ascending=False).head(10))
plt.title("Top 10 Customers by Sales")
plt.show()
print("The top customer by sales is 'Sean Miller', followed by 'Tamara Chand'.\n")

monthly_sales = (sales_df.groupby([sales_df['Order Date'].dt.year.rename("Year"), sales_df['Order Date'].dt.month.rename("Month")])['Sales'].sum().reset_index())
plt.figure(figsize=(12, 6))
sns.lineplot(data=monthly_sales, x='Month', y='Sales', hue='Year', marker='o', palette='tab10', linewidth=3)
plt.xticks(ticks=range(1, 13), labels=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
plt.title("Sales Trend")
plt.show()
print("Sales exhibit clear seasonality with sharp peaks every September and November across all years, followed by consistent drops in February and October.\n")

sns.histplot(sales_df["Shipping Duration"], bins=8, kde=True)
plt.title("Shipping Duration Distribution")
plt.show()
print(f"Average shipping duration: {sales_df['Shipping Duration'].mean():.1f} days\n\n")

#Summary
print("Summary:\nThis analysis shows a business driven primarily by the Consumer segment (over half of revenue) and the Technology category, with Copiers and Machines as top sub-categories. Sales are concentrated in a few key markets — led by Florida and Jacksonville — with the South region showing the highest volume but also the most volatility. Customers favor Standard Class shipping despite Same Day delivery yielding higher average sales, pointing to a possible opportunity to promote faster options. Sales also peak consistently every September and November, useful for inventory and marketing planning.")

