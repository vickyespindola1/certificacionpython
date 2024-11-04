##piedra,papel,tijera
import random 

def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return f'it is a Tie!, computer Choice {computer}'

    # r > s, s > p, p > r
    if is_win(user, computer):
        return f'You win!, computer Choice {computer}'

    return f'You lost!, computer Choice {computer}'

def is_win(player, opponent):
    # return true if player wins
    # r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True

print(play())