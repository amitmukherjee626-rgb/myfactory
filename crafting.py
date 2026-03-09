import data

def produce_plank():
    if data.inventory["wood"] >= 2:
        data.inventory["wood"] -= 2
        data.inventory["plank"] += 1

def produce_iron_plate():
    if data.inventory["iron_ore"] >= 2:
        data.inventory["iron_ore"] -= 2
        data.inventory["iron_plate"] += 1

def produce_glass():
    if data.inventory["sand"] >= 2:
        data.inventory["sand"] -= 2
        data.inventory["glass"] += 1

def produce_machine_part():
    if data.inventory["iron_plate"] >= 1 and data.inventory["copper_ore"] >= 1:
        data.inventory["iron_plate"] -= 1
        data.inventory["copper_ore"] -= 1
        data.inventory["machine_part"] += 1

def produce_engine():
    if data.inventory["machine_part"] >= 2:
        data.inventory["machine_part"] -= 2
        data.inventory["engine"] += 1