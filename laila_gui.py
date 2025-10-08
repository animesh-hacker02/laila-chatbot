# laila_gui.py
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView


# --- Laila AI logic ---
def laila_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hi! I’m Laila, your AI friend 😊"
    elif "how are you" in user_input:
        return "I’m great! What about you?"
    elif "your name" in user_input:
        return "My name is Laila 💖, made by you!"
    elif "love" in user_input:
        return "Aww 🥰 love you too!"
    elif "bye" in user_input:
        return "Bye! Take care 🌸"
    else:
        return "Hmm... I didn’t understand that. Can you say it differently?"


# --- Kivy App Design ---
class ChatBotApp(App):
    def build(self):
        self.window = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Scrollable chat area
        self.scroll = ScrollView(size_hint=(1, 0.8))
        self.chat_label = Label(size_hint_y=None, text='', valign='top')
        self.chat_label.bind(texture_size=self._update_label_height)
        self.scroll.add_widget(self.chat_label)

        # Text input area
        self.user_input = TextInput(size_hint=(1, 0.1), multiline=False, hint_text="Type your message...")

        # Send button
        send_button = Button(text="Send", size_hint=(1, 0.1), on_press=self.send_message)

        # Add widgets
        self.window.add_widget(self.scroll)
        self.window.add_widget(self.user_input)
        self.window.add_widget(send_button)

        return self.window

    def _update_label_height(self, instance, value):
        self.chat_label.height = self.chat_label.texture_size[1]
        self.chat_label.text_size = (self.chat_label.width, None)

    def send_message(self, instance):
        user_text = self.user_input.text.strip()
        if user_text:
            self.chat_label.text += f"\nYou: {user_text}"
            reply = laila_response(user_text)
            self.chat_label.text += f"\nLaila: {reply}\n"
            self.user_input.text = ''
            self.scroll.scroll_y = 0  # auto-scroll to bottom


# --- Run App ---
if __name__ == "__main__":
    ChatBotApp().run()