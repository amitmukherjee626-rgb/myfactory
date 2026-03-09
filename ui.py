from kivy.uix.screenmanager import ScreenManager, Screen
import data
import crafting
import save_system


class ShopScreen(Screen):

    def update_money(self):
        if "money_label" in self.ids:
            self.ids.money_label.text = "₹ " + str(data.money)

    def on_enter(self):
        self.update_money()

    def buy(self,item,cost):

        if data.money >= cost:

            data.money -= cost
            data.inventory[item] += 1

            save_system.save_game(data.money,data.inventory)

            self.update_money()


class ProductionScreen(Screen):

    def plank(self):
        crafting.produce_plank()
        save_system.save_game(data.money,data.inventory)

    def iron_plate(self):
        crafting.produce_iron_plate()
        save_system.save_game(data.money,data.inventory)

    def glass(self):
        crafting.produce_glass()
        save_system.save_game(data.money,data.inventory)

    def machine_part(self):
        crafting.produce_machine_part()
        save_system.save_game(data.money,data.inventory)

    def engine(self):
        crafting.produce_engine()
        save_system.save_game(data.money,data.inventory)


class InventoryScreen(Screen):

    def update_inventory(self):

        inv = data.inventory

        text = ""

        text += "Wood : " + str(inv["wood"]) + "\n"
        text += "Iron Ore : " + str(inv["iron_ore"]) + "\n"
        text += "Copper Ore : " + str(inv["copper_ore"]) + "\n"
        text += "Stone : " + str(inv["stone"]) + "\n"
        text += "Sand : " + str(inv["sand"]) + "\n"
        text += "Coal : " + str(inv["coal"]) + "\n"
        text += "Oil : " + str(inv["oil"]) + "\n"
        text += "Water : " + str(inv["water"]) + "\n\n"

        text += "Plank : " + str(inv["plank"]) + "\n"
        text += "Iron Plate : " + str(inv["iron_plate"]) + "\n"
        text += "Glass : " + str(inv["glass"]) + "\n"
        text += "Machine Part : " + str(inv["machine_part"]) + "\n"
        text += "Engine : " + str(inv["engine"])

        self.ids.inventory_label.text = text


    def on_enter(self):
        self.update_inventory()


    def sell(self,item):

        if data.inventory[item] > 0:

            data.inventory[item] -= 1
            data.money += data.sell_prices[item]

            save_system.save_game(data.money,data.inventory)

            self.update_inventory()


class MainUI(ScreenManager):
    pass