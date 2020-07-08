from rewardapp.model import Configuration, Employee, Customer, Rewards

def  rewardCalculation(r_fuelamount):
     return lambda rewardRate: float(r_fuelamount)*(float(rewardRate)/100.0)  

def isAdmin(employee):
     employee = Employee.query.filter(Employee.e_username == employee).first()
     if employee.e_admin == True:
          return True
     return False

