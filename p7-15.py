def main(): 
  another = 'y' 
  coffee_file = open('coffee.txt', 'a')
  while another == 'y' or another == 'Y':
    print('enter the following coffee data:')
    descr = input('description: ')
    qty = int(input('quantity (in pounds): '))
    coffee_file.write(descr + '\n')
    coffee_file.write(str(qty) + '\n')
    print('do you want to add another record?')
    another = input('Y = yes, anything else = no: ')

  coffee_file.close()
  print('data appended to coffee.txt')

main()
