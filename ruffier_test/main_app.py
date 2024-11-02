from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from ruffier import test
from instructions import txt_instruction, txt_test1, txt_test2, txt_test3, txt_sits

res_1, res_2, res_3 = 0,0,0
age = 7
name = 'Ivan'
class InstrScr(Screen):
    def __init__(self, name='instructions'):
      super().__init__(name=name)
      box_v = BoxLayout(orientation='vertical')
      box_h1 = BoxLayout(orientation='horizontal', size_hint=(.5,.15), pos_hint={'center_x': 0.5, 'center_y':0.5})
      box_h2 = BoxLayout(orientation='horizontal', size_hint=(.5,.15), pos_hint={'center_x': 0.5, 'center_y':0.5})
      label_main = Label(text=txt_instruction, size_hint=(.7,1), pos_hint={'center_x': 0.5, 'center_y':0.5})
      self.input1 = TextInput(multiline=False, size_hint=(1,.7), pos_hint={'center_x': 0.5, 'center_y':0.5})
      self.input2 = TextInput(multiline=False, size_hint=(1,.7), pos_hint={'center_x': 0.5, 'center_y':0.5})
      label_1 = Label(text = 'Введите имя:')
      label_2 = Label(text = 'Введите возраст:')
      self.btn = Button(text='Начать', size_hint=(.3,.2), pos_hint={'center_x': 0.5, 'center_y':0.5})
      self.btn.on_press = self.next
      box_h1.add_widget(label_1)
      box_h1.add_widget(self.input1)
      box_h2.add_widget(label_2)
      box_h2.add_widget(self.input2)
      box_v.add_widget(label_main)
      box_v.add_widget(box_h1)
      box_v.add_widget(box_h2)
      box_v.add_widget(self.btn)
      self.add_widget(box_v)
    def next(self):
      global name, age
      name = self.input1.text
      age = int(self.input2.text)
      self.manager.current = 'first'

class Scr_1(Screen):
  def __init__(self, name='first'):
        super().__init__(name=name)
        box_v = BoxLayout(orientation='vertical')
        box_h1 = BoxLayout(orientation='horizontal', size_hint=(.5,.15), pos_hint={'center_x': 0.5, 'center_y':0.5})
        label_main = Label(text=txt_test1, size_hint=(.7,1), pos_hint={'center_x': 0.5, 'center_y':0.5})
        self.input_1 = TextInput(multiline=False, size_hint=(1,.7), pos_hint={'center_x': 0.5, 'center_y':0.5})
        label_1 = Label(text = 'Введите результат:')
        self.btn = Button(text='Продолжить', size_hint=(.3,.2), pos_hint={'center_x': 0.5, 'center_y':0.5})
        self.btn.on_press = self.next
        box_h1.add_widget(label_1)
        box_h1.add_widget(self.input_1)
        box_v.add_widget(label_main)
        box_v.add_widget(box_h1)
        box_v.add_widget(self.btn)
        self.add_widget(box_v)
  def next(self):
      global res_1
      res_1 = int(self.input_1.text)
      self.manager.current = 'second'

class Scr_2(Screen):
  def __init__(self, name='second'):
        super().__init__(name=name)
        box_v = BoxLayout(orientation='vertical')
        label_main = Label(text=txt_sits, size_hint=(.7,1), pos_hint={'center_x': 0.5, 'center_y':0.5})
        self.btn = Button(text='Продолжить', size_hint=(.3,.2), pos_hint={'center_x': 0.5, 'center_y':0.5})
        self.btn.on_press = self.next
        box_v.add_widget(label_main)
        box_v.add_widget(self.btn)
        self.add_widget(box_v)
  def next(self):
      self.manager.current = 'third'

class Scr_3(Screen):
  def __init__(self, name='third'):
        super().__init__(name=name)
        box_v = BoxLayout(orientation='vertical')
        box_h1 = BoxLayout(orientation='horizontal', size_hint=(.5,.15), pos_hint={'center_x': 0.5, 'center_y':0.5})
        box_h2 = BoxLayout(orientation='horizontal', size_hint=(.5,.15), pos_hint={'center_x': 0.5, 'center_y':0.5})
        label_main = Label(text=txt_test3, size_hint=(.7,1), pos_hint={'center_x': 0.5, 'center_y':0.5})
        self.input_1 = TextInput(multiline=False, size_hint=(1,.7), pos_hint={'center_x': 0.5, 'center_y':0.5})
        self.input_2 = TextInput(multiline=False, size_hint=(1,.7), pos_hint={'center_x': 0.5, 'center_y':0.5})
        label_1 = Label(text = 'Результат:')
        label_2 = Label(text = 'Результат после отдыха:')
        self.btn = Button(text='Завершить', size_hint=(.3,.2), pos_hint={'center_x': 0.5, 'center_y':0.5})
        self.btn.on_press = self.next
        box_h1.add_widget(label_1)
        box_h1.add_widget(self.input_1)
        box_h2.add_widget(label_2)
        box_h2.add_widget(self.input_2)
        box_v.add_widget(label_main)
        box_v.add_widget(box_h1)
        box_v.add_widget(box_h2)
        box_v.add_widget(self.btn)
        self.add_widget(box_v)
  def next(self):
      global res_2
      global res_3
      res_2 = int(self.input_1.text)
      res_3 = int(self.input_2.text)
      self.manager.current = 'result'


class Result(Screen):
  def __init__(self, name='result'):
        super().__init__(name=name)
        self.label_main = Label(text='Instructions', size_hint=(.7,1), pos_hint={'center_x': 0.5, 'center_y':0.5})
        self.add_widget(self.label_main)
        self.on_enter = self.before
  def before(self):
        self.label_main.text = f'{name}\n' + test(res_1, res_2, res_3, age)
        

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(InstrScr())
        sm.add_widget(Scr_1()) 
        sm.add_widget(Scr_2()) 
        sm.add_widget(Scr_3()) 
        sm.add_widget(Result()) 
        return sm

app = MyApp()
app.run()
