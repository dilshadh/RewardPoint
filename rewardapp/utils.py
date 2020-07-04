from rewardapp.model import Configuration

def rewardCalculation(r_fuelamount):
     config = Configuration.query.get(1)
     rewardRate = config.cnfg_value
     reward_point = float(r_fuelamount)*(float(rewardRate)/100.0)
     return reward_point