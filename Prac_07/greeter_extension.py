


from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty

class GreeterExtension(App):
    status_text = StringProperty()

    def build(self):
        self.title = 'Greeter App'
        self.root = Builder.load_file('greeter_extension.kv')
        return self.root

    def greet(self):
        self.root.ids.name_output.text = "Hello" + self.root.ids.name_input.text

    def clear_all(self):
        self.root.ids.name_output.text = ""
        self.root.ids.name_input.text = ""

GreeterExtension().run()