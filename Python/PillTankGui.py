import kivy
import os
kivy.require('2.0.0')

from os import system

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout

from kivy.lang import Builder

from kivy.config import Config


# Setting app size (Pi Touchscreen uses 800x480)
Config.set('graphics', 'width', '1280')
Config.set('graphics', 'height', '720')

class DetectButton(Button):
    def build(self):
        MyApp.build.layout.add_widget(DetectButton)
    #     self.bind(on_press = self.callback)
    def callback(self):
        os.system('sudo ../vectorizedUnlooped/vectorizedSobel')

class HistoryButton(Button):
    def build(self):
        MyApp.build.layout.add_widget(HistoryButton)

class ProfileButton(Button):
    def build(self):
        MyApp.build.layout.add_widget(ProfileButton)

class SettingsButton(Button):
    def build(self):
        MyApp.build.layout.add_widget(SettingsButton)
         

class MyApp(App):

    # DetectButton = Builder.load_file('DetectButton.kv')
    App.orientation = 'horizontal'
    def build(self):
        layout = GridLayout(cols = 2)

        self.DetectButton = Builder.load_file('DetectButton.kv')
        self.HistoryButton = Builder.load_file('HistoryButton.kv')
        self.ProfileButton = Builder.load_file('ProfileButton.kv')
        self.SettingsButton = Builder.load_file('SettingsButton.kv')

        layout.add_widget(self.DetectButton)
        layout.add_widget(self.HistoryButton)
        layout.add_widget(self.ProfileButton)
        layout.add_widget(self.SettingsButton)

        # self.DetectButton.bind(on_press = os.system('sudo ./vectorizedUnlooped/vectorizedSobel'))

        return layout

    # def pressed(self):
    #     return None
        

if __name__ == '__main__':
    MyApp().run()
