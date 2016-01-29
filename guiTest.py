from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.config import Config
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.logger import Logger
from kivy.uix.progressbar import ProgressBar
import socket, os, subprocess, time, threading
import server, client  
from os.path import expanduser

Config.set('graphics', 'width', '300')
Config.set('graphics', 'height', '300')   

Builder.load_string("""
<HomeScreen>:
	canvas.before:
		Color:
			rgba: 42,150,168, 0.8
		Rectangle:
			pos: self.pos
			size: self.size	
    FloatLayout:	
		Image:
			pos_hint: {'x': .43, 'y': .6}
			size_hint: None, None
			source: './mir-r.png'
		Button:
			text: "Host"
			pos_hint: {'x': .30, 'y': .4}
			size_hint: .2, .1
			on_press: root.manager.current = 'host'
		Button:
			text: "Client"
			pos_hint: {'x': .51, 'y': .4}
			size_hint: .2, .1
			on_press: root.manager.current = 'client'

<HostScreen>:
	on_enter: root.hostCon()
	on_enter: root.load()
    FloatLayout:
        Button:
            text: "Back"
            pos_hint: {'x': .1, 'y': .8}
            size_hint: .2, .1
            on_press: root.load()
            on_press: root.manager.current = 'home'
        Label:
            text: root.getIP()
            pos_hint: {'x': .30, 'y': .5}
            size_hint: .4, .2
		ProgressBar:
			id: bar
			max: 1000
			value: 1000
        Label:
            text: "Hosting"
            pos_hint: {'x': .30, 'y': .3}
            size_hint: .4, .2

<ClientScreen>:
    FloatLayout:
        Button:
            text: "Back"
            pos_hint: {'x': .1, 'y': .8}
            size_hint: .2, .1
            on_press: root.manager.current = 'home'
        Button:
            text: "Connect"
            pos_hint: {'x': .2, 'y': .4}
            size_hint: .2, .1
            on_press: root.clientCon(ip.text)
        TextInput:
            id: ip
            pos_hint: {'x': .41, 'y': .4}
            size_hint: .4, .1
""") 

class HomeScreen(Screen):
	pass

class HostScreen(Screen):
	def hostCon(fk):
		output = []
		server.getOpenData(output)
		host = threading.Thread(target=server.runHost, args=[output])
		host.start()
	def load(self):
		screen = HostScreen()
		screen.ids['bar'].value = 1000
		pb = ProgressBar()
		pb.value = 1000
	def getIP(self):
		return server.getIP()
	pass

class ClientScreen(Screen):
	def clientCon(fk, ip):
		guest = threading.Thread(target=client.runClient, args=[ip])
		guest.start()
	pass 

sm = ScreenManager()
sm.add_widget(HomeScreen(name='home'))
sm.add_widget(HostScreen(name='host'))
sm.add_widget(ClientScreen(name='client'))

class MirrorApp(App):
    def build(self):
    	self.icon = './mir-r.png'
        return sm

if __name__ == '__main__':
    MirrorApp().run()