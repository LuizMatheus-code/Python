#Disclaimer: Undertale belongs to Toby Fox, i do not own any of the characters used here.
from time import sleep
from random import randint
class Character:
    def __init__(self, name, life, attack, defense):
        self.name = name.capitalize()
        self.life = life
        self.attack = attack
        self.defense = defense


    @classmethod
    def more_life(cls, life):
        try:
            life += 10
            return life
        except Exception as fail:
            print(fail)


    def fight(self, opponent):
        winner = None
        try:
            opponent_lifepoints = opponent.life
            opponent_name = opponent.name
            opponent_attackpoints = opponent.attack
            sleep(1)
            print(f'{self.name} ({self.life}, {self.attack}) VS {opponent_name} ({opponent_lifepoints}, {opponent_attackpoints})')
            sleep(1)
            while True:
                randomness = randint(1, 2)
                if self.life > 0 and opponent_lifepoints > 0:
                    if randomness == 1:
                        print(f'\nPlayer {randomness}\n{self.name} attacks')
                        sleep(2)
                        opponent_lifepoints -= self.attack
                        print(f'{self.name}: {self.life}\n{opponent_name}: {opponent_lifepoints}')
                        sleep(1.5)
                    else:
                        print(f'\nPlayer {randomness}\n{opponent_name} attacks')
                        sleep(2)
                        self.life -= opponent_attackpoints
                        print(f'{self.name}: {self.life}\n{opponent_name}: {opponent_lifepoints}')
                        sleep(1.5)
                else:
                    break
            if self.life <= 0:
                winner = f'\n{opponent_name} won with {opponent_lifepoints} HP'
            else:
                winner = f'\n{self.name} won with {self.life} HP'
        except:
            print('something went wrong')
        finally:
            return winner

    @staticmethod
    def sans_gaster_blaster(charac):
        try:
            character_name = charac.name.capitalize()
            character_attack = charac.attack
            if character_name == "Sans":
                character_attack *= 10
                return character_attack
            else:
                return NameError
        except Exception as error:
            return error


class Human(Character):
    def __init__(self, name, life, attack, defense):
        self.name = name.capitalize()
        self.life = life
        self.attack = attack
        self.defense = defense


    def __str__(self):
        return(f'{self.name}\nLife: {self.life}\nAttack: {self.attack}\nDefense: {self.defense}')


class Monster(Character):
    def __init__(self, name, life, attack, defense):
        self.name = name.capitalize()
        self.life = life
        self.attack = attack
        self.defense = defense


    def __str__(self):
        return f'{self.name}\nLife: {self.life}\nAttack: {self.attack}\nDefense: {self.defense}\nThe easiest enemy. Can only deal 1 damage.'


if __name__ == '__main__':
    chara = Character('Chara', True, None, 999)
