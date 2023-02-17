print("Welcome to Fiber Optic For You")
company_name = input("Please enter the name of your company-")
feet_of_cable = input("Please enter your desired amount of fiber optic cable in feet-")
feet_of_cable = float(feet_of_cable)
cable_cost = feet_of_cable*.87
message = "Thank you for your business "
message += company_name
message += ". Your total cost is $"+str(cable_cost)
message += "."
print(message)