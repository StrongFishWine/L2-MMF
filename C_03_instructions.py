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

# Main routine goes here

make_statement( "Mini-Movie Fundraiser Program", "🍿")

print()
want_instructions = string_check("Do you want to see the instructions? ")

if want_intructions == "yes":
    instruction()

print()
print("program continues...")

