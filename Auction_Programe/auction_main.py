Logo = ['''⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢠⣿⣿⣶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣰⣿⣿⣿⡿⠁⡀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣼⣿⣿⣿⡟⢀⣼⣿⣶⣤⣀⠘⠿⣶⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣼⣿⣿⣿⠟⢀⣾⣿⣿⣿⣿⣿⣷⣦⣄⠉⠻⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢀⣾⣿⣿⣿⠏⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠈⠻⢿⡿⠃⠰⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠆⢠⣿⣷⣦⡀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⣠⣿⣿⣿⡟⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢴⣦⣄⠙⠻⣿⣿⣿⣿⣿⣿⡿⠃⣰⣿⣿⣿⡟⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣈⠙⠻⣶⠄⠉⠛⠿⣿⡿⠁⣼⣿⣿⣿⠟⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⠏⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠛⢿⣿⣿⠋⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢠⣾⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢠⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠛⠛⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀''']

print(Logo[0])
print('Welcome to the secret auction program.')
bidders = []

game_on = 'yes'
while game_on == 'yes':
    name = input('What is your name? :')
    bid = int(input('What is Your Bid?: $'))
    auction = {}
    auction['name'] = name
    auction['bid'] = bid
    bidders.append(auction)
    game_on = input('Are there any other bidders? Type "yes" or "no". ').lower()
    if game_on == 'yes':
        game_on = 'yes'
    else:
        heighst_bid = 0
        winner = ''
        for item in bidders:
            bid_amount = bidders[item]
            if 

        print(f'The winner is {} with a bid of ${}.')

