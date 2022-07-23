def __init__(User, username, password, ID): # Defining new object
        User.name = username                # 
        User.password = password            # Adding attributes
        User.ID = ID                        #



class User:                                 # Creating parent class
        username = 'JaneDoe'
        password = 'Pa$$word'
        ID = 67890

class Compensation(User):                   # Creating child class of User
        pay_rate = 30.00                    #
        pay_type = 'Hourly'                 # Adding attributes
        schedule = 'Standard'               #

class Job_Info(User):                       # Creating child class of User
        location = 'Newport Beach'          #
        division = 'Operations'             # Adding attributes
        department = 'Tracking'             #
