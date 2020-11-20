import pygame as pg
import threading

SCREEN_MAX_WIDTH = 800
SCREEN_MAX_HEIGHT = 600
SCREEN_CONFIG_WIDTH = 200

pg.init()
FONT = pg.font.Font(None, 32)
INPUT_LABEL_FONT = pg.font.SysFont("Algerian", 16)
COLOR_INACTIVE = pg.Color('lightskyblue3')
COLOR_ACTIVE = pg.Color('dodgerblue2')


class BFControlId(object):
    _instance_lock = threading.Lock()

    def __init__(self):
        self.id = 1

    @classmethod
    def instance(cls, *args, **kwargs):
        if not hasattr(BFControlId, "_instance"):
            BFControlId._instance = BFControlId(*args, **kwargs)
        return BFControlId._instance

    def get_new_id(self):
        self.id += 1
        return self.id


CLICK_EFFECT_TIME = 100


class Button(object):
    def __init__(self, text, color, screen, x_percent=None, y_percent=None, click=None, **kwargs):
        self.surface = FONT.render(text, True, color)
        self.bg_color = (225, 225, 225)
        self.color = color
        self.WIDTH = self.surface.get_width()
        self.HEIGHT = self.surface.get_height()
        self.screen = screen
        self.in_click = False
        self.click_loss_time = 0
        self.click_event_id = -1
        self.ctl_id = BFControlId().instance().get_new_id()
        self._click = click
        self.is_hover = False

        if 'centered_x' in kwargs and kwargs['centered_x']:
            self.x = SCREEN_MAX_WIDTH // 2 - self.WIDTH // 2
            self.__x_percent = 0.5
        else:
            self.x = max(
                int(SCREEN_MAX_WIDTH * x_percent - self.WIDTH // 2), 0)
            self.__x_percent = x_percent

        if 'centered_y' in kwargs and kwargs['cenntered_y']:
            self.y = SCREEN_MAX_HEIGHT // 2 - self.HEIGHT // 2
            self.__y_percent = 0.5
        else:
            self.y = max(
                int(SCREEN_MAX_HEIGHT * y_percent - self.HEIGHT // 2), 0)
            self.__y_percent = y_percent

    @property
    def click(self): return self._click

    @click.setter
    def click(self, value): self._click = value

    def update(self, event):
        if self.in_click and event.type == self.click_event_id:
            if self._click:
                self._click(self)
            self.click_event_id = -1
            return
        if self.check_click(pg.mouse.get_pos()):
            self.is_hover = True
            if event.type == pg.MOUSEBUTTONDOWN:
                pressed_array = pg.mouse.get_pressed()
                if pressed_array[0]:
                    self.in_click = True
                    self.click_loss_time = pg.time.get_ticks() + CLICK_EFFECT_TIME
                    self.click_event_id = pg.USEREVENT+self.ctl_id
                    pg.time.set_timer(self.click_event_id,
                                      CLICK_EFFECT_TIME-10)
        else:
            self.is_hover = False

    def display(self):
        self.screen.blit(self.surface, (self.x, self.y))

    def check_click(self, position):
        x_match = position[0] > self.x and position[0] < self.x + self.WIDTH
        y_match = position[1] > self.y and position[1] < self.y + self.HEIGHT

        if x_match and y_match:
            return True
        else:
            return False

    def changetext(self, text, color=None):
        if color is None:
            self.surface = FONT.render(text, True, self.color)
        else:
            self.surface = FONT.render(text, True, color)

        self.WIDTH = self.surface.get_width()
        self.HEIGHT = self.surface.get_height()

        self.x = max(
            int(SCREEN_MAX_WIDTH * self.__x_percent - self.WIDTH // 2), 0)
        self.y = max(
            int(SCREEN_MAX_HEIGHT * self.__y_percent - self.HEIGHT // 2), 0)


class Label(object):
    def __init__(self, text, color, screen, x_percent=None, y_percent=None, FONT=FONT, **kwargs):
        self.surface = FONT.render(text, True, color)
        self.color = color
        self.WIDTH = self.surface.get_width()
        self.HEIGHT = self.surface.get_height()
        self.screen = screen

        if 'centered_x' in kwargs and kwargs['centered_x']:
            self.x = SCREEN_MAX_WIDTH // 2 - self.WIDTH // 2
            self.__x_percent = 0.5
        else:
            self.x = max(
                int(SCREEN_MAX_WIDTH * x_percent - self.WIDTH // 2), 0)
            self.__x_percent = x_percent

        if 'centered_y' in kwargs and kwargs['centered_y']:
            self.y = SCREEN_MAX_HEIGHT // 2 - self.HEIGHT // 2
            self.__y_percent = 0.5
        else:
            self.y = max(
                int(SCREEN_MAX_HEIGHT * y_percent - self.HEIGHT // 2), 0)
            self.__y_percent = y_percent

    def display(self):
        self.screen.blit(self.surface, (self.x, self.y))

    def changetext(self, text, color=None):
        if color is None:
            self.surface = FONT.render(text, True, self.color)
        else:
            self.surface = FONT.render(text, True, color)

        self.WIDTH = self.surface.get_width()
        self.HEIGHT = self.surface.get_height()

        self.x = max(
            int(SCREEN_MAX_WIDTH * self.__x_percent - self.WIDTH // 2), 0)
        self.y = max(
            int(SCREEN_MAX_HEIGHT * self.__y_percent - self.HEIGHT // 2), 0)


class InputBox(object):

    def __init__(self, x_percent, y_percent, w_percent, h_percent, screen, key='', text='', callback=None):
        w = int(w_percent * SCREEN_MAX_WIDTH)
        h = int(h_percent * SCREEN_MAX_HEIGHT)
        x = max(int(SCREEN_MAX_WIDTH * x_percent - w // 2), 0)
        y = max(int(SCREEN_MAX_HEIGHT * y_percent - h // 2), 0)
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.txt_color = pg.Color('gray12')
        self.text = text
        self.key = key
        self.txt_surface = FONT.render(text, True, self.txt_color)
        self.active = False
        self.callback = callback
        self.screen = screen
        self.state = 0   # the initial status equal to 0, input status equal to 1

    def get_key(self): return self.key
    def get_value(self): return self.text

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.txt_color)
        self.update()

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the rect.
        pg.draw.rect(screen, self.color, self.rect, 0)
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))


class CellButton(object):

    def __init__(self, x, y, w, h, color, text=''):
        self.__x = x
        self.__y = y
        self.__w = w
        self.__h = h
        self.color = color
        self.__text = text
        self.__rect = pg.Rect(x, y, w, h)
        self.__NEW_FONT = pg.font.Font(None, min(w, h))
        self.__txt_surface = self.__NEW_FONT.render(
            text, True, pg.Color('gray12'))

    def display(self, screen):
        pg.draw.rect(screen, self.color, self.__rect, 0)
        screen.blit(self.__txt_surface, (self.__rect.x+5, self.__rect.y+5))

    def check_click(self, position):
        x_match = position[0] > self.__x and position[0] < self.__x + self.__w
        y_match = position[1] > self.__y and position[1] < self.__y + self.__h

        if x_match and y_match:
            return True
        else:
            return False

    def change_text(self, text):
        self.__text = text
        self.__txt_surface = self.__NEW_FONT.render(
            text, True, pg.Color('gray12'))


class Rectangle(object):

    def __init__(self, screen, x_percent=None, y_percent=None, w_percent=None, h_percent=None, color=None):
        surface = pg.Surface((1, 1))
        w = int(w_percent * SCREEN_MAX_WIDTH)
        h = int(h_percent * SCREEN_MAX_HEIGHT)
        x = max(int(SCREEN_MAX_WIDTH * x_percent - w // 2), 0)
        y = max(int(SCREEN_MAX_HEIGHT * y_percent - h // 2), 0)
        self.screen = screen
        self.color = color
        self.__surface = surface
        self.__rect = pg.Rect(x, y, w, h)

    def display(self):
        pg.draw.rect(self.screen, self.color, self.__rect, 0)
        self.screen.blit(self.__surface, (self.__rect.x, self.__rect.y))
