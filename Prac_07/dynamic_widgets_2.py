
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty


class DynWidgetsApp(App):
    status_text = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ['Hung', 'John', 'Jean', 'Paris Hilton', 'London Tipton']

    def build(self):
        self.title = 'This is Dynamic Widgets'
        self.root = Builder.load_file('dynamic_widgets_2.kv')
        self.add_widgets()
        return self.root

    def add_widgets(self):
        for name in self.names:
            temp_button = Button(text=name, id=name)
            temp_button.bind(on_release=self.press_entry)
            self.root.ids.main_box.add_widget(temp_button)

    def press_entry(self, instance):
        name = instance.id
        self.status_text = "{}'s name is {}".format(name, name)

    def clear_all(self):
        self.root.ids.main_box.clear_widgets()


DynWidgetsApp().run()