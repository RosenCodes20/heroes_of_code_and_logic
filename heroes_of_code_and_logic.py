number_of_heroes = int(input())
heroes_dict = {}
for heroes in range(number_of_heroes):
    hero_name, hp, mp = input().split()
    hp, mp = int(hp), int(mp)
    if hero_name not in heroes_dict:
        heroes_dict[hero_name] = {"hp": hp, "mp": mp}

command = input()
while command != "End":
    current_command = command.split(" - ")
    if current_command[0] == "CastSpell":
        hero_name, mp_needed, spell_name = current_command[1], int(current_command[2]), current_command[3]
        if mp_needed <= heroes_dict[hero_name]["mp"]:
            heroes_dict[hero_name]["mp"] -= mp_needed
            print(f"{hero_name} has successfully cast {spell_name} and now has {heroes_dict[hero_name]['mp']} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")

    elif current_command[0] == "TakeDamage":
        hero_name, damage, attacker = current_command[1], int(current_command[2]), current_command[3]
        heroes_dict[hero_name]["hp"] -= damage
        if heroes_dict[hero_name]["hp"] > 0:
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes_dict[hero_name]['hp']} HP left!")
        else:
            heroes_dict.pop(hero_name)
            print(f"{hero_name} has been killed by {attacker}!")

    elif current_command[0] == "Recharge":
        max_mp = 200
        hero_name, amount = current_command[1], int(current_command[2])
        amount_to_add = min(amount, max_mp - heroes_dict[hero_name]["mp"])
        heroes_dict[hero_name]["mp"] += amount_to_add
        print(f"{hero_name} recharged for {amount_to_add} MP!")

    elif current_command[0] == "Heal":
        max_heal = 100
        hero_name, amount = current_command[1], int(current_command[2])
        amount_to_add = min(amount, max_heal - heroes_dict[hero_name]["hp"])
        heroes_dict[hero_name]["hp"] += amount_to_add
        print(f"{hero_name} healed for {amount_to_add} HP!")

    command = input()

for name, hp_mp in heroes_dict.items():
    print(f"{name}")
    print(f"HP: {hp_mp['hp']}")
    print(f"MP: {hp_mp['mp']}")
