import random
import kivy
import sys


from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivy.uix.textinput import TextInput
from kivy.graphics import Color
from kivy.properties import NumericProperty
from kivy.properties import ObjectProperty
from kivy.uix.image import Image
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
from specialbuttons import ImageButton
from kivy.uix.button import ButtonBehavior
from kivy.graphics import Color
from kivy.graphics import RoundedRectangle
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.factory import Factory

class MainMenu(Screen):
	pass

class DiceRoller(Screen):

	diceType = ObjectProperty()
	diceNumber = ObjectProperty()


	def rolldice(self):
		Total = 0
		print(F"{self.diceNumber.text}D{self.diceType.text}")


		for x in range(int(self.diceNumber.text)):
			x = x + 1

			ActualDie = random.randint(1, int(self.diceType.text))
			Total = Total + ActualDie

			print(ActualDie)
		print("Total:", Total)

		self.diceType.text = ""
		self.diceNumber.text = ""
		show_popup()

class EncounterTable(Screen):
	pass

class settings(Screen):
	pass

class WindowManager(ScreenManager):
	pass

class smoothButton(Button):
	pass

class MyPopup(FloatLayout):
	pass

def show_popup():
	show = MyPopup()

	popupWindow = Popup(title="Dice rolled", content=show, size_hint=(None,None),size=(400,400))

	popupWindow.open()

kv = Builder.load_file("UI.kv")

class MyMainApp(App):
	def build(self):
		return Builder.load_file("UI.kv")

if __name__ == "__main__":
	MyMainApp().run()