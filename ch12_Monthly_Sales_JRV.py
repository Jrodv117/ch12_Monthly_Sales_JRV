
monthly_sales_dictionary = {}

with open('monthly_sales.txt') as sales:
    for line in sales:
        (key,val) = line.split()
        monthly_sales_dictionary[(key)] = int(val)
        
        
print(monthly_sales_dictionary)