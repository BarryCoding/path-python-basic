import random

print("🎮 Welcome to the role-playing game!")

# The player starts with 100 health, the monster with 150 health (it’s big!)
player_health = 100
monster_health = 150


def almost_game_over_check():
    """print a warning message if the player or the monster is almost dead."""
    global player_health, monster_health
    if player_health <= 20:
        print("🆘 You are almost dead! You should heal!")

    if monster_health <= 15:
        print("🎉 The monster is almost dead! Victory is near!")


def calculate_damage(min_damage: int, max_damage: int):
    """double-damage critical hits that happen when an attack value is a factor of 3."""
    damage = random.randint(min_damage, max_damage)
    if damage % 3 == 0:
        damage = damage * 2
        print(f"💥💥 D-D-D-DOUBLE DAMAGE!")
    return damage


def player_attack():
    """If the player attack, the player deal between 10- 15 damage to the monster"""
    damage = calculate_damage(10, 15)
    global monster_health
    monster_health -= damage
    print(f"🥷 You attacked the monster for {damage} damage!")
    if monster_health <= 0:
        print("🏆 You defeated the monster!")


def player_heal():
    """If the player heal, the player regain 30 health, up to a maximum of 100."""
    global player_health
    player_health += 30
    if player_health > 100:
        player_health = 100
    print(f"✨ You healed for 30 health!")


def player_run():
    print("🏃 You ran away!")


def get_player_action():
    try:
        # The player can choose to attack, heal, or run away.
        action = input("👤 Do you want to (A)ttack, (H)eal, or (R)un away: ")
        action = action.upper()
        return action
    except KeyboardInterrupt:
        # Prevent the player from exiting the game by pressing Ctrl + C.
        print("\n❌ You can't quit the game by pressing Ctrl+C.")
        print("❗ If you really want to leave, you'll need to (R)un...")
        return "continue"


def player_action(action: str):
    """If the player choose to attack, heal, or run away, the player action is performed."""
    if action == "A":
        player_attack()
        return "done"
    elif action == "H":
        player_heal()
        return "done"
    elif action == "R":
        player_run()
        return "break"
    else:
        print("❌ Invalid action. Please choose A, H, or R.")
        return "continue"


def monster_attack():
    """if the monster is still alive, it deals 15- 20 damage to the player."""
    global player_health, monster_health
    if monster_health <= 0:
        return
    damage = calculate_damage(15, 20)
    player_health -= damage
    print(f"🐲 The monster attacked you for {damage} damage! \n")
    if player_health <= 0:
        print("💀 You were defeated by the monster!")


def game_loop():
    game_round = 0
    # The game continues until either the player or the monster’s health reaches 0, or the player runs away.
    while player_health > 0 and monster_health > 0:
        game_round += 1
        print(f"🔄 Game Round {game_round}")
        almost_game_over_check()

        action = get_player_action()
        if action == "continue":
            continue

        result = player_action(action)
        if result == "break":
            break
        elif result == "continue":
            continue
        elif result == "done":
            pass

        # After the player’s turn
        monster_attack()


game_loop()
