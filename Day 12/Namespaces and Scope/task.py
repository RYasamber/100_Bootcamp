enemies = 1


def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")
player_health = 10
def game():
    def drink_potion():
        player_health += 2
        print(player_health)

    drink_potion()

print(player_health)
