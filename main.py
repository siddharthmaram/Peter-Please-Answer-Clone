from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
import re
from random import choice
from voice import voice
# from kivy.config import Config
# import os

# Config.set('graphics', 'width', '600')
# Config.set('graphics', 'height', '800')

ans = ""
unfilled_implore = ["Why are you wasting my time?", "You need more practice", "My time is valuable you know",
                    "Don't you know how to ask nicely?", "What if I implored with you like that?", "Please do not play with me"]
no_ans = ["Your energy is questionable", "I think you need to calm down first", "Prove that I can trust you with this info",
          "I might not be the right fit for you", "Let someone else try to ask the question", "You are not getting into my database like that",
          "I'm sorry but something feels off about you", "You need more practice", "First answer how are you feeling today?",
          "Please do not play with me"]


class HiddenInput(TextInput):
    txt = "Peter please answer the following question" + " " * 10 ** 5
    hidden = False

    def insert_text(self, substring, from_undo=False):
        global ans
        if len(self.text) == 0:
            self.hidden = False

        if len(ans) != len(self.text):
            ans = ans[:len(self.text)]

        if substring == "/" and ans.count("/") < 2:
            s = self.txt[len(self.text)]
            self.hidden = not self.hidden
        elif self.hidden:
            s = self.txt[len(self.text)] if len(substring) == 1 else ""
        else:
            s = substring

        ans += substring

        # print(ans)
        return super(HiddenInput, self).insert_text(s, from_undo=from_undo)


class MainLayout(BoxLayout):
    def ask_peter(self):
        a = self.ids["dis"]
        q = self.ids["ques"]
        h = self.ids["hidden"]
        if ans.count("/") == 2:
            if q.in_text.text:
                if h.sol.text.strip() == "Peter please answer" or h.sol.text.strip() == "Peter please answer the following question":
                    t = re.findall("/(.+)/", ans)[0]
                    a.text = t
                    voice(t)
                else:
                    t = choice(unfilled_implore)
                    a.text = t
                    voice(t)
            else:
                a.text = "Please enter a valid question"
                voice("Please enter a valid question")
        else:
            t = choice(no_ans)
            a.text = t
            voice(t)


class HiddenLabelText(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "horizontal"
        self.add_widget(Label(text="Implore:", size_hint=(0.4, 1), font_name="OdibeeSans-Regular.ttf", font_size="20dp"))
        answer_text = HiddenInput()
        answer_text.font_size = "18dp"
        self.ids["answer"] = answer_text
        self.add_widget(answer_text)


class KivyApp(App):
    pass


KivyApp().run()
