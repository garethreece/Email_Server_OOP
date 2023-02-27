# An Email Simulation

# Import libraries
# datetime used to get the date and time of a sent email and save it to the email_outbox.txt
from datetime import datetime

# Class Definitions
# Creat a class definition for Email
class Email():
    
    '''This is a docstring and I am going to test to see if I can print this out using help(Email) below'''

#  Constructor for Email class to initiate the variables:
# - from address
# - header
# - email contents
# - date / time
# - has been read
# - is spam 

    def __init__(self, from_address, header, email_contents, date_received, time_received):
        self.from_address = from_address
        self.header = header
        self.email_contents = email_contents
        self.date_received = date_received
        self.time_received = time_received
        # Email is spam has been set to False
        self.is_spam = False
        # Email has been read set to False
        self.has_been_read = False

# Mark as read function to turn emails that have been read to True.
######### Need to fix this #######
    def mark_as_read(self):
        self.has_been_read = True
        return self.has_been_read

# Mark as spam function to turn emails that are indicated by user as spam to True.
########## Need to fix this ###########
    def mark_as_spam(self):
        self.is_spam = True
        return self.is_spam

# help(Email)
# the help(Email) worked for the docstring so I have turned it into a comment so not to run it with the main program.

# Define Functions

# Add email function to get the emails from a simulated email API that has all the emails in that account
# The simulated email server is called email_API.txt and saved in the same directory.
# I arbitrarily made up some emails to populate this text file for the simulation
# This then turns the api_emails into Email objects and appends the objects to the 'inbox' list
def add_email(address, head, content, date, time):
    email = Email(address, head, content, date, time)
    inbox.append(email)

# A function to count the total number of emails, the number of unread emails, and the number of spam emails.
def get_count():
    email_count = len(inbox)
    unread_email_count = 0
    spam_count = 0
    for i in range (0, len(inbox)):
        if inbox[i].has_been_read == False:
            unread_email_count += 1
    for i in range (0, len(inbox)):
        if inbox[i].is_spam == True:
            spam_count += 1
    return email_count, unread_email_count, spam_count

# A get email function to get the full contents of a single email that the user has chosen and display it 
def get_email(email_index):
    if email_index in range (0, len(inbox)):
        # uses the mark as reead method in the class to turn read email to True
        inbox[email_index].mark_as_read()
        print(f"""From: {inbox[email_index].from_address}
Date: {inbox[email_index].date_received}  Time: {inbox[email_index].time_received}
Title: {inbox[email_index].header}
Contents: {inbox[email_index].email_contents}
Marked as spam: {inbox[email_index].is_spam}
""")
    # If the email choice does not match it returns an error and goes back to main menu
    else:
        print('Did not pick a number from selection, does not compute. Returning to main menu.')

# A function to display a list of all the current unread emails to the user
def get_unread_emails():
    # creates a new list for unread emails if has_been_read is false
    unread_email = []
    #creates a for loop to assign the not been read emails to the list
    for email in inbox:
        if email.has_been_read == False:
            unread_email.append(email)
    #prints out the unread emails from the list in a easy to read format
    print("\nUnread emails list:\n")
    for i in range (0, len(unread_email)):
        print(f"{i + 1} - From: {unread_email[i].from_address}   Title: {unread_email[i].header}   Date: {unread_email[i].date_received}   Read: {unread_email[i].has_been_read}")
    email_count, unread_email_count, spam_count = get_count()
    print(f"""Number of emails: {email_count}
Number of unread emails: {unread_email_count}
Number of spam emails: {spam_count}""")

# function to show spam emails list
def get_spam_emails():
    # creates a spam_email list
    spam_email = []
    # loop to assign emails where spam is True to the list
    for email in inbox:
        if email.is_spam == True:
            spam_email.append(email)
    # prints out the spam list in an easy to read format
    print("\nSpam emails list:\n")
    for i in range (0, len(spam_email)):
        print(f"{i + 1} - From: {spam_email[i].from_address}   Title: {spam_email[i].header}   Date: {spam_email[i].date_received}   Read: {spam_email[i].has_been_read}")
    email_count, unread_email_count, spam_count = get_count()
    print(f"""Number of emails: {email_count}
Number of unread emails: {unread_email_count}
Number of spam emails: {spam_count}""")

# delete function that takes the users choice of email, displays it, and asks if they are sure they wnat to delete
# if yes it will remove it from the inbox list
def delete(email_index):
    # if the user has selected a number in the range, it will display the selected email
    if email_index in range (0, len(inbox)):
        print(f"""From: {inbox[email_index].from_address}
Date: {inbox[email_index].date_received}  Time: {inbox[email_index].time_received}
Title: {inbox[email_index].header}
Contents: {inbox[email_index].email_contents}
Marked as spam: {inbox[email_index].is_spam}
""")
        # check to see if they are sure they want to delete
        check = input("Are you sure you want to delete this email Y/N: ").upper()
        if check == 'Y' or check == 'YES':
            # if yes, removes from inbox list
            inbox.pop(email_index)
            print("This email has been deleted!")
        else:
            # if no, states that it won't delete and goes back to main menu
            print("This email has not been deleted!")
    # if the user doesn't pick a valid number it will return an error and go back to main menu
    else:
        print('Did not pick a number from selection, does not compute. Returning to main menu.')

# function to make sure the selection for the user email to be marked as spam is valid
# if so, it will use the mark as spam method in the Email class  
def identify_spam(email_index):
    if email_index in range (0, len(inbox)):
        inbox[email_index].mark_as_spam()
        print("Email marked as spam!")
    else:
        print("Not a valid selection, returning to main menu!")

# A function to write and send an email to a siumlated outbox and saved in email_outbox.txt
def write_email():
    # creates a send email list to save the user information
    send_email = [0, 1, 2, 3, 4]
    send_email[0] = input("Please type the email address that you want to send: ")
    send_email[1] = input("Please input a title: ")
    send_email[2] = input("What is the content of the email you are sending: ")
    # uses the import date time to get the current date and time in the correct format and save it to the send email list
    now = datetime.now()
    now_date = now.strftime("%Y-%m-%d")
    send_email[3] = now_date
    now_time = now.strftime("%H:%M:%S")
    send_email[4] = now_time
    # join all the list info into a string seperated by " || "
    send_email = (" || ").join(send_email)
    # append the information to the end of the email_outbox.txt file
    # every time the program is run it will create a new file so the simulation can start fresh 
    file = open("email_outbox.txt", "a+", encoding = "utf-8-sig")
    file.write(f"{send_email}\n")
    file.close()
    print(f"""Email has been sent:
{send_email}
Check email_outbox.txt for sent emails""")

# Function to format how the main menu should be displayed
def main_email_menu():
    menu_choice = input("""
What would you like to do:
1 = read
2 = mark spam
3 = send
4 = show spam
5 = show unread
6 = delete
0 = quit
Please make a choice: """).lower()
    return menu_choice

# Global variables

# A list to store all the objects for emails
api_inbox = []
inbox = []
# A variable to record the menu item chosen by the user
user_choice = ""

# Main Program

# Clear the email_outbox.txt file to start fresh for the simulation
file = open ("email_outbox.txt", "w+", encoding = "utf-8-sig")
file.write("")
file.close()

# Get the info form the simulated email API and store in an api_inbox to be turned into objects
# This way every time the simulation is run it has emails to check
file = open("email_API.txt", "r", encoding = "utf-8-sig")
for email_list in file:
    email_list = email_list.replace("\n", "")
    email_list = email_list.split(" || ")
    api_inbox.append(email_list)

# get a position at a time in the api_inbox and send to the add email function
for i in api_inbox:
    address, header, content, date, time = i[0], i[1], i[2], i[3], i[4]
    add_email(address, header, content, date, time)

# This corresponds to the main menu selection
# It uses if / elif statements to run what happens when the user makes a selection off the main menu
while user_choice != "quit":
    user_choice = main_email_menu()
    # This choice will display all the emails and allow the user to read an email in more deatail
    if user_choice == "read" or user_choice == "1":
        print("\nEmail Inbox - Which do you want to read\n")
        for i in range (0, len(inbox)):
            print(f"{i + 1} - From: {inbox[i].from_address}   Title: {inbox[i].header}   Date: {inbox[i].date_received}   Read: {inbox[i].has_been_read}")
        email_count, unread_email_count, spam_count = get_count()
        print(f"Number of emails: {email_count}\nNumber of unread emails: {unread_email_count}\nNumber of spam emails: {spam_count}")
        while True:
            try:
                choice = int(input(f"\nChoose an email (1 - {i + 1} or \'0\' to exit): "))
                break
            except:
                print("Please put in a number!")
        choice -= 1
        get_email(choice)

    # This option will allow the user to choose and mark a specific email as spam
    elif user_choice == "mark spam" or user_choice == "2":
        print("\nEmail Inbox -  Which do you want to mark as spam\n")
        for i in range (0, len(inbox)):
            print(f"{i + 1} - From: {inbox[i].from_address}   Title: {inbox[i].header}   Date: {inbox[i].date_received}   Read: {inbox[i].has_been_read}")
        email_count, unread_email_count, spam_count = get_count()
        print(f"Number of emails: {email_count}\nNumber of unread emails: {unread_email_count}\nNumber of spam emails: {spam_count}")
        while True:
            try:
                choice = int(input(f"\nChoose an email to mark as spam (1 - {i + 1} or \'0\' to exit): "))
                break
            except:
                print("Please put in a number!")
        choice -= 1
        identify_spam(choice)

    # This choice will give the user information to write and send an email
    elif user_choice == "send" or user_choice == "3":
        write_email()

    # This choice ill show all unread emails
    elif user_choice == "show_unread" or user_choice == "4":
        get_spam_emails()

# This choice will show in a list all the unread emails
    elif user_choice == "show_unread" or user_choice == "5":
        get_unread_emails()
    # This choice will allow the user to choose and delete an email from the inbox
    elif user_choice == "delete email" or user_choice == "6":
        for i in range (0, len(inbox)):
            print(f"{i + 1} - From: {inbox[i].from_address}   Title: {inbox[i].header}   Date: {inbox[i].date_received}   Read: {inbox[i].has_been_read}")
        while True:
            try:
                choice = int(input(f"\nChoose an email (1 - {i + 1} or \'0\' to exit): "))
                break
            except:
                print("Please put in a number!")
        choice -= 1
        delete(choice)
    # This choice will quit the program
    elif user_choice == "quit" or user_choice == "0":
        if user_choice == '0':
            user_choice = "quit"
        print("Goodbye")
    # If the user chooses wrong in the menu it will display an error and allow them to try again
    else:
        print("Oops - incorrect input")
