import kivy.app
import kivy.uix.button

class TestApp(App):
    def build(self):
        return Button(text='Hello World')

TestApp().run()