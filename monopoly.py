import random

TILES_LIST = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]
TILES_DICT = {
    0: ["Go", 0],
    1: ["Meditterean Avenue", 0],
    2: ["Community Chest", 0],
    3: ["Baltic Ave", 0],
    4: ["Income Tax", 0],
    5: ["Reading Railroad", 0],
    6: ["Oriental Avenue", 0],
    7: ["Chance", 0],
    8: ["Vermont Avenue", 0],
    9: ["Connecticut Avenue", 0],
    10: ["Jail", 0],
    11: ["St. Charles Place", 0],
    12: ["Electric Company", 0],
    13: ["States Avenue", 0],
    14: ["Virginia Avenue", 0],
    15: ["Pennsylvania Railroad", 0],
    16: ["St. James Place", 0],
    17: ["Community Chest", 0],
    18: ["Tennessee Avenue", 0],
    19: ["New York Avenue", 0],
    20: ["Free Parking", 0],
    21: ["Kentucky Avenue", 0],
    22: ["Chance", 0],
    23: ["Indiana Avenue", 0],
    24: ["Illinous Avenue", 0],
    25: ["B&O Railroad", 0],
    26: ["Atlantic Avenue", 0],
    27: ["Ventnor Avenue", 0],
    28: ["Water Works", 0],
    29: ["Marvin Gardens", 0],
    30: ["Go to Jail", 0],
    31: ["Pacific Avenue", 0],
    32: ["North Carolina Avenue", 0],
    33: ["Community Chest", 0],
    34: ["Pennsylvania Avenue", 0],
    35: ["Short Line", 0],
    36: ["Chance", 0],
    37: ["Park Place", 0],
    38: ["Luxury Tax", 0],
    39: ["Boardwalk", 0]
}
position = 0
num_rolls = 100000

### Simulations ###

def dice_roll():
    return random.randrange(1, 7) + random.randrange(1, 7)

def move():
    global position
    # print("Start position: " + str(TILES_DICT[position][0]))
    num_tiles = dice_roll()
    # print("Dice roll: " + str(num_tiles))
    position += num_tiles
    if position >= 40:
        position = position - 40
    # print("End position: " + str(TILES_DICT[position][0]))
    TILES_DICT[position][1] += 1 
    if position == 30:
        position = 10
    # print()

for roll in range(num_rolls):
    move()


for tile in TILES_DICT.values():
    print(tile[0], ",", tile[1])