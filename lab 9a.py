#Sitong Guo

# Create a rock-paper-scissors game!
# - Play once and report the result
# - Play in a loop and record how many wins and losses happen?
# - Allow choosing how many human players there are, from 0-2?
# - Organize everything into functions?
# - Organize everything into classes??

from numpy import random

choices = ['rock', 'paper', 'scissors']

p1 = input('Pick one of rock, paper or scissors: ')
p2 = random.choice(choices)

def win(p1, p2):
    if p1 == p2:
        return "Tie!"
    elif (p1 == 'rock' and p2 == 'scissors') or (p1 == 'paper' and p2 == 'rock') or (p1 == 'scissors' and p2 == 'paper'):
        return 'Player 1 victory!'
    else:
        return 'Player 2 victory!'

#organize into function::
def play_once(num_human_players):
    if num_human_players == 0:
        p1 = random.choice(choices)
        p2 = random.choice(choices)
        print(f'Computer 1 picked: {p1}')
        print(f'Computer 2 picked: {p2}')
    elif num_human_players == 1:
        p1 = input('Pick one of rock, paper or scissors: ')
        p2 = random.choice(choices)
        print(f'Computer picked: {p2}')
    else:  
        p1 = input('Player 1, pick one of rock, paper, or scissors: ')
        p2 = input('Player 2, pick one of rock, paper, or scissors: ')

    result = win(p1, p2)
    print(result)

def play_in_loop(num_games, num_human_players):
    wins, losses, ties = 0, 0, 0
    for _ in range(num_games):
        if num_human_players == 0:
            p1 = random.choice(choices)
            p2 = random.choice(choices)
            print(f'Computer 1 picked: {p1}')
            print(f'Computer 2 picked: {p2}')
        elif num_human_players == 1:
            p1 = input('Pick one of rock, paper or scissors: ')
            p2 = random.choice(choices)
            print(f'Computer picked: {p2}')
        else:  
            p1 = input('Player 1, pick one of rock, paper, or scissors: ')
            p2 = input('Player 2, pick one of rock, paper, or scissors: ')

        result = win(p1, p2)
        if result == 'Player 1 victory!':
            wins += 1
        elif result == 'Player 2 victory!':
            losses += 1
        else:
            ties += 1
        print(result)
    print(f'\nPlayer 1 Results: {wins} WONS, {losses} DEFEATs, {ties} Tied')

def main():
    print("~~RockPaperScissors Game~~")
    num_human_players = int(input("Enter number of human players (0, 1, or 2): "))
    
    if num_human_players not in [0, 1, 2]:
        print("Invalid number ")
        return
    
    mode = input("set game mode: 1 (Play once), 2 (Play in loop): ")
    
    if mode == '1':
        play_once(num_human_players)
    elif mode == '2':
        num_games = int(input("How many rounds to play? "))
        play_in_loop(num_games, num_human_players)
    else:
        print("go see a doctor!")

if __name__ == "__main__":
    main()

#organize into classes:
class RockPaperScissors:
    def __init__(self):
        self.choices = ['rock', 'paper', 'scissors']
        self.wins = 0
        self.losses = 0
        self.ties = 0

    def win_c(self, p1, p2):
        if p1 == p2:
            return "tie!"
        elif (p1 == 'rock' and p2 == 'scissors') or (p1 == 'paper' and p2 == 'rock') or (p1 == 'scissors' and p2 == 'paper'):
            return 'Player 1 victory!'
        else:
            return 'Player 2 victory!'

    def play_once_c(self, num_human_players):
        if num_human_players == 0:
            p1 = random.choice(self.choices)
            p2 = random.choice(self.choices)
            print(f'Computer 1 picked: {p1}')
            print(f'Computer 2 picked: {p2}')
        elif num_human_players == 1:
            p1 = input('Pick one of rock, paper or scissors: ')
            p2 = random.choice(choices)
            print(f'Computer picked: {p2}')
        else:  
            p1 = input('Player 1, pick one of rock, paper, or scissors: ')
            p2 = input('Player 2, pick one of rock, paper, or scissors: ')

        result = self.win_c(p1, p2)
        print(result)

    def play_in_loop_c(self, num_games, num_human_players):
        for _ in range(num_games):
            if num_human_players == 0:
                p1 = random.choice(self.choices)
                p2 = random.choice(self.choices)
                print(f'Computer 1 picked: {p1}')
                print(f'Computer 2 picked: {p2}')
            elif num_human_players == 1:
                p1 = input('Pick one of rock, paper or scissors: ')
                p2 = random.choice(choices)
                print(f'Computer picked: {p2}')
            else:  
                p1 = input('Player 1, pick one of rock, paper, or scissors: ')
                p2 = input('Player 2, pick one of rock, paper, or scissors: ')

            result = self.win_c(p1, p2)
            if result == 'Player 1 victory!':
                self.wins += 1
            elif result == 'Player 2 victory!':
                self.losses += 1
            else:
                self.ties += 1
            print(result)
        
        print(f'\nPlayer 1 Results: {self.wins} VICTORIES, {self.losses} DEFEATS, {self.ties} Ties')

def main_c():
    game = RockPaperScissors()
    print("Let's roll RockPaperScissors !")
    num_human_players = int(input("Enter number of human players (0, 1, or 2): "))
    
    if num_human_players not in [0, 1, 2]:
        print("Invalid number")
        return
    
    mode = input("Choose game mode: 1 (Play once), 2 (Play in loop): ")
    
    if mode == '1':
        game.play_once_c(num_human_players)
    elif mode == '2':
        num_games = int(input("How many rounds? "))
        game.play_in_loop_c(num_games, num_human_players)
    else:
        print("go see a doctor!")

if __name__ == "__main__":
    main_c()