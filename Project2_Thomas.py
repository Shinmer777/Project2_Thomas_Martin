levels = [1, 2, 3, 4, 5]
coins = [5, 8, 3, 10, 7]
enemies = [2, 4, 1, 5, 3]
power_ups = ["Mushroom", "Star", "Flower", "Mushroom", "Star"]
level_scores = []
actions = [0, 1, 0, 2, 1]
action_results = []
player_name = "Hero"
lives = 3
score = 0
total_coins = 0
life_history= []
bonus_coin_levels=[]
inventory = ["Mushroom", "Star", "Flower"]
used_powerups = ["Mushroom", "Star"]
narcoimo=0
avcole = sum(coins) / len(levels)
narenmo=0
high_score=[]
score_his=0
score_history=[]
print(f"===Platform Adventure===")
for i in range(len(levels)):
    print(f"Level {levels[i]}\nCoins:{coins[i]}\nEnemies:{enemies[i]}\nPower-Up:{power_ups[i]}\n")
print(f"===Player Info===\nName:{player_name}\n{player_name} has {lives} lives left.\nScore: {score}\nTotal coins: {total_coins}\n")
print("=== Level Scores ===")
for i in range(len(levels)):
    level_score = coins[i] * 10 - enemies[i] * 5
    if power_ups[i] == "Star":
        level_score += 25
    print(f"Level {levels[i]} Score: {level_score}")
    level_scores.append(level_score)
print(f'\n===Adventure Actions===')
for i in range(len(levels)):
    if actions[i] == 0:
        print(f"Level {levels[i]}: Collect Coins")
    elif actions[i] == 1:
        print(f"Level {levels[i]}: Fight Enemies")
    elif actions[i] == 2:
        print(f"Level {levels[i]}: Use Power-Up")
for i in range(len(actions)):
    if actions[i] == 0:
        action_results.append(0)
    elif actions[i] == 1:
        action_results.append(1)
    elif actions[i] == 2:
        action_results.append(2)
print(f"\n===Life History===")
for i in range(len(levels)):
    if power_ups[i] == "Star":
        lives -= 0
    else:
        if enemies[i] >= 4:
            lives -=1
    life_history.append(lives)
    print(f"After Level {levels[i]}: {lives} lives")
print(f"\n===Coin Collection===")
for i in range(len(levels)):
    total_coins += coins[i]
    if coins[i] >= 7:
        bonus_coin_levels.append(coins[i])
print(f"Coins Collected: {total_coins}\nLevels with 7 or more coins: {bonus_coin_levels}")
print(f"\n===Power-Up Inventory===\nStarting Inventory: {inventory}\nUsed Power-Ups: {used_powerups}")
inventory.pop(0)
inventory.pop(0)
print(f"Remaining Inventory: {inventory}")
print(f"\n===Level Analysis===\nTotal Coins: {total_coins}")
for coin in coins:
    if coin > narcoimo:
        narcoimo = coin
print(f"Most Coins in One Level: {narcoimo}")
for coin in coins:
    if coin < narcoimo:
        narcoimo = coin
print(f"Fewest Coins in One Level: {narcoimo}\nAverage Coins per Level: {avcole}\nTotal Enemies: {sum(enemies)}")
for enemy in enemies:
    if enemy > narenmo:
        narenmo = enemy
print(f"Most Enemies in One Level: {narenmo}\n\n===High Scores===")
for i in range(len(levels)):
    if level_scores[i] >= 50:
        high_score.append(level_scores[i])
print(f"Scores of 50 or Higher: {high_score}\n\n===Score History===")
for i in range(len(levels)):
    score_his += level_scores[i]
    score_history.append(score_his)
    print(f"After Level {levels[i]}: {score_his}")
print(f"\nFirst Two Score: {score_history[:2]}\nLast Two Scores: {score_history[-2:]}\n")
print(f"===Final Status===")
if lives == 0:
    print("Game Over")
elif score_his >= 250:
    print("Adventure Champion")
elif score_his >= 150:
    print("Great Adventure")
else:
    print("Keep Trying")
print(f"\n===Adventure Ranking===\nFinal Score: {score_his}\nFinal Lives: {lives}\nRank: Legend")