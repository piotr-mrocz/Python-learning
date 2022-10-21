# flake8:  noqa: E226
from random import randint

from cymunk import Body, Circle, Space, Segment, Vec2d
from kivy.app import App
from kivy.base import EventLoop
from kivy.clock import Clock
from kivy.core.window import Keyboard, Window
from kivy.logger import Logger
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.widget import Widget
from kivy.vector import Vector

import defs

class GameScreenManager(ScreenManager):
    pass

class Baloon(Widget):
    pass


class KivyGame(Widget):

    def __init__(self, *a, **kwa):
        super().__init__(*a, **kwa)

        self.baloons = []
        self.widgets_with_bodies = []
        self.walls = []
        self.space = None

        self.app = App.get_running_app()
        Clock.schedule_once(self.init_widgets)

    def init_widgets(self, dt):
        w, h = self.size
        for _ in range(defs.num_baloons):
            baloon = Baloon(center=(randint(200, w - 200), randint(100, h - 200)))
            self.baloons.append(baloon)
            self.add_widget(baloon)

        self.app = App.get_running_app()

        Clock.schedule_interval(self.update, 1.0 / 30)
        EventLoop.window.bind(on_key_up=self.on_key_up)
        Window.bind(on_resize=self.on_resize)

        self.init_physics()

    def init_physics(self):
        self.space = Space()  # cała fizyka dzieje się w ramach obiektu Space()

        self.init_body(self.fred, defs.fred_collision_type)
        for b in self.baloons:
            self.init_body(b)

        self.create_walls()

        self.space.add_collision_handler(defs.goal_collision_type,
                                         defs.fred_collision_type,
                                         self.goal_reached)

    def create_walls(self):
        segments, R = self.wall_segments()
        for (v1, v2), goal in zip(segments, [False, False, False, True]):

            wall = Segment(self.space.static_body, v1, v2, R)
            wall.elasticity = defs.elasticity
            wall.friction = defs.wall_friction
            wall.collision_type = defs.goal_collision_type if goal else defs.default_collision_type

            self.space.add_static(wall)
            self.walls.append(wall)

    def init_body(self, widget, collision_type=defs.default_collision_type):
        """ initialize cymunk body for given widget as circle
            of radius=r
        """
        widget.body = Body(defs.mass, defs.moment)
        widget.body.position = widget.center
        self.widgets_with_bodies.append(widget)

        w, h = widget.size
        r = (w + h) / 4

        shape = Circle(widget.body, r)
        shape.elasticity = defs.elasticity
        shape.friction = defs.friction
        shape.collision_type = collision_type

        self.space.add(widget.body)
        self.space.add(shape)

    def update(self, dt):
        for b in self.baloons:
            b.body.apply_impulse((randint(-10, 10), randint(-10, 10)))

        self.space.step(1.0 / 30)

        for w in self.widgets_with_bodies:
            w.center = tuple(w.body.position)

    def on_resize(self, _win, w, h):
        if not self.walls:
            return
        Logger.debug("move walls with witgh w=%s h=%s", w, h)

        segments, __R = self.wall_segments()

        for (v1, v2), wall in zip(segments,
                                  self.walls):
            wall.a = v1
            wall.b = v2

        self.space.reindex_static()

    def on_key_up(self, __window, key, *__, **___):
        # code = Keyboard.keycode_to_string(None, key) # można tak, ale to brzydki hack
        dx, dy = 0, 0
        if key == Keyboard.keycodes['up']:
            dy = 1500
        elif key == Keyboard.keycodes['down']:
            dy = -1500
        elif key == Keyboard.keycodes['left']:
            dx = -1500
        elif key == Keyboard.keycodes['right']:
            dx = +1500

        self.fred.body.apply_impulse(Vector(dx, dy))

    def on_touch_up(self, touch):
        vdir = Vector(touch.pos) - self.fred.center  # wynik to Vector
        self.fred.body.apply_impulse(vdir * 5)

    def goal_reached(self, _space, _arbiter):
        self.app.sm.current = 'success'

    def wall_segments(self):
        w, h = self.size
        R = 200
        return [(Vec2d(-2 * R, -R), Vec2d(w + 2 * R, -R)),
                (Vec2d(-R, -2 * R), Vec2d(-R, h + 2 * R)),
                (Vec2d(-2 * R, h + R), Vec2d(w + 2 * R, h + R)),
                (Vec2d(w + R, h + 2 * R), Vec2d(w + R, -2 * R))], R


class KivyGameApp(App):
    def __init__(self, *a, **kw):
        super().__init__(*a, **kw)
        self.sm = None

    def build(self):
        self.sm = GameScreenManager()
        return self.sm

if __name__ == '__main__':
    KivyGameApp().run()
