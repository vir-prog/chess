import random
list_of_players = []
def get_players():
    no_of_players = int(input('Number of Players: '))
    return no_of_players

def get_player_names(no_of_players):
    for a in range(no_of_players):
        a = input('player name: ')
        list_of_players.append(a)

def roll_dice():
    outcomes = ['1', '2', '3', '4', '5', '6']
    outcome = random.choice(outcomes)
    i = 1
    while outcome.endswith('6') and i < 3:
        outcome = outcome + ', ' + random.choice(outcomes)
        i += 1
    return outcome

def final_result():
    for player in list_of_players:
        input(f"{player}'s Turn andpress enter! ")
        result = roll_dice()
        print(f"{player} got {result}")

if __name__ == "__main__":
    get_player_names(get_players())
    while 1:
        final_result()
