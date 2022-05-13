import random

round_number = 0


class GameEntity:
    def __init__(self, name, hp, damage):
        self.__name = name
        self.__hp = hp
        self.__damage = damage

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, value):
        if value > 0:
            self.__hp = value
        else:
            self.__hp = 0


    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        self.__damage = value

    def __str__(self):
        return f"{self.name} HP: {self.hp} [{self.damage}]"


class Boss(GameEntity):
    def __init__(self, name, hp, damage):
        GameEntity.__init__(self, name, hp, damage)


class Hero(GameEntity):
    def __init__(self, name, hp, damage, skill):
        GameEntity.__init__(self, name, hp, damage)
        self.__skill = skill

    @property
    def skill(self):
        return self.__skill

    @skill.setter
    def skill(self, value):
        self.__skill = value

    def apply_super_power(self, boss, heroes):
        pass


class Warrior(Hero):
    def __init__(self, name, hp, damage):
        Hero.__init__(self, name, hp, damage, "CRITICAL DAMAGE")

    def apply_super_power(self, boss, heroes):
        coeff = random.randint(2, 5)
        boss.hp -= coeff * self.damage
        print(f"{self.name} hit critically: {coeff * self.damage}")


class Magic(Hero):
    def __init__(self, name, hp, damage):
        Hero.__init__(self, name, hp, damage, "BOOST")

    def apply_super_power(self, boss, heroes):
        boost = random.randint(5, 10)
        for hero in heroes:
            if hero.hp > 0:
                hero.damage += boost


class Medic(Hero):
    def __init__(self, name, hp, damage, heal_points):
        Hero.__init__(self, name, hp, damage, "HEAL")
        self.__heal_points = heal_points

    def apply_super_power(self, boss, heroes):
        for hero in heroes:
            if hero.hp > 0 and self != hero:
                hero.hp += self.__heal_points


class Berserk(Hero):
    def __init__(self, name, hp, damage):
        Hero.__init__(self, name, hp, damage, "SAVE DAMAGE AND RETURN")

    def apply_super_power(self, boss, heroes):
        damage_range = [5, 10, 15]
        saved = random.choice(damage_range)
        self.hp += saved
        boss.hp -= saved


def start():
    boss = Boss(name="Sai", hp=1000, damage=50)

    warrior = Warrior("Ahiles", 270, 15)
    medic_1 = Medic("Aibolit", 200, 5, 15)
    magic = Magic("Bairon", 280, 30)
    berserk = Berserk("Titan", 250, 10)
    medic_2 = Medic("Medbrat", 230, 10, 5)

    heroes = [warrior, medic_1, magic, berserk, medic_2]
    print_stats(boss, heroes)

    while not is_game_finished(boss, heroes):
        if boss.hp <= 0:
            print('Heroes won!!!')
            break
        play_round(boss, heroes)



def print_stats(boss, heroes):
    print(f"------------------ ROUND: {round_number} ------------------")
    print(boss)
    for hero in heroes:
        print(hero)


def boss_hits(boss, heroes):
    for hero in heroes:
        if hero.hp > 0 and boss.hp > 0:
            hero.hp -= boss.damage


def heroes_hit(boss, heroes):
    for hero in heroes:
        if hero.hp > 0 and boss.hp > 0:
            boss.hp -= hero.damage


def heroes_skills(boss, heroes):
    for hero in heroes:
        if hero.hp > 0 and boss.hp > 0:
            hero.apply_super_power(boss, heroes)


def is_game_finished(boss, heroes):
    if boss.hp <= 0:
        print("Heroes won!!!")
        return False

    all_heroes_dead = True
    for hero in heroes:
        if hero.hp > 0:
            all_heroes_dead = False
            break

    if all_heroes_dead:
        print("Boss won loxi!!!")
    return all_heroes_dead


def play_round(boss, heroes):
    global round_number
    round_number += 1
    boss_hits(boss, heroes)
    heroes_hit(boss, heroes)
    heroes_skills(boss, heroes)
    print_stats(boss, heroes)


start()
