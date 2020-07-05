from rewardapp.model import Configuration, Employee

def rewardCalculation(r_fuelamount):
     config = Configuration.query.get(1)
     rewardRate = config.cnfg_value
     reward_point= r_fuelamount*(rewardRate/100)
     return reward_point

def isAdmin(employee):
     employee = Employee.query.filter(Employee.e_username == employee).first()
     if employee.e_admin == True:
          return True
     return False