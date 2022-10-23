
monthly_sales_dictionary = {}
FILE_NAME = 'monthly_sales.txt'
with open(FILE_NAME) as f:
    for line in f:
        (key,val) = line.split()
        monthly_sales_dictionary[(key)] = int(val)
        
with open(FILE_NAME,'w', encoding='utf-8') as f:
    f.write(monthly_sales_dictionary)

def menu():
    print('Command Menu')
    print('view - View sales for specified month')
    print('edit - Edit sales for specified month')
    print('totals - View sales summary for year')
    print('exit - Exit program')
        
def view(dictionary):
    month = input('Three letter month: ')
    print(f'Sales amount for {month} is {dictionary.get(month)}')
    
def edit(dictionary):
        month = input('\nThree letter month: ')
        amount = int(input('Sales amount: '))
        dictionary[month] = amount
        
def main():
    print('Montly Sales Program\n')
    menu()
    command = input('\nCommand: ').lower()
    while command != 'exit':
        if command == 'view':
            view(monthly_sales_dictionary)
        elif command == edit:
            edit(monthly_sales_dictionary)
main()