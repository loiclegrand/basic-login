######### GLOBAL VARIABLES ###############

username = ""
password = ""

new_username = ""
new_password = ""

has_account = None
answer = ""

valid_answer = False
login_succesfull = False


# the main function that does it all
def full_login():


    ask_if_account()

    if has_account == True:
       while login_succesfull == False:
            ask_for_login()
            find_login()
        

    elif has_account == False:
        
        create_account()
        write_credentials()
        
        while login_succesfull == False:
            ask_for_login()
            find_login()
        




# ask if the user has an account
def ask_if_account():

    global answer
    global has_account
    global valid_answer

    answer = input("Do you already have an account? y/n:  ")

    # while there is no valid answer it will re ask the question above
    while valid_answer == False:

        if answer == "y" or answer == "Y":
            has_account = True
            valid_answer = True
        elif answer == "n" or answer == "N":
            has_account = False
            valid_answer = True
        elif answer != "y" or answer != "Y" or answer != "n" or answer != "N":
            answer = input("That's not a valid input, Do you already have an account? y/n:  ")
            
        
# asks the user to input his credentials
def ask_for_login():

    global username
    global password

    username = input("enter your username: ")
    password = input("enter your password: ")
    return

# asks the user to create an account
def create_account():

    global new_username
    global new_password
    valid_password = False
    valid_lenght = False
    # user inputs the username that he wants
    new_username = input("Enter your wanted username: ")
    
    # you must repeat the password and have at least 8 characters to continue
    while valid_password == False:
        while valid_lenght == False:
                if len(new_password) < 8:
                    print("Your password must be at least 8 characters long. Try again")
                    new_password = input("Enter your wanted password: ")
                    repeat_new_password = input("Repeat your wanted password: ")
                else:
                    valid_lenght = True
        
        
        # if your password match it becomes a valid password
        if new_password == repeat_new_password:
                        
            print("You account have been created, please log in.")
            valid_password = True
        # if it doens't match you can try again
        elif new_password != repeat_new_password:
            print("your password does not match, try again. ")
    return


# write the given credentials to a text file
def write_credentials():

    creds = open("credentials.txt", "a")
    creds.write(new_username)
    creds.write(" " + new_password)
    creds.write("\n")
    creds.close()

# find the given credentials in the text file
def find_login():

    global login_succesfull
    
    # Merge credentials to find it in the text file
    merged_credentials = username + " " + password

    # search for credentials in the file
    with open("credentials.txt") as file:
        if merged_credentials in file.read():
            print("You are logged in!")
            login_succesfull = True
        else:
            print("Wrong user name or password, Try again.")
    
            
    return


full_login()
## ask if the user has an account
## if yes:
    ## ask for a user name and a password
## if no:
    ##ask them to make a new account
     
## check in the txt file if username exist
## check if the password matches with the username
