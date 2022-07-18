from flask import request
from equipment import Equipment
from hero_classes import unit_classes
from unit import PlayerUnit, EnemyUnit


def get_data_for_choosing(hero=False) -> dict:
    classes = unit_classes
    weapons = Equipment().get_weapons_names()
    armors = Equipment().get_armors_names()
    data = {
        "classes": classes,
        "weapons": weapons,
        "armors": armors,
    }
    if hero:
        header = 'Выберите героя'
        button_name = 'Выбрать героя'
        data['header'] = header
        data['button'] = button_name
    else:
        header = 'Выберите врага'
        button_name = "Выбрать врага"
        data['header'] = header
        data['button'] = button_name
    return data


def get_unit_from_form(hero=False):
    name = request.form['name']
    armor_name = request.form['armor']
    weapon_name = request.form['weapon']
    unit_class = request.form['unit_class']
    if hero:
        player = PlayerUnit(name=name, unit_class=unit_classes.get(unit_class))
        player.equip_weapon(Equipment().get_weapon(weapon_name))
        player.equip_armor(Equipment().get_armor(armor_name))
        return player
    else:
        enemy = EnemyUnit(name=name, unit_class=unit_classes.get(unit_class))
        enemy.equip_weapon(Equipment().get_weapon(weapon_name))
        enemy.equip_armor(Equipment().get_armor(armor_name))
        return enemy
