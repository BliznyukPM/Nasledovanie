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
    def __init__(self,name_hero,id,team,lvl=1):
        Unit.__init__(self,id,team)
        self.lvl=lvl
        self.name_hero=name_hero
    def lvl_up(self):
        #method of increasing the level
        self.lvl+=1
class Soldier(Unit):
    #class Soldier
    def __init__(self,id,team,gofh=False):
        Unit.__init__(self,id,team)
        self.gofh=gofh
    def goin_to_the_hero(self):
        #method going fo the hero
        self.gofh=True

'''
def coin():
    #function coin for random
    b = random.randint(1,4)
    if b % 2 == 0:
        return (True)
    else:
        return (False)
'''
def belonging_to_the_teem():
    #belonging to the team GDI or NOD
    b = random.randint(1, 4)
    if b % 2 == 0:
        return ('NOD')
    else:
        return ('GDI')
def general_lvl_up():
    #determining who lvl up
    if length_GDI > length_NOD:
        generalGDI.lvl_up()
    elif length_NOD > length_GDI:
        generalNOD.lvl_up()
    else:
        generalGDI.lvl_up()
        generalNOD.lvl_up()

generalGDI=Hero(int(uuid.uuid4()),'GDI')
generalNOD=Hero(int(uuid.uuid4()),'NOD')

number_of_soldiers=100
list_NOD=[]             #list team Nod
list_GDI=[]             #list team GDI
list_soldiers=[Soldier(int(uuid.uuid4()),belonging_to_the_teem()) for i in range(number_of_soldiers)] #list all soldier
'''
for i in range(number_of_soldiers):
    list_soldiers.append(Soldier(int(uuid.uuid4()),belonging_to_the_teem()))
'''
for k in range(len(list_soldiers)):
    #distribute soldiers to team NOD or GDI
    if list_soldiers[k].team=='NOD':
        list_NOD.append(list_soldiers[k])
    else:
        list_GDI.append(list_soldiers[k])

length_NOD=len(list_NOD)
length_GDI=len(list_GDI)
print('команда GDI ',length_GDI,' солдат')
print('команда NOD ',length_NOD,' солдат')

general_lvl_up()

list_GDI[0].goin_to_the_hero()
print('id солдата следующего за генералом ',list_GDI[0].id)
print('id генерала за которым следует солдат ',generalGDI.id)
