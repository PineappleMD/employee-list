class Employee:

  def __init__(self, name, number):
    self.__name = name
    self.number = number

  def set_emp_name(self, name):
    self.__name = name

  def set_emp_number(self, number):
    self.__number = number

  def get_emp_name(self):
    return self.__name

  def get_emp_number(self):
    return self.number


class ProductionWorker(Employee):

  def __init__(self, name, number, shift_num, pay_rate):
    Employee.__init__(self, name, number)
    self.__shift_num = shift_num
    self.__pay_rate = pay_rate

  def set_shift_num(self, shift_num):
    self.__shift_num = shift_num

  def set_pay_rate(self, pay_rate):
    self.__pay_rate = pay_rate

  def get_shift_num(self):
    return self.__shift_num

  def get_pay_rates(self):
    return self.__pay_rate
