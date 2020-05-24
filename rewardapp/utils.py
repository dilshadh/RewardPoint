from rewardapp.model import Employee
def fetchMobileNumber(phone_number):
    employee = Employee.query.filter_by(e_phone_number=phone_number).first()
    return employee