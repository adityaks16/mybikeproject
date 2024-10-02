# Aditya Kunapareddy
# Purpose: Bike class for Object Oriented Programming assignment
#
# Properties
#  Number of Gears: get_num_gears(), set_num_gears()
#  Current Gear: get_current_gear(), set_current_gear()
#  Number of Wheels: get_num_wheels(), set_num_wheels()
#  Brake Type: get_brake_type(), set_brake_type()
#
# Methods
#  reset_gears()
#  increase_gear()
#  decrease_gear()

class Bike:
    # Private properties
    __num_gears: int = 15
    __current_gear: int = 1
    __num_wheels: int = 2
    __brake_type: str = "hand brakes"

    ##################################
    # Instantiate a copy of this class
    def __init__(self,
                 num_gears=15,
                 current_gear=1,
                 num_wheels=2,
                 brake_type="hand brakes"):
        # Set all our properties
        self.set_num_gears(num_gears)
        self.set_current_gear(current_gear)
        self.set_num_wheels(num_wheels)
        self.set_brake_type(brake_type)

    #################################################
    # Getter and setter for the number of gears property
    def get_num_gears(self) -> int:
        return self.__num_gears

    def set_num_gears(self, num_gears: int) -> None:
        try:
            num_gears = int(num_gears)
            if 1 <= num_gears <= 15:
                self.__num_gears = num_gears
            else:
                raise ValueError("Number of gears must be between 1 and 15")
        except ValueError as e:
            raise e

    ###############################################
    # Getter and setter for the current gear property
    def get_current_gear(self) -> int:
        return self.__current_gear

    def set_current_gear(self, gear: int) -> None:
        try:
            gear = int(gear)
            if 1 <= gear <= self.__num_gears:
                self.__current_gear = gear
            else:
                raise ValueError(f"Current gear must be between 1 and {self.__num_gears}")
        except ValueError as e:
            raise e

    ##################################################
    # Getter and setter for the number of wheels property
    def get_num_wheels(self) -> int:
        return self.__num_wheels

    def set_num_wheels(self, num_wheels: int) -> None:
        try:
            num_wheels = int(num_wheels)
            if num_wheels in [1, 2, 3, 4]:
                self.__num_wheels = num_wheels
            else:
                raise ValueError("Number of wheels must be 1, 2, 3, or 4")
        except ValueError as e:
            raise e

    #############################################
    # Getter and setter for the brake type property
    def get_brake_type(self) -> str:
        return self.__brake_type

    def set_brake_type(self, brake_type: str) -> None:
        if brake_type in ["hand brakes", "foot brakes"]:
            self.__brake_type = brake_type
        else:
            raise ValueError("Brake type must be 'hand brakes' or 'foot brakes'")

    ##############
    # Reset Gears
    def reset_gears(self) -> None:
        self.__current_gear = 1

    ###############
    # Increase Gear
    def increase_gear(self) -> None:
        if self.__current_gear < self.__num_gears:
            self.__current_gear += 1
        else:
            print(f"Already at maximum gear ({self.__num_gears})")

    ###############
    # Decrease Gear
    def decrease_gear(self) -> None:
        if self.__current_gear > 1:
            self.__current_gear -= 1
        else:
            print("Already at minimum gear (1)")