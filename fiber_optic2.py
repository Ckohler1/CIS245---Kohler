def main():
  
  print("Welcome to Fiber Optic For You")
  
  company_name = input("Please enter the name of your company-")
  
  feet_of_cable = input("Please enter your desired amount of fiber optic cable in feet-")
  
  feet_of_cable = float(feet_of_cable)
  
  if feet_of_cable > 100
    cable_cost = feet_of_cable*.80

  elif feet_of_cable > 250
    cable_cost = feet_of_cable*.70

  elif feet_of_cable > 500
    cable_cost = feet_of_cable*.50

  else cable_cost = feet_of_cable*.87

  message = "Thank you for your business "
  message += company_name
  message += ". Your total cost is $"+str(cable_cost)
  message += "."

  print(message)

main()