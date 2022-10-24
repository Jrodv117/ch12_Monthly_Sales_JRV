monthly_sales_dictionary = {}

FILE_NAME = 'monthly_sales.txt'
with open(FILE_NAME) as f:
    for line in f:
        (key,val) = line.split()
        monthly_sales_dictionary[(key)] = int(val)
        
def write_to_txt(dictionary):        
    with open(FILE_NAME,'w', encoding='utf-8') as f:
        for key in dictionary.keys():
            f.write(key.capitalize() + "\t" + str(dictionary[key])+ "\n") 
        f.close() 


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
        write_to_txt(dictionary)

def totals(dictionary):
    sum_of_values = sum(dictionary.values())
    print(f'Yearly total: {sum_of_values}')
    print(f'Monthly average: {sum_of_values/len(dictionary)}')
        
def main():
    print('Montly Sales Program\n')
    menu()
    while True:
        command = input('\nCommand: ').lower
        if command == 'view':
            view(monthly_sales_dictionary)
        elif command == 'edit':
            edit(monthly_sales_dictionary)
        elif command == 'totals':
            totals(monthly_sales_dictionary)
        elif command == "exit":
            print("Bye!")
            exit()

if __name__ == "__main__":
    main()