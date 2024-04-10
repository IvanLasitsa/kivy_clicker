from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.switch import Switch
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.utils import platform
from kivy.uix.image import Image
from kivy.properties import NumericProperty
from kivy.animation import Animation
from random import randint
from kivy.clock import Clock

class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class GameScreen(Screen):
    points = NumericProperty(0)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
    def on_enter(self, *args):
        self.ids.fruit.new_fruit()
        return super().on_enter(*args)
    
class Shop(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
    
class Fruit(Image):
    is_anim = False
    hp = None
    fruit = None
    fruit_index = 0
    
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.parent.parent.parent.points += 1
            self.hp -= 1
            if self.hp <= 0:
                self.new_fruit()
            
            x = self.x
            y = self.y
            anim = Animation(x=x-5, y=y-5, duration=0.05) + Animation(x=x, y=y, duration=0.05)
            anim.start(self)
            self.is_anim = True
            anim.on_complete = lambda *args: setattr(self, 'is_anim', False)
        return super().on_touch_down(touch)
    

    
    
    def Auto_Clicker(self, switch):
        if switch.active:
            Clock.schedule_interval(self.auto_click, 0.2)  # Запускаємо автоклік кожні 2 секунди
        else:
             Clock.unschedule(self.auto_click)

    def auto_click(self, dt):
        self.parent.parent.parent.points += 1
        self.hp -= 1
        if self.hp <= 0:
            self.new_fruit()
        
        x = self.x
        y = self.y
        anim = Animation(x=x-5, y=y-5, duration=0.05) + Animation(x=x, y=y, duration=0.05)
        anim.start(self)
        self.is_anim = True
        anim.on_complete = lambda *args: setattr(self, 'is_anim', False)


    
    
    def new_fruit(self):
        self.fruit = self.LEVELS[randint(0, len(self.LEVELS))-1]
        self.source = self.FRUIT[self.fruit]['source']
        self.hp = self.FRUIT[self.fruit]['hp']
        
    LEVELS = ['Apple', 'Banana','Pear']

    FRUIT = {
        'Apple': {"source": 'assets/images/apple.png', 'hp': 10},
        'Banana': {"source": 'assets/images/banana.png', 'hp': 20},
        'Pear': {"source": 'assets/images/pear.png', 'hp': 30},
        
    }
    
class MainApp(App):
    
    
    
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name = 'menu'))
        sm.add_widget(GameScreen(name = 'game'))
        sm.add_widget(Shop(name = 'shop'))
        return sm 
    
        
    
    if platform != 'android':
        Window.size = (400,800)
        Window.left = +500
        Window.top = 100
        
app = MainApp().run()
app.run



