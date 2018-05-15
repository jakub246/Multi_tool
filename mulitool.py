# Import the necessary packages
from consolemenu import *
from consolemenu.items import *
from calc.calculator import calc_main
from weather import weather_main

# Create the menu
menu = ConsoleMenu("Multi tool by Jakub", "Select subprogram which you need")

# A FunctionItem runs a Python function when selected
calc_item = FunctionItem("Calculator", calc_main)
weather_item = FunctionItem("Weather", weather_main)

# Once we're done creating them, we just add the items to the menu
menu.append_item(calc_item)
menu.append_item(weather_item)

# Finally, we call show to show the menu and allow the user to interact
menu.show()
