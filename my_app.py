#импорт необходимых элементов
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen

# класс для кнопки
class ScrButton(Button):
    def __init__(self, screen, direction='right', goal='main', **kwargs):
        super().__init__(**kwargs)
        self.screen = screen
        self.direction = direction
        self.goal = goal

    def on_press(self):
        self.screen.manager.transition.direction = self.direction
        self.screen.manager.current = self.goal



# создание 5-ти экранов
class Scr_1(Screen):
  def __init__(self, name='first'):
        super().__init__(name=name)
        btn_back = ScrButton(self, text='Назад')
        self.add_widget(btn_back)


class Scr_2(Screen):
  def __init__(self, name='second'):
        super().__init__(name=name)

class Scr_3(Screen):
  def __init__(self, name='third'):
        super().__init__(name=name)

class Scr_4(Screen):
  def __init__(self, name='fourth'):
        super().__init__(name=name)

class Main(Screen):
  def __init__(self, name='main'):
        super().__init__(name=name)
        box_h = BoxLayout()
        label = Label(text = 'Выбери экран')
        box_v = BoxLayout(orientation='vertical')
        btn_1 = ScrButton(self, goal = 'first', text = '1')
        btn_2 = ScrButton(self, goal = 'second', text = '2')
        btn_3 = ScrButton(self, goal = 'third', text = '3')
        btn_4 = ScrButton(self, goal = 'fourth', text = '4')
        box_v.add_widget(btn_1)
        box_v.add_widget(btn_2)
        box_v.add_widget(btn_3)
        box_v.add_widget(btn_4)
        box_h.add_widget(label)
        box_h.add_widget(box_v)
        self.add_widget(box_h)



# Создаем приложение
class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Main())
        sm.add_widget(Scr_1()) 
        sm.add_widget(Scr_2()) 
        sm.add_widget(Scr_3()) 
        sm.add_widget(Scr_4()) 
        return sm

app = MyApp()
app.run()
