import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
#from kivy.uix.textinput import TextInput
#from kivy.uix.filechooser import FileChooserIconView
from kivy.garden.filebrowser import FileBrowser
from kivy.utils import platform
from kivy.uix.button import Button
kivy.require('1.11.1')


class ControlPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2

        # Widget 1: Label
        self.add_widget(Label(text='Roster Path:'))

        # Widget 2: Text Field - roster
        self.roster = FileBrowser()
        self.add_widget(self.roster)

        # Widget 3: Label
        self.add_widget(Label(text='Schedule:'))

        # Widget 4: Text Field - schedule
        self.port = FileBrowser()
        self.add_widget(self.port)

        self.process = Button(text='Process')
        self.add_widget(self.process)

class MyApp(App):
    def build(self):
        return ControlPage()

if __name__ == '__main__':
    MyApp().run()
