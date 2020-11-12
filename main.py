"""
App project
"""
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.audio import SoundLoader
try:
	import pygame
	pygame.mixer.init()
except ModuleNotFoundError:
	pygame = None

def playm(sound):
	""" Crossplatform sound playing """
	if isinstance(sound,str):
		if pygame:
			s = pygame.mixer.Sound(sound)
		else:
			s = SoundLoader.load(sound)
		s.play()
		return s
	else:
		try:
			s.play()
			return s
		except AttributeError as a:
			return s

oakm = 'data/aud/Oak.wav'
oakm = playm(oakm)

try:
	import pygame
	pygame.mixer.init()
	sound = pygame.mixer.Sound('data/aud/106.wav')
	tjuta = 'data/aud/Oak.mp3'
	sound.play()
	tjuta = pygame.mixer.music.load(tjuta)
	#if tjuta is None:
	#	tjuta = pygame.mixer.music.load('data/aud/tjuta.wav')
except Exception as e:
	print(e)
	sound = SoundLoader.load('data/aud/106.wav')
	sound.play()
	tjuta = SoundLoader.load('data/aud/tjuta.wav')


"""

sound = SoundLoader.load('data/aud/106.wav')
if sound:
	print("Sound found at %s" % sound.source)
	print("Sound is %.3f seconds" % sound.length)
	sound.play()
import random

red = [1,0,0,1]
green = [0,1,0,1]
blue =  [0,0,1,1]
purple = [1,0,1,1]

class HBoxLayoutExample(App):
    def build(self):
        layout = BoxLayout(padding=10)
        colors = [red, green, blue, purple]

        for i in range(5):
            btn = Button(text="Button #%s" % (i+1),
                         background_color=random.choice(colors)
                         )

            layout.add_widget(btn)
        return layout

class Imgap(App):
    def build(self):
        img = Image(source='data/img/castle.png',
                    size_hint=(1, .5),
                    pos_hint={'center_x':.5, 'center_y':.5})
        label = Label(text='Hello from Kivy',
                      size_hint=(.5, .5),
                      pos_hint={'center_x': .5, 'center_y': .5})

        return img
"""
class MainApp(App):
    def build(self):
        self.icon = 'icon.ico'
        self.button = Button(text='CLICK HERE FOR FREE ROBUX !!!  NO SCAM !',
                        size_hint=(.5, .5),
                        background_color = [0,0,1,.5],
                        background_normal = "",
                        pos_hint={'center_x': .5, 'center_y': .5})
        self.button.bind(on_press=self.on_press_button)
        self.red = 0
        return self.button

    def on_press_button(self, instance):
        print('You pressed the button!')
        if not self.red:
            sound.play()
            self.button.background_color = [1,0,0,1]
            self.button.background_down = 'data/img/colors/green.png'
            self.button.text = "You have been TROLLED !!!!!!!!!!!XD"
            self.red += 1
        elif self.red:
            pygame.mixer.music.play()
            self.red = 0
            self.button.background_color = [0,0.8,0,1]
            self.button.background_down = 'data/img/colors/green.png'
            self.button.text = "Jo mama :O is so fat :D that she's yo DAD !!§XDDDDD"




if __name__ == '__main__':
    app = MainApp()
    app.run()

