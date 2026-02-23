# functions here go
def string_check(question, valid_answer=('yes', 'no'),
                 num_letters=1):
    """checks that users enter the full word
    or the first letter of a word from a list of valid responses"""

    while True:

        response = input(question).lower()

        for item in valid_answer:

            # checks if the response is the entire word
            if response == item:
                return item

            # check if it's the first letter
            elif response == item[:num_letters]:
                return item

        print(f"Please choose an option from {valid_answer}")

def make_statement(statement, decoration):
    """Emphasises heading by adding decoration
    at the start and end"""

    print (f"{decoration * 3} {statement} {decoration * 3}")

def instruction():
    make_statement( "instruction", "ℹ️")

    print( '''
    
For each ticket holder enter ...
- Their name 
- Their age
-Their payment method (cash / credit

The program will record the ticket sale and calculate the
ticket cost (and the profit).

Once you have either sold all of the tickets or enter the 
exit code ('xxx'), the program will display the ticket 
sales information and write the data to a text file.

It will also choose one lucky ticket holder who wins the 
draw (their ticket is free).
   
    ''')

def int_check(question):
    """Checks users enter an integer that is more than zero (or the 'xxx' exit code)"""

    error = "Oops - please enter an integer."

    while True:

        try:
            # Return the response if it's an integer
            response = int(input(question))

            return response

        except ValueError:
            print(error)

def not_blank(question):
    """makes sure user response isnt blank"""

    while True:
        response = input(question)

        if response != "":
            return response
        print("Sorry, this can't be blank. Please tey again.\n")

# Main routine goes here
# Initialise ticket number
MAX_TICKETS = 5
tickets_sold = 0

# initialise variable / non-default options for string checker
payment_ans = ('cash', 'credit')

make_statement( "Mini-Movie Fundraiser Program", "🍿")

want_instructions = string_check("Do you want to see the instructions? ")

if want_instructions == "yes":
    instruction()

# loop to get ticket data
while True:

    print()
    # ask user for their name

    name = not_blank("Name: ")  # replace with call to 'not blank' function!
    # if name is exit cade, break out of loop
    if name == "xxx":
        break
    # ask user for their age and checks it's between 12 and 120
    age = int_check("Age: ")

    # Ask error message / success message
    if age < 12:
        print(f"Sorry you are too young for this movie.")
        continue
    elif age > 120:
        print(f"{name} is too old")
        continue
    else:
        pass

    # ask user for payment method
    pay_method = string_check("Payment method: ", payment_ans, 2)
    print(f"{name} had bought a ticket ({pay_method})")

    tickets_sold += 1

if tickets_sold == MAX_TICKETS:
    print(f"You have sold all the tickets (ie: {MAX_TICKETS} tickets")
else:
    print(f"You have sold {tickets_sold} / {MAX_TICKETS} tickets."
          f"")

