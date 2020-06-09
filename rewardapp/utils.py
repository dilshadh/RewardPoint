from rewardapp.model import Configuration

def rewardCalculation(r_fuelamount):
     config = Configuration.query.get(1)
     rewardRate = config.cnfg_value
     reward_point= r_fuelamount*(rewardRate/100)
     return reward_point