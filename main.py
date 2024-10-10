import emp


def main():

  print('Enter the following details of the employee')
  emp_name = input('Enter Employee Name: ')
  number = input('Enter Employee Number: ')
  sh = input('Enter Shift Number: ')
  pay = input('Enter Pay Rate: ')

  emp = ProductionWorker(emp_name, number, sh, pay)

  print('Details of Employee:')
  print('Name', emp.get_emp_name())
  print('Employee Number', emp.get_emp_number())
  print('Shift Number', emp.get_shift_num())
  print('Pay Rate', emp.get_pay_rates())


if __name__ == '__main__':
  main()
