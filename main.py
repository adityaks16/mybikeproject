# Aditya Kunapareddy
# Purpose: Demonstrate the use of the Bike class
# Import our Bike class
from bike import Bike

###############################################
# Instantiate Bike objects and demonstrate functionality
###############################################
try:
    # Create a default bike
    default_bike = Bike()
    print("Default Bike:")
    print(f"Number of gears: {default_bike.get_num_gears()}")
    print(f"Current gear: {default_bike.get_current_gear()}")
    print(f"Number of wheels: {default_bike.get_num_wheels()}")
    print(f"Brake type: {default_bike.get_brake_type()}")

    print("\nTesting gear changes:")
    default_bike.increase_gear()
    print(f"After increasing: Current gear is {default_bike.get_current_gear()}")
    default_bike.decrease_gear()
    print(f"After decreasing: Current gear is {default_bike.get_current_gear()}")
    default_bike.reset_gears()
    print(f"After resetting: Current gear is {default_bike.get_current_gear()}")


    # Create a custom bike
    custom_bike = Bike(num_gears=10, current_gear=5, num_wheels=3, brake_type="foot brakes")
    print("Custom Bike:")
    print(f"Number of gears: {custom_bike.get_num_gears()}")
    print(f"Current gear: {custom_bike.get_current_gear()}")
    print(f"Number of wheels: {custom_bike.get_num_wheels()}")
    print(f"Brake type: {custom_bike.get_brake_type()}")


    # Demonstrate error handling
    print("Demonstrating error handling:")
    try:
        custom_bike.set_num_gears(20)
    except ValueError as e:
        print(f"Error setting number of gears: {e}")

    try:
        custom_bike.set_current_gear(15)
    except ValueError as e:
        print(f"Error setting current gear: {e}")

    try:
        custom_bike.set_num_wheels(5)
    except ValueError as e:
        print(f"Error setting number of wheels: {e}")

    try:
        custom_bike.set_brake_type("electric brakes")
    except ValueError as e:
        print(f"Error setting brake type: {e}")

except Exception as e:
    print(f"An unexpected error occurred: {e}")