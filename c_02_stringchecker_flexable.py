
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


# Main routine here goes
payment_ans = ('cash','credit')

want_instructions = string_check("Do you want to see the instructions? ", ['yes', 'no'])
print(f"You chose {want_instructions}")
pay_method = string_check( "Payment method: ", payment_ans, 2)
print(f"You chose {pay_method}")