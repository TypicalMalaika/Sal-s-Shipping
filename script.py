cost = 0
premium_gs = 125
def ground_shipping(weight):
  if (weight <= 2):
    cost = 1.50 * weight + 20
  elif (weight > 2) and (weight <= 6):
    cost = 3 * weight + 20
  elif (weight > 6) and (weight <= 10):
    cost = 4 * weight +20
  elif (weight > 10):
    cost = 4.75 * weight + 20
  return cost

def drone_shipping(weight):
  if (weight <= 2):
    cost = 4.50 * weight
  elif (weight > 2) and (weight <= 6):
    cost = 9 * weight
  elif (weight > 6) and (weight <= 10):
    cost = 12 * weight
  elif (weight > 10):
    cost = 14.25 * weight
  return cost

def cheap_option_ans(weight):
  ground = ground_shipping(weight)
  drone = drone_shipping(weight)
  if ground < drone and ground < premium_gs:
    return "You should ship using ground shipping, it will cost £" + str(ground)
  elif drone < ground and drone < premium_gs:
    return "You should ship using drone shipping, it will cost £" + str(drone)
  else:
    return "You should ship using Premium Ground Shipping, it will cost £" +str(premium_gs)

print(cheap_option_ans(800))
