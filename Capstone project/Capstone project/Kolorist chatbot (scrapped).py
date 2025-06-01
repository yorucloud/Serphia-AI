from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout

class HairCareAssistant(BoxLayout):
    def __init__(self, **kwargs):
        super(HairCareAssistant, self).__init__(orientation='vertical', spacing=10, padding=10, **kwargs)

        # Top Section
        self.add_widget(Label(text="StyleCuts Salon Assistant\nI'm here to help you with appointments, services, and questions", 
                               size_hint_y=None, height=80, halign="center", valign="middle"))
        
        # Quick Action Buttons
        action_buttons = BoxLayout(size_hint_y=None, height=50, spacing=10)
        action_buttons.add_widget(Button(text="Book Appointment"))
        action_buttons.add_widget(Button(text="Our Services"))
        self.add_widget(action_buttons)

        # Chat Section
        self.add_widget(Label(text="How can I assist you today?", size_hint_y=None, height=40))

        chat_options = GridLayout(cols=2, size_hint_y=None, height=120, spacing=10)
        chat_options.add_widget(Button(text="Book an appointment"))
        chat_options.add_widget(Button(text="Check service prices"))
        chat_options.add_widget(Button(text="Ask about treatments"))
        chat_options.add_widget(Button(text="Contact stylist"))
        self.add_widget(chat_options)

        # Suggested Questions
        suggested_scroll = ScrollView(size_hint=(1, None), size=(self.width, 80))
        suggested_layout = GridLayout(cols=2, size_hint_y=None, height=160, spacing=10)

        suggested_layout.add_widget(Button(text="What services do you offer?", size_hint_y=None, height=40))
        suggested_layout.add_widget(Button(text="How long is the wait time?", size_hint_y=None, height=40))
        suggested_layout.add_widget(Button(text="Do you take walk-ins?", size_hint_y=None, height=40))
        suggested_layout.add_widget(Button(text="Cancellation policy", size_hint_y=None, height=40))

        suggested_scroll.add_widget(suggested_layout)
        self.add_widget(suggested_scroll)

        # Text Input Section
        bottom_layout = BoxLayout(size_hint_y=None, height=50, spacing=10)
        bottom_layout.add_widget(TextInput(hint_text="Type your message..."))
        bottom_layout.add_widget(Button(text="Send", size_hint_x=None, width=80))
        self.add_widget(bottom_layout)

class HairCareApp(App):
    def build(self):
        return HairCareAssistant()

if __name__ == '__main__':
    HairCareApp().run()