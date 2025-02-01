when the parallel() is called this allow for users to calculate the effective resistance of a network of resistor in a parallel circuit, by just entering the number of resistor values within the parallel circuit. 

def parallel(resistors):
   sum = 0
   for resistance in resistors:
    effective_resistance = 1/ resistance
    sum += effective_resistance
   print(f"{round(1/sum,2)} ohm")
   
parallel([330, 1000, 2200]) """test trial"""

Additionally, the implementation of the voltage_divider() function was created with the functionality to obtain the respective voltage drop across various component throughout an electrical circuit. When the voltage_divider() function is called, the user would only need to enter first the supply voltage and the number of load resistive component throughout the curcuit and the function do the rest. 

def potential_divider(supply_voltage, resistors_value):
    total_resistance = 0
    for resistance in resistors_value:
        total_resistance += resistance
    current = supply_voltage/ total_resistance
    
    for resistor in resistors_value: 
        print(f"{round(resistor*current, 2)} V")

potential_divider(5, [4, 5]) """test trial"""

Moveover, the implementation of the temperature_check() function, this function aid in determining if a patient is either hypothermic or Hyperthermic and convert between the temperature scale degree fahrenheit and degree celcius base on the user desire. When this function is implemented in your code this allow for the convertion between the desire temperature either fahrenheit or celcius and determine wheather a patient is either Hypothermic or Hyperthermic base on the input temperature value in the function. 
def Temperature_check(temp_val, unit_sign):
    if unit_sign == "C":
        degree = (temp_val -32)* (5/9)
    elif unit_sign == "F":
        degree = temp_val*(5/9)+ 32
    if temp_val < 29:
         print("The Patient is Hypothermic")
    else: 
        print("The Patient is Hyperthermic")
     
Temperature_check(35, "C") """test trial"""

To concluded, the reason for the creation of these functions was to complete the objective and task of this assignment.

I used to steal soap, but I'm clean now. #"mi nahhh look"(if you don't get it tiktok the expression and try again)