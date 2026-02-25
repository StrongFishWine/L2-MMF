import pandas

# lists to hold ticket details
all_names = ["A", "B", "C", "D", "E"]
all_ticket_costs = [7.50, 7.50, 10.50, 10.50, 6.50]
all_surcharges = [0, 0, 0.53, 0.53, 0]

mini_movie_dict = {
    'Name': all_names,
    'Ticket Price': all_ticket_costs,
    'Surcharge': all_surcharges
}

# create dataframe / table from dictionary
mini_movie_frame = pandas.DataFrame(mini_movie_dict)

print(mini_movie_frame)