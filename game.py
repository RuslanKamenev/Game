import random

class Game():

    #Выбор кто будет ходить: 0-игрок, 1-компьютер
    @staticmethod
    def activePlayerChose(user, computer):
        move = random.randint(0, 1)
        if move == 0:
            active = user
            enemy = computer
        else:
            active = computer
            enemy = user
        return active, enemy

    #Выбор шанса действия для функции actionChose(). 
    #Выбирается случайное число в интервале от 0 до maxChance
    #При полном здоровье атакующего chance=1 случайный выбор атак с шансом 50%
    #При неполном здоровье chance=2, шанс нанесения урона или исцеления 33%
    #При снижении здоровья компьютера ниже критического, при его ходе, chance=5, шанс исцеления = 66%
    @staticmethod
    def actionChance(player, maxHealth, CRITICAL_HEALTH):
        if player.getName() == 'Компьютер' and player.getHealth() < maxHealth*CRITICAL_HEALTH:
            maxChance = 5
        elif player.getHealth() < maxHealth:
            maxChance = 2
        else:
            maxChance = 1
        chance = random.randint(0, maxChance)
        return chance

    #Различные типы действий, в зависимости от chance полученного из функции actionChance(): 0-обычный удар, 1-сильный удар, остальные значения - исцеление
    @staticmethod
    def actionChose(chance, active, enemy, maxHealth):
        if chance == 0:
            damage = random.randint(18, 25)
            enemy.setlDamage(damage)
            print(active.getName(), 'использует обычный удар и наносит', damage, 'урона.')
        elif chance == 1:
            damage = random.randint(10, 35)
            enemy.setlDamage(damage)
            print(active.getName(), 'использует сильный удар и наносит', damage, 'урона.')
        else:
            heal = random.randint(18, 25)
            active.setHeal(heal, maxHealth)
            print(active.getName(), 'восстановил', heal, 'едениц здоровья.')

    #Функция для каждого хода с правилами игры
    @staticmethod
    def battle(user, computer, turn, maxHealth):
        #критический уровень здоровья, ниже которого увеличивается вероятность исцеления компьютера
        CRITICAL_HEALTH = 0.35
        activePlayers = Game.activePlayerChose(user, computer)
        active = activePlayers[0]
        enemy = activePlayers[1]
        print('Ход №', turn, '. Ходит ', active.getName(), '.', sep='')
        chance = Game.actionChance(active, maxHealth, CRITICAL_HEALTH)
        Game.actionChose(chance, active, enemy, maxHealth)
        print('Здоровье игрока', user.getName(), 'составляет', user.getHealth(), 'очков.', computer.getName(), 'имеет', computer.getHealth(), 'здоровья.')