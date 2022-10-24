from operator import truediv


monthly_sales_dictionary = {}

FILE_NAME = 'monthly_sales.txt'
def read_text():
    with open(FILE_NAME) as f:
        for line in f:
            (key,val) = line.split()
            monthly_sales_dictionary[(key)] = int(val)
        
def write_to_txt(dictionary):        
    with open(FILE_NAME,'w', encoding='utf-8') as f:
        for key in dictionary.keys():
            f.write(key.capitalize() + "\t" + str(dictionary[key])+ "\n") 
        f.close() 


def menus():
    print('Command Menu')
    print('view - View sales for specified month')
    print('edit - Edit sales for specified month')
    print('totals - View sales summary for year')
    print('exit - Exit program')
        
def view(dictionary):
    month = input('Three letter month: ').capitalize()
    checked_input = check_entry(dictionary, month)
    if checked_input == True:
        print(f'Sales amount for {month} is {dictionary.get(month)}')
    else:
        pass
    
def edit(dictionary):
    month = input('\nThree letter month: ').capitalize()
    checked_input = check_entry(dictionary, month)
    if checked_input == True:
        amount = int(input('Sales amount: '))
        dictionary[month] = amount
        write_to_txt(dictionary)
    else: 
        pass

def totals(dictionary):
    sum_of_values = sum(dictionary.values())
    print(f'Yearly total: {sum_of_values}')
    print(f'Monthly average: {sum_of_values/len(dictionary)}') 
    
def check_entry(dictionary, month):
    check_input = True
    if month in dictionary:
        pass
    else:
        check_input = False
        print('Invalid three-letter month')
    return check_input
    


def main():
    print('Montly Sales Program\n')
    read_text()
    menus()
    while True:
        command = input('\nCommand: ').lower()
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