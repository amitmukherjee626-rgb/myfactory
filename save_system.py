import json
import os

SAVE_FILE = "savegame.json"

def save_game(money, inventory):

    data = {
        "money": money,
        "inventory": inventory
    }

    with open(SAVE_FILE, "w") as f:
        json.dump(data, f)


def load_game():

    if not os.path.exists(SAVE_FILE):
        return None

    with open(SAVE_FILE, "r") as f:
        return json.load(f)