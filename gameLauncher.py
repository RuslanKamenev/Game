import random
from participants import Participants 
from game import Game

turn = 0

print ('Введите имя игрока:')
name = input()
print ('Введите здоровье участников игры:')
inputHealth = input()

maxHealth = int(inputHealth)
user = Participants(name, maxHealth)
computer = Participants('Компьютер', maxHealth)

while True:
    turn += 1
    Game.battle(user, computer, turn, maxHealth)

    if user.getHealth() < 0:
        print('Ваше здоровье меньше 1, вы проиграли')
        break
    if computer.getHealth() < 0:
        print('Здоровье противника меньше 1, вы выиграли')
        break

input()