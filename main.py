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
    def __init__(self,id,team_name):
        self.id=id
        self.team_name=team_name
class Hero(Unit):
    #class Hero
    def __init__(self,id,team_name,lvl=1):
        Unit.__init__(self,id,team_name)
        self.lvl=lvl
        self.team_name=team_name
        self.team=Team(team_name)

    def lvl_up(self):
        #method of increasing the level
        self.lvl+=1

class Soldier(Unit):
    #class Soldier
    def __init__(self,id,team_name):
        Unit.__init__(self,id,team_name)
        self.gtth=1
    def goin_to_the_hero(self,gtth):
        #method going fo the hero
        self.gtth=gtth
        print('я, ',self.id,' иду за героем ',self.gtth.id)

class Team:
    #class Teams
        def __init__(self,team_name):
            self.team_name=team_name
            self.team=[]


def belonging_to_the_teem():
    #belonging to the team GDI or NOD
    b = random.randint(1, 4)
    if b % 2 == 0:
        return (hero_list[0])
    else:
        return (hero_list[1])
def general_lvl_up():
    #determining who lvl up
    if length_GDI > length_NOD:
        generalGDI.lvl_up()
    elif length_NOD > length_GDI:
        generalNOD.lvl_up()
    else:
        generalGDI.lvl_up()
        generalNOD.lvl_up()
hero_list=[]


generalGDI=Hero(int(uuid.uuid4()),'GDI')
hero_list.append(generalGDI)
generalNOD=Hero(int(uuid.uuid4()),'NOD')
hero_list.append(generalNOD)

number_of_soldiers=100

for k in range(number_of_soldiers):
    #generate soldiers and distribute to team NOD or GDI
    teams=belonging_to_the_teem()
    s=Soldier(int(uuid.uuid4()),teams.team_name)
    if s.team_name==hero_list[0].team.team_name:
        hero_list[0].team.team.append(s)
    else:
        hero_list[1].team.team.append(s)


length_GDI=len(hero_list[0].team.team)
length_NOD=len(hero_list[1].team.team)
print('команда GDI ',length_GDI,' солдат')
print('команда NOD ',length_NOD,' солдат')

general_lvl_up()
hero_list[0].team.team[4].goin_to_the_hero(hero_list[0])
