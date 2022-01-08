from kivymd.app import MDApp
from kivymd.theming import ThemeManager
from kivymd.uix import button
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import OneLineAvatarListItem
from kivy.uix.popup import Popup
from kivy.properties import StringProperty 
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivy.core.window import Window
from kivy.lang import Builder
from os import mkdir, chdir, startfile, getcwd, listdir, remove
from datetime import date, datetime



code='''
ScreenManager:
	OptionScreen:
    RMode1Screen:
    RMode2Screen:
    AppScreen:
    DataScreen:
    AboutScreen:

<OptionScreen>:
	
	name:'opt'
	
	MDNavigationLayout:

		ScreenManager:
			Screen:

                MDFloatLayout:
                    cols:1

                    MDBoxLayout:
                        orientation:'vertical'
                        spacing: 50

                    MDRectangleFlatButton:
                        text: "Normal"
                        pos_hint: {'center_x':0.4, 'center_y':0.5}
                        on_release: 
                            app.root.current = 'rmode1'
                            root.manager.transition.direction = 'up'

                    MDRectangleFlatButton:
                        text: "Parent"
                        pos_hint: {'center_x':0.6, 'center_y':0.5}
                        on_release: 
                            app.root.current = 'rmode2'
                            root.manager.transition.direction = 'up'
                

<RMode1Screen>:

    name:'rmode1'
    nm:nm
    scrt:scrt

    MDNavigationLayout:

        ScreenManager:
			Screen:

                MDGridLayout:
                    cols:1

                    MDToolbar:
                        title: "Welcome to Registration"
                        elevation: 10

                    MDBoxLayout:
                        orientation: 'vertical'

                        Widget:
                            
                        MDTextField:
                            id: nm
                            hint_text:"Enter Your Full Name"
                            size_hint: (0.8,0)
                            pos_hint:{'center_x':0.5}
                            multiline:False

                        MDTextField:
                            id: scrt
                            hint_text:"Enter Your Prefered Screen Time (Usually 3 hours)"
                            size_hint: (0.8,0)
                            pos_hint:{'center_x':0.5}
                            multiline:False

                    MDBoxLayout:
                        orientation: 'vertical'
                        padding: 15
                        spacing: 15

                        MDRectangleFlatButton:
                            text: "Register"
                            pos_hint:{'center_x':0.5}
                            on_release: root.reg()

                        MDRectangleFlatButton:
                            text: "Back"
                            pos_hint:{'center_x':0.5}
                            on_release:
                                app.root.current = 'opt'
                                root.manager.transition.direction = 'down'

                        Widget:

<RMode2Screen>:

    name:'rmode2'

    MDNavigationLayout:

        ScreenManager:
			Screen:

                MDGridLayout:
                    cols:1

                    MDToolbar:
                        title: "Welcome to Registration"
                        elevation: 10

                    MDBoxLayout:
                        orientation: 'vertical'

                        Widget:
                            
                        MDTextField:
                            id: nm
                            hint_text:"Enter Full Name"
                            size_hint: (0.8,0)
                            pos_hint:{'center_x':0.5}
                            multiline:False

                        MDTextField:
                            id: email
                            hint_text:"Enter Your Email ID"
                            size_hint: (0.8,0)
                            pos_hint:{'center_x':0.5}
                            multiline:False

                        MDTextField:
                            id: scrt
                            hint_text:"Enter Your Prefered Screen Time (Usually 3 hours)"
                            size_hint: (0.8,0)
                            pos_hint:{'center_x':0.5}
                            multiline:False

                    MDBoxLayout:
                        orientation: 'vertical'
                        padding: 15
                        spacing: 15

                        MDRectangleFlatButton:
                            text: "Register"
                            pos_hint:{'center_x':0.5}
                            on_release: root.reg()

                        MDRectangleFlatButton:
                            text: "Back"
                            pos_hint:{'center_x':0.5}
                            on_release:
                                app.root.current = 'opt'
                                root.manager.transition.direction = 'down'

                        Widget:
'''

class OptionScreen(Screen):
    pass
            
class RMode1Screen(Screen):
    
    def reg(self):
        pass

class RMode2Screen(Screen):
    
    def reg(self):
        pass

class AppScreen(Screen):
    pass

class DataScreen(Screen):
    pass

class AboutScreen(Screen):
    pass
            
sm = ScreenManager()
sm.add_widget(OptionScreen(name = 'opt'))
sm.add_widget(RMode1Screen(name = 'rmode1'))
sm.add_widget(RMode2Screen(name = 'rmode2'))
sm.add_widget(AppScreen(name = 'app'))
sm.add_widget(DataScreen(name = 'data'))
sm.add_widget(AboutScreen(name = 'about'))


class HonestClockApp(MDApp):

	def build(self):
		self.theme_cls = ThemeManager()
		#self.icon="icon.png"
		self.theme_cls.primary_palette='Indigo'
		self.theme_cls.primary_hue='900'
		self.screen=Builder.load_string(code)
		return self.screen

HonestClockApp().run()