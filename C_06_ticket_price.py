
# functions here
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

# Main routine here

# ticket prices
CHILD_PRICE = 7.50
ADULT_PRICE = 10.50
SENIOR_PRICE = 8.50


# credit surcharge 5%
CREDIT_SURCHARGE = 0.05

# initialise variable / non-default options for string checker
payment_ans = ('cash', 'credit')

# loop for testing purposes...
while True:
    print()

    # ask user for their name
    name = input("Name: ") # replace with call to 'not blank' function!

    # ask user for their age and checks it's between 12 and 120
    age = int_check("Age: ")

    # Ask error message / success message
    if age < 12:
        print(f"{name} is too young")
        continue

    #     child ticket price is $7.50
    elif 12 <= age < 16:
        ticket_price = CHILD_PRICE

    # Adult ticket $10.50
    elif 16<= age <65:
        ticket_price = ADULT_PRICE

    # Senior Citizen ticket 8.50
    elif 65 <= age < 121:
        ticket_price = SENIOR_PRICE

    else:
        print(f"{name} is too old")
        continue

    # ask user for payment method
    pay_method = string_check( "Payment method: ", payment_ans, 2)
    if pay_method == "cash":
        surcharge = 0

    # if paying by credit calculate surcharge
    else:
        surcharge = ticket_price * CREDIT_SURCHARGE

    # calculate total payable..
    total_to_pay = ticket_price + surcharge

    print(f"{name}'s ticket cost ${ticket_price:.2f}, they paid by {pay_method} "
          f"so the surcharge is ${surcharge:.2f}\n"
          f"The total payable is ${total_to_pay:.2f}\n")
