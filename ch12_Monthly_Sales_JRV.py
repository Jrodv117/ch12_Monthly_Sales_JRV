
monthly_sales_dictionary = {}
FILE_NAME = 'monthly_sales.txt'
with open(FILE_NAME) as f:
    for line in f:
        (key,val) = line.split()
        monthly_sales_dictionary[(key)] = int(val)
        
        
print(monthly_sales_dictionary)