# -----------------------------------------------+
# Bradley White                                  | 
# CSCI 107, Assignment 8                         |
# Last Updated: October 31, 2013                 |  
# -----------------------------------------------|
# This is a program to diagnose patients based   |
# on symptoms they input and if they enter a     |
# fever a more specific diagnose can be given    |
# -----------------------------------------------+

def diagnose():
    """lol, we have a nice diagnosis tool!"""
    print("Hello! Welcome to MyDiagnose!")

    # Asks the user to input if they're sick.    
    while True:

        illQuestion = input("Are you ill (yes or no)?:")

        if illQuestion.lower() == "yes":
            imSick()
            break

        elif illQuestion.lower() == "no":
            imNotSick()
            break

        # If something other than yes or no is entered the question is reasked.
        else:
            print("Can you please just answer yes or no?")



    print("All done!")


def imSick():
    print("Lets try ti fix you up.")
    print("Have you been experiencing...")
    print("1. Runny nose?")
    print("2. Fever?")
    print("3. Yellowing of the skin or eyes?")
    print("4. Nausea or vomiting?")
    print("5. Something else we can treat for?")

    while True:

        # Asks the user to enter their symptoms and a specific function for each is called for the diagnose.
        myDiagnose = input("Please enter 1-5 corresponding to your symptoms:")
        
        if (myDiagnose == "1"):
            cold()
            break
        
        elif (myDiagnose == "2"):
            patientTemperature()
            break
        
        elif (myDiagnose == "3"):
            jaundice()
            break
        
        elif (myDiagnose == "4"):
            stomach_virus()
            break
        
        elif (myDiagnose == "5"):
            unknown()
            break
        
        else:
            print("Please enter a number 1-5!")
            
def cold():
    print("You have a cold.")

# If fever is entered they're asked their temperature and a more specific diagnose is given.
def patientTemperature():
    while True:

        try:
        
            myTemp = float(input("Please enter your temperature:"))
        
            if (myTemp >= 102.2):
                print("You have pyrexia.")
                break

            elif (myTemp < 102.2) and (myTemp >= 99.5):
                print("You have the flu.")
                break

            elif (myTemp < 99.5) and (myTemp >= 96.8):
                print("You have an unknown diease.")
                break

            elif (myTemp < 96.8) and (myTemp >= 95.0):
                print("You have the flu.")
                break

            else:
                (myTemp < 95.0)
                print("You have hypothermia.")
                break
            
        # If the user does not enter a number the question is reasked.
        except ValueError:
            print("Please enter your temperature!")


def jaundice():
    print("You have jaundice.")

def stomach_virus():
    print("You have a stomach virus.")

def unknown():
    print("You have a unknown diease.")

def imNotSick():
    """The person is not sick."""
    print("You look just fine. Go do some homework or something!!")   


diagnose()
