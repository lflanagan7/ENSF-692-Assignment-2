# input_processing.py
# Laurel Flanagan, ENSF 692 P24
# A terminal-based program for processing computer vision changes detected by a car.

class Sensor:

    def __init__(self):
        self.light = "green"
        self.pedestrian = "no"
        self.vehicle = "no"

    # The update_status method passes the user inputs from menu and status and the self attribute
    # The values for light, pedestrian, and vehicle are updated based on the inputs specified by the user
    # Values are only updated if they are valid vision changes 
    def update_status(self, input1, input2): 
        if (input1 == "1") and ((input2 == "green") or (input2 == "yellow") or (input2 == "red")):
            self.light = input2
        elif (input1 == "2") and ((input2 == "yes") or (input2 == "no")):
            self.pedestrian = input2
        elif (input1 == "3") and ((input2 == "yes") or (input2 == "no")):
            self.vehicle = input2
        


# The sensor object is passed to this function to print the action message and current status
# The print_message function displays a course of action message that is dependent on the user inputs
# The function also displays the current values for the light, pedestrian, and vehicle parameters of the sensor object
def print_message(sensor):
    if (sensor.light == "green") and (sensor.pedestrian == "no") and (sensor.vehicle == "no"):
        print("\n")
        print("Proceed")
    elif (sensor.light == "yellow") and (sensor.pedestrian == "no") and (sensor.vehicle == "no"):
        print("\n")
        print("Caution")
    elif (sensor.light == "red") or (sensor.pedestrian == "yes") or (sensor.vehicle == "yes"):
        print("\n")
        print("STOP")

    print("\n")
    print("Light = ", sensor.light, ",", "Pedestrian = ", sensor.pedestrian, ",", "Vehicle = ", sensor.vehicle, ".")
  

def main():
    print("\n***ENSF 692 Car Vision Detector Processing Program***\n")
    #Create new object of the Sensor class
    sensor = Sensor() 
    x = True
    while x == True: 
        try:
            #First prompt for user input to select menu option
            print("Are changes detected in the vision input?") 
            input1 = input("Select 1 for light, 2 for pedestrian, 3 for vehicle, or 0 to end the program: ")

            #End program if user enters 0 
            if input1 == "0":
                break
            
            #If user selected 1 to update light status, prompt for user input again.
            #If a valid vision change is provided, update status based on input, display message and current values.
            #If invalid vision change is provided, display message to inform user and display current values. 
            elif (input1 == "1"): 
                input2 = input("What change has been identified?: ") 
                if (input2 == "green") or (input2 =="yellow") or (input2 == "red"): 
                    sensor.update_status(input1, input2) 
                    print_message(sensor) 
                else:
                    print("Invalid vision change.") 
                    print_message(sensor) 
            
            #If user selected 2 to update pedestrian status, prompt for user input again.
            #If a valid vision change is provided, update status based on input, display message and current values.
            #If invalid vision change is provided, display message to inform user and display current values.
            elif (input1 == "2"): 
                input2 = input("What change has been identified?: ") 
                if (input2 == "yes") or (input2 =="no"): 
                    sensor.update_status(input1, input2) 
                    print_message(sensor) 
                else:
                    print("Invalid vision change.") 
                    print_message(sensor) 

            #If user selected 3 to update vehicle status, prompt for user input again.
            #If a valid vision change is provided, update status based on input, display message and current values.
            #If invalid vision change is provided, display message to inform user and display current values.
            elif (input1 == "3"): 
                input2 = input("What change has been identified?: ") 
                if(input2 == "yes") or (input2 == "no"): 
                    sensor.update_status(input1, input2) 
                    print_message(sensor) 
                else:
                    print("Invalid vision change.") 
                    print_message(sensor) 
            
            
            else: 
                raise ValueError ("You must select either 1, 2, 3, or 0.") 
        
        #If user enters something other than 0, 1, 2, or 3, display message to let them know input is invalid.
        #Error is handled so that program can continue to ask user for inputs         
        except ValueError: 
                print("You must select either 1, 2, 3, or 0.") 
                print("\n")
                 
    

# Conventional Python code for running main within a larger program
# No additional code should be included below this
if __name__ == '__main__':
    main()

