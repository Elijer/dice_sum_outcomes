from itertools import combinations

# The goal of this file is to determine the number of options
# the player will have given a certain number of dice rolled

two_dice_example = [1, 2]

rolls2 = [x for x in combinations(two_dice_example, 1)]
rolls3 = [x for x in combinations(two_dice_example, 2)]
print(f"Plays possible for two dice is {len(rolls2 + rolls3)}")
print(f"Example: {rolls2 + rolls3}")
print(" ")

three_dice_example = [1, 2, 3]

rolls2 = [x for x in combinations(three_dice_example, 1)]
rolls3 = [x for x in combinations(three_dice_example, 2)]
rolls4 = [x for x in combinations(three_dice_example, 3)]
print(f"Plays possible for three dice is {len(rolls2 + rolls3 + rolls4)}")
print(f"Example: {rolls2 + rolls3 + rolls4}")
print(" ")

four_dice_example = [1, 2, 3, 4]

rolls2 = [x for x in combinations(four_dice_example, 1)]
rolls3 = [x for x in combinations(four_dice_example, 2)]
rolls4 = [x for x in combinations(four_dice_example, 3)]
rolls5 = [x for x in combinations(four_dice_example, 4)]
print(f"Plays possible for three dice is {len(rolls2 + rolls3 + rolls4 + rolls5)}")
print(f"Example: {rolls2 + rolls3 + rolls4 + rolls5}")
print(" ")

