# from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivy.uix.anchorlayout import AnchorLayout
from kivymd.uix.textfield import MDTextField
from kivy.uix.label import Label
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id

Window.size = [480, 853]


from kivymd.theming import ThemeManager


class Container(BoxLayout):
    def artem(self):
        def write_message(sender, message):
            auto.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id()})

        auto = vk_api.VkApi(token=self.api.text)
        longpoll = VkLongPoll(auto)

        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                received_message = event.text
                sender = event.user_id
                if self.count.text == '1':

                    self.remove_widget(self.third)
                    self.remove_widget(self.four)
                    self.remove_widget(self.five)
                    self.remove_widget(self.six)

                    if received_message == self.first.text:
                        write_message(sender, self.second.text)
                elif self.count.text == '2':

                    self.remove_widget(self.five)
                    self.remove_widget(self.six)

                    if received_message == self.first.text:
                        write_message(sender, self.second.text)
                    elif received_message == self.third.text:
                        write_message(sender, self.four.text)
                elif self.count.text == '3':
                    if received_message == self.first.text:
                        write_message(sender, self.second.text)
                    elif received_message == self.third.text:
                        write_message(sender, self.four.text)
                    elif received_message == self.five.text:
                        write_message(sender, self.six.text)


class MyApp(MDApp):
    theme = ThemeManager()

    def build(self):
        self.theme.theme_style = 'Light'
        return Container()


if __name__ == '__main__':
    MyApp().run()

