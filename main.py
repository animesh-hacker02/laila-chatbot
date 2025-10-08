from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
import random

KV = '''
<ChatScreen>:
    orientation: 'vertical'
    ScrollView:
        id: scroll
        do_scroll_x: False
        do_scroll_y: True
        size_hint_y: 0.9
        GridLayout:
            id: chat_area
            cols: 1
            size_hint_y: None
            height: self.minimum_height
            padding: 10
            spacing: 10
    BoxLayout:
        size_hint_y: 0.1
        TextInput:
            id: user_input
            multiline: False
            hint_text: "Type your message..."
            on_text_validate: root.send_message()
        Button:
            text: "Send"
            size_hint_x: 0.3
            on_press: root.send_message()
'''

class ChatScreen(BoxLayout):
    def send_message(self):
        user_text = self.ids.user_input.text.strip()
        if not user_text:
            return
        self.add_message("You: " + user_text)
        reply = laila_response(user_text)
        self.add_message("Laila: " + reply)
        self.ids.user_input.text = ''

    def add_message(self, msg):
        from kivy.uix.label import Label
        lbl = Label(text=msg, size_hint_y=None)
        lbl.bind(texture_size=lambda inst, val: setattr(inst, 'height', val[1]))
        self.ids.chat_area.add_widget(lbl)

def laila_response(user_input):
    user_input = user_input.lower()
    responses = {
        "hi": ["Hey there! 😊", "Hello! How are you?", "Hi, I’m Laila 💕"],
        "how are you": ["I'm feeling great today!", "Doing awesome! You?"],
        "your name": ["My name is Laila, your AI friend 💖"],
        "bye": ["Goodbye! Take care 💫", "See you soon 😇"]
    }
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    return "Hmm... batao aur (tell me more) 💭"

class LailaApp(App):
    def build(self):
        Builder.load_string(KV)
        return ChatScreen()

if __name__ == "__main__":
    LailaApp().run()