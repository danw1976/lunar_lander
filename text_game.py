speed = 30
gravity = 1.622
fuel = 1500
altitude = 1000
burn = 0

while altitude > 0:
    if speed <= 0:
        impact = 1000
    else:
        impact = altitude / speed
    print("altitude = {:8.3f}\n Speed={:6.3f}\n Fuel={:8.3f}\n Impact={:6.3f}\n Previous burn={:6.3f}".format(altitude,speed,fuel, impact,burn))
    burn = float(input("Enter an amount of fuel to burn between 0 and 50: "))
    if burn < 0:
        burn = 0
    if burn > 50:
        burn = 50
    if burn > fuel:
        burn = fuel
    altitude -= speed
    speed += gravity - burn/10
    fuel -= burn

print("Altitude={:8.3f} Speed={:6.3f} Fuel={:8.3f} Last burn={:6.3f}".format(altitude,speed,fuel,burn))
if altitude < -5 or speed > 5:
    print("You have crashed.")
else:
    print("You have successfully landed.")
