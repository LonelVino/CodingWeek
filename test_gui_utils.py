import pygame as pg
from gui_utils import Button,InputBox

RED = (255, 0, 0)

def test_all():
    pg.init()
    screen = pg.display.set_mode((640, 480))

    input_box1 = InputBox(0.5, 0.2, 0.5, 0.1, screen)
    
    yes_button = Button('Yes',RED,screen,x_percent= 1/4, y_percent= 3/4)
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                raise SystemExit
            if pg.mouse.get_pressed()[0]:
                if yes_button.check_click(pg.mouse.get_pos()):
                    print(input_box1.text)
                    break

            input_box1.handle_event(event)
            input_box1.update()
        
        input_box1.draw(screen)
        yes_button.display()
        pg.display.flip()


if __name__ == '__main__':
    test_all()