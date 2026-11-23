import csv

#store the sale data in a list
report = []
with open ("sales_data.csv.txt", "r") as file:
    sales = csv.DictReader(file)
    for row in sales:#to conver them into their respective categorie
        row["quantity"] = int(row["quantity"])
        row["price"] = float(row["price"])
        report.append(row)


#calculate total revenue
total_revenue = 0
for row in report:
    single_revenue = row["quantity"] * row["price"]
    total_revenue += single_revenue
print(f"Total revenue: {total_revenue:.2f}")

print("-" * 10 + "Revenue Per Product" + "-" * 10)

#calculate revenue for each widget
for product in report:
    product_revenue = product["quantity"] * product["price"]
    product["revenue"] = product_revenue

    print(f"{product["revenue"]:.2f}")


#calculate the quantity and revenue
quantity_sold = {} 
revenue_by_product = {}

for product in report:
    product_name = product["product"]
    
    if product_name in quantity_sold:
        quantity_sold[product_name] += product["quantity"]
        revenue_by_product[product_name] += product["revenue"]

    else:
        quantity_sold[product_name] = product["quantity"]
        revenue_by_product[product_name] = product["revenue"]

print("\nTotal Quantity Sold")

for product_name, total_quantity in quantity_sold.items():
    print(f"{product_name}: {total_quantity}")


daily_revenue = {}

for product in report:
    date = product["date"]
    if date in daily_revenue:
        daily_revenue[date] += product["revenue"]
    else:
        daily_revenue[date] = product["revenue"]

best_day = max(daily_revenue, key=daily_revenue.get)

print(f"\nHighest Revenue Day: {best_day}")
print(f"Revenue: ${daily_revenue[best_day]:.2f}")

total_quantity = sum(quantity_sold.values())

#create a formatted sales report text file
with open ("sales_report.txt", "w") as file:
    file.write("=" * 10 + "SALES REPORT" + "=" * 10 + "\n\n")
    file.write(f"Total Revenue: ${total_revenue:.2f}\n")
    file.write(f"Total Quantity Sold: {total_quantity}\n\n")

    file.write("Revenue by product:\n")

    for product, revenue in revenue_by_product.items():
        file.write(f"{product}: ${revenue:.2f}\n")

        file.write("\n" + "=" * 25 + "\n")
#create csv file containing total quantity and revenue by widget
with open ("product_summary.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["product", "total_quantity", "total_revenue"])

    for product in revenue_by_product:
        writer.writerow([
            product,
            quantity_sold[product],
            round(revenue_by_product[product],2)
        ])