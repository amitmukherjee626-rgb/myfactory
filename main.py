from kivy.app import App
from kivy.lang import Builder
from ui import MainUI

Builder.load_file("ui.kv")

class FactoryEmpireApp(App):
    def build(self):
        return MainUI()

FactoryEmpireApp().run()