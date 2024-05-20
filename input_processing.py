# input_processing.py
# Laurel Flanagan, ENSF 692 P24
# A terminal-based program for processing computer vision changes detected by a car.
# Detailed specifications are provided via the Assignment 2 README file.
# You must include the code provided below but you may delete the instructional comments.
# You may add your own additional classes, functions, variables, etc. as long as they do not contradict the requirements (i.e. no global variables, etc.). 
# You may import any modules from the standard Python library.
# Remember to include your name and comments.



# No global variables are permitted


# You do not need to provide additional commenting above this class, just the user-defined functions within the class
class Sensor:

    # Must include a constructor that uses default values
    # You do not need to provide commenting above the constructor
    def __init__(self):
        self.light = "green"
        self.pedestrian = "no"
        self.vehicle = "no"

    # The update_status method passes the user inputs from input1 and input2 (menu and status) and the self parameter
    # The values for light, pedestrian, and vehicle are updated based on the inputs specified by the user
    # Values are only updated if they are valid vision changes 
    def update_status(self, input1, input2): # You may decide how to implement the arguments for this function
        if (input1 == "1") and ((input2 == "green") or (input2 == "yellow") or (input2 == "red")):
            self.light = input2
        elif (input1 == "2") and ((input2 == "yes") or (input2 == "no")):
            self.pedestrian = input2
        elif (input1 == "3") and ((input2 == "yes") or (input2 == "no")):
            self.vehicle = input2
        


# The sensor object should be passed to this function to print the action message and current status
# The print_message function displays a course of action message based on the user inputs
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
  

# Complete the main function below
def main():
    print("\n***ENSF 692 Car Vision Detector Processing Program***\n") #display program title
    sensor = Sensor() #create new object of the Sensor class 
    x = True
    while x == True: #loop continuously unless 0 is entered to end the program
        print("Are changes detected in the vision input?") #display initial question
        input1 = input("Select 1 for light, 2 for pedestrian, 3 for vehicle, or 0 to end the program: ") #prompt for user input
   
        if input1 == "0": #end loop if user enters 0
            break
        elif (input1 == "1"): #user selected 1 to update light status
            input2 = input("What change has been identified?: ") #prompt for user input again
            if (input2 == "green") or (input2 =="yellow") or (input2 == "red"): #if valid vision change for light is provided
                sensor.update_status(input1, input2) #update status based on input 
                print_message(sensor) #display course of action message and current values for light, pedestrian and vehicle 
            else:
                print("Invalid vision change.") #display message to let user know input is invalid
                print_message(sensor) #display current values for light, pedestrian and vehicle of the sensor object

        elif (input1 == "2"): #user selected 2 to update pedestrian status
            input2 = input("What change has been identified?: ") #prompt for user input again 
            if (input2 == "yes") or (input2 =="no"): #if valid vision change for pedestrian is provided
                sensor.update_status(input1, input2) #update status based on input
                print_message(sensor) #display course of action message and current values for light, pedestrian and vehicle 
            else:
                print("Invalid vision change.") #display message to let user know input is invalid 
                print_message(sensor) #display current values for light, pedestrian and vehicle of the sensor object

        elif (input1 == "3"): #user selected 3 to update vehicle status 
            input2 = input("What change has been identified?: ") #prompt user for input again
            if(input2 == "yes") or (input2 == "no"): #if valid vision change for vehicle is provided
                sensor.update_status(input1, input2) #update status based on input
                print_message(sensor) #display course of action message and current values for light, pedestrian and vehicle
            else:
                print("Invalid vision change.") #display message to let user know input is invalid 
                print_message(sensor) #display current values for light, pedestrian and vehicle of the sensor object

        else: #if user enters something other than 0, 1, 2, or 3 provide message to let them know input is invalid and continue loop
            try:
                raise ValueError ("You must select either 1, 2, 3, or 0.") #ValueError if input is something other than 0, 1, 2, or 3
                
            except ValueError: #handle error such that program can continue
                print("You must select either 1, 2, 3, or 0.") #display message to let user know input is invalid
                print("\n")
                continue #continues loop to prompt for input1 again 
        
            

            

# Conventional Python code for running main within a larger program
# No additional code should be included below this
if __name__ == '__main__':
    main()

