'''
В некой игре-стратегии есть солдаты и герои. У всех есть свойство, содержащее уникальный номер объекта,
и свойство, в котором хранится принадлежность команде. У солдат есть метод "иду за героем", который
в качестве аргумента принимает объект типа "герой". У героев есть метод увеличения собственного уровня.

В основной ветке программы создается по одному герою для каждой команды. В цикле генерируются объекты-солдаты.
Их принадлежность команде определяется случайно. Солдаты разных команд добавляются в разные списки.

Измеряется длина списков солдат противоборствующих команд и выводится на экран. У героя, принадлежащего
команде с более длинным списком, увеличивается уровень.

Отправьте одного из солдат первого героя следовать за ним. Выведите на экран идентификационные номера
этих двух юнитов.
'''
import random
import uuid

class Unit:
    # parent class Unit
    def __init__(self,id,team):
        self.id=id
        self.team=team
class Hero(Unit):
    #class Hero
    def __init__(self,id,team,lvl=1):
        Unit.__init__(self,id,team)
        self.lvl=lvl
    def lvl_up(self):
        #method of increasing the level
        self.lvl+=1
class Soldier(Unit):
    #class Soldier
    def __init__(self,id,team,gofh=False):
        Unit.__init__(self,id,team)
        self.gofh=gofh
    def goin_fo_the_hero(self):
        #method going fo the hero
        self.gofh+=1

def coin():
    #function coin for random
    b = random.randint(1,4)
    print(b)
    if b % 2 == 0:
        return (True)
    else:
        return (False)

generalNOD=Hero(int(uuid.uuid4()),'NOD')
generalGDI=Hero(int(uuid.uuid4()),'GDI')

