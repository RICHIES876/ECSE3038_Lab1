def parallel(resistors):
   sum = 0
   for resistance in resistors:
    effective_resistance = 1/ resistance
    sum += effective_resistance
   print(f"{round(1/sum,2)} ohm")
   
parallel([330, 1000, 2200])

def potential_divider(supply_voltage, resistors_value):

    total_resistance = 0
    for resistance in resistors_value:
        total_resistance += resistance
    current = supply_voltage/ total_resistance
    
    for resistor in resistors_value: 
        print(f"{round(resistor*current, 2)} V")


potential_divider(5, [4, 5])

def Temperature_check(temp_val, unit_sign):
    if unit_sign == "C":
        degree = (temp_val -32)* (5/9)
    elif unit_sign == "F":
        degree = temp_val*(5/9)+ 32
    if temp_val < 29:
         print("The Patient is Hypothermic")
    else: 
        print("The Patient is Hyperthermic")

        
Temperature_check(35, "C")


    
