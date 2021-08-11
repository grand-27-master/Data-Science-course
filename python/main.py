from classes.game import person,bcolors
magic=[{"name":"fire","cost":10,"dmg":60},
       {"name":"thunder","cost":10,"dmg":60},
       {"name":"shocker","cost":10,"dmg":60}]
player=person(465,60,30,34,magic)

print(player.generate_damage())
print(player.generate_damage())
print(player.generate_damage())
