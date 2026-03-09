import save_system

default_inventory = {

    "wood":0,
    "iron_ore":0,
    "copper_ore":0,
    "stone":0,
    "sand":0,
    "coal":0,
    "oil":0,
    "water":0,

    "plank":0,
    "iron_plate":0,
    "glass":0,
    "machine_part":0,
    "engine":0
}

sell_prices = {

    "wood":6,
    "iron_ore":12,
    "copper_ore":12,
    "stone":6,
    "sand":5,
    "coal":10,
    "oil":20,
    "water":4,

    "plank":20,
    "iron_plate":25,
    "glass":30,
    "machine_part":80,
    "engine":200
}

loaded = save_system.load_game()

if loaded:

    money = loaded["money"]
    inventory = loaded["inventory"]

else:

    money = 1000
    inventory = default_inventory