import pandas
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

def currency(x):
    return "${:.2f}".format(x)

# lists to hold ticket details
all_names = ["A", "B", "C", "D", "E"]
all_ticket_costs = [7.50, 7.50, 10.50, 10.50, 6.50]
all_surcharges = [0, 0, 0.53, 0.53, 0]

mini_movie_dict = {
    'Name': all_names,
    'Ticket Price': all_ticket_costs,
    'Surcharge': all_surcharges
}

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
    elif age < 16:
        ticket_price = CHILD_PRICE

    # Adult ticket $10.50
    elif age <65:
        ticket_price = ADULT_PRICE

    # Senior Citizen ticket 8.50
    elif age < 121:
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

    # add name, ticket cost and surcharge to
    all_names.append(name)
    all_ticket_costs.append(ticket_price)
    all_surcharges.append(surcharge)

# create dataframe / table from dictionary
mini_movie_frame = pandas.DataFrame(mini_movie_dict)

# Calculate the total payable & profit for each ticket
mini_movie_frame['Total'] = mini_movie_frame['Ticket Print'] + mini_movie_frame['Surcharge']
mini_movie_frame['Profit'] = mini_movie_frame['Ticket Prince'] - 5

# Work out total paid and total profit...
total_paid = mini_movie_frame['Total'].sum()
total_profit = mini_movie_frame['Profit'].sum()

# Currency Formatting (uses currency function)
add_dollars = ['Ticket Price',  'Surcharge', 'Total', 'Profit']
for var_item in add_dollars:
    mini_movie_frame[var_item] = mini_movie_frame[var_item].apply(currency)

# Output movie fram without index
# print(mini_movie_frame)
print(mini_movie_frame.to_string(index=False))

print()
print(f"Total Pain: ${total_paid:.2f}")
print(f"Total Profit: ${total_profit:.2f}")