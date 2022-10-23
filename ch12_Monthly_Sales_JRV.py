
monthly_sales_dictionary = {}
FILE_NAME = 'monthly_sales.txt'
with open(FILE_NAME) as f:
    for line in f:
        (key,val) = line.split()
        monthly_sales_dictionary[(key)] = int(val)

def menu():
    print('Command Menu')
    print('view - View sales for specified month')
    print('edit - Edit sales for specified month')
    print('totals - View sales summary for year')
    print('exit - Exit program')
        
def view(dictionary):
    month = input('Three letter month: ')
    print(f'Sales for month: {dictionary.get(month)}')
    
def main():
    print('Montly Sales Program\n')
    menu()
    command = input('\nCommand: ').lower()
    while command != 'exit':
        if command == 'view':
            view(monthly_sales_dictionary)
    
main()