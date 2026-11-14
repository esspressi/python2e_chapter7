def main(): 
  num1 = int(input('Enter a number: '))
  num2 = int(input('Enter another number: '))
  
  if num2 != 0:
    result = num1 / num2
    print(num1, 'divided by', num2, 'is', result)
  else:
    print('Cannot divide by zero.')
    
main()  
