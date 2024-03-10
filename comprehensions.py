import math


numbers: list[int] = [49, 64, 81, 100, 121]

new_list: list[int] = [int(math.sqrt(n)) for n in numbers if n % 2 == 0]

print(f"{new_list = }")

team_1: list[str] = ["Janet", "Arya", "Mary"]
team_2: list[str] = ["Evan", "Jake", "Randy"]

new_teams: list[tuple] = [(x, y) for x in team_1 for y in team_2]

print(f"{new_teams = }")
