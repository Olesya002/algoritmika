from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.config import Config
from ruffier import test
from instructions import txt_instruction, txt_test1, txt_test3, txt_sits
from kivy.properties import ObjectProperty, StringProperty, NumericProperty, BooleanProperty

Config.set('kivy','window_icon','logo.png')
age = 7
name = ""
p1, p2, p3 = 0, 0, 0


class InstrScr(Screen):
    '''Экран инструкции'''
    in_name = ObjectProperty(None)
    in_age = ObjectProperty(None)
    inst_text = StringProperty(txt_instruction)

    def next(self):
        global name, age
        name = self.in_name.text
        age = int(self.in_age.text)
        print(f"Имя: {name}, Возраст: {age}")
        
        self.manager.current = 'pulse1'


class PulseScr(Screen):
    '''Экран первого пульса'''
    in_p1 = ObjectProperty(None)
    inst_text = StringProperty(txt_test1)
    def next(self):
        global p1
        p1 = int(self.in_p1.text)
        print(f"Пульс: {p1}")
        self.manager.current = 'sits'


class CheckSits(Screen):
    '''Экран приседаний и таймера'''
    time_left = NumericProperty(45)
    timer_running = BooleanProperty(False)
    inst_text = StringProperty(txt_sits)

    def start_timer(self):
        if not self.timer_running:
            self.timer_running = True
            self.timer_event = Clock.schedule_interval(self.update_timer, 1)
        else:
            self.stop_timer()

    def stop_timer(self):
        self.timer_running = False
        if hasattr(self, 'timer_event'):
            Clock.unschedule(self.timer_event)

    def update_timer(self, dt):
        if self.time_left > 0:
            self.time_left -= 1
        else:
            self.stop_timer()

    def reset_timer(self):
        self.stop_timer()
        self.time_left = 45

    def next(self):
        self.stop_timer()
        self.manager.current = 'pulse2'


class PulseScr2(Screen):
    '''Экран второго пульса'''
    in_p2 = ObjectProperty(None)
    in_p3 = ObjectProperty(None)
    inst_text = StringProperty(txt_test3)
    def next(self):
        global p2, p3
        p2 = int(self.in_p2.text)
        p3 = int(self.in_p3.text)
        print(f"Пульс 2: {p2}, Пульс 3: {p3}")
        self.manager.current = 'result'


class Result(Screen):
    '''Экран с результатом'''
    def on_enter(self):
        self.ids.result_label.text = name + '\n' + str(test(p1, p2, p3, age))


class HeartCheckApp(App):
    def build(self):
        self.icon = 'logo.png'
        return Builder.load_file('heartcheck.kv')
    
app = HeartCheckApp()
app.run()