def parallel(resistors):
   sum = 0
   for resistance in resistors:
    effective_resistance = 1/ resistance
    sum += effective_resistance
   print(f"{round(1/sum,2)} ohm")
   
parallel([330, 1000, 2200])

def potential_divider(supply_voltage, resistors_value):
    pass
    
