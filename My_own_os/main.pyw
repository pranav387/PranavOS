import os
import sys
import pygame as pg
from tkinter import *
import math
import random as rd
from pygame.display import set_mode
import pygame_widgets as pw
sys.path.append('C:\\Users\\prana\\Desktop\\vscodeprojects')
import My_own_os.bapps as apps

# my os version of exe(.mos)
print(apps.reg_apps[0])
pg.init()
screen = pg.display.set_mode((800,600),pg.RESIZABLE)

pg.display.set_caption('Pranav OS')
run = True
# button = pw.Button(
#             screen, 100, 100, 300, 150, text='Hello',
#             fontSize=50, margin=20,
#             inactiveColour=(255, 0, 0),
#             pressedColour=(0, 255, 0), radius=20,
#             onClick=lambda: print('Click')
#          )
example_app = False


def open_terminal():
    os.system('start '+'C:\\Users\\prana\\Desktop\\vscodeprojects\\My_own_os\\terminal.py')

def run_example():
    global example_app
    example_app = True
    # app = apps.Example(screen)
    return # app.rect

def close_example():
    global example_app
    example_app = False
    return 

def close_all():
    global example_app
    example_app = False
    return 


tskmgr_open_ = False


def open_tskmgr_function():
    global tskmgr_open_
    tskmgr_open_ = True


app_tm = apps.TaskMgr(win=screen,tskmgr_open=open_tskmgr_function)

# def run_tskmgr():
#     global app_tm
#     global taskmgr_open


button_open_example = pw.Button(win=screen,x=10,y=525,height=60,width=60,text='example',fontSize=20,margin=20,hoverColour=(68,172,249),
                inactiveColour=(247,207,69),pressedColour=(68,172,249),radius=20,onClick=run_example) 

button_close_example = pw.Button(win=screen,x=90,y=525,height=60,width=60,text='close all',fontSize=20,margin=20,hoverColour=(68,172,249),
                inactiveColour=(247,207,69),pressedColour=(68,172,249),radius=20,onClick=close_example)

close_app_example = apps.Example(screen).button_close = pw.Button(win=screen,x=205,y=35,height=20,width=20,text='X',fontSize=20,margin=20,hoverColour=(68,172,249),
        inactiveColour=(247,207,69),pressedColour=(68,172,249),radius=20,onClick=close_example)

button_open_terminal = pw.Button(win=screen,x=170,y=525,height=60,width=60,text='terminal',fontSize=20,margin=20,hoverColour=(68,172,249),
                inactiveColour=(247,207,69),pressedColour=(68,172,249),radius=20,onClick=open_terminal)

button_exit_app = pw.Button(win=screen,x=250,y=525,height=60,width=60,text='exit',fontSize=40,margin=20,hoverColour=(68,172,249),
                inactiveColour=(247,207,69),pressedColour=(68,172,249),radius=20,onClick=lambda: exit())

button_open_taskmgr = pw.Button(win=screen,x=320,y=525,height=60,width=60,text='taskmgr',fontSize=20,margin=20,hoverColour=(68,172,249),
                inactiveColour=(247,207,69),pressedColour=(68,172,249),radius=20,onClick=open_tskmgr_function)


app_slider = pw.Slider(screen, 30, 475, 740, 20, min=0, max=99, step=10)
app_slider.setValue(0)

while run:
    # print()
    screen.fill((96,248,69))
    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            run = False
    # button_open_example.draw()
    # button_open_example.listen(events)
        # rect_color = (0,0,0)
        # rect_coords = pg.Rect(30,30,60,60)
        # rect = pg.draw.rect(screen, rect_color, rect_coords, 2) 
    if example_app:
        app2_no = apps.Example(screen)
        # app2_no = app2_no.rect_color = (50,125,100)
        app2_no.rect
        screen.blit(app2_no.text, (50,85))
        close_app_example.draw()
        close_app_example.listen(events)
        
    def app_example():
        while True:
            return apps.Example(screen).rect

    # app_example()
    def create_app_icon(x,y,height,width,text, font_size,inactive_color,on_click):
    
        button_open_example = pw.Button(win=screen,x=x,y=y,height=height,width=width,text=str(text),fontSize=font_size,margin=20,hoverColour=(68,172,249),
                    inactiveColour=inactive_color,radius=20,onClick=on_click)
        draw = button_open_example.draw()
        listen = button_open_example.listen(events)
        return button_open_example, draw, listen
    # rect_color = (0,0,0)
    # rect_coords = pg.Rect(30,30,60,60)
    # pg.draw.rect(screen, rect_color, rect_coords, 2)
    # # BuiltinApps.open_terminal

    app_slider.listen(events)
    app_slider.draw()

    # when want to add slider apps value then do like this


    # if app_slider.getValue() == 0:
    #     button_open_example.draw()
    #     button_open_example.listen(events)
        
    # button_close_example.draw()
    # button_close_example.listen(events)

    # for app_slide_num_test_cal in range(10,20):
    #     if app_slider.getValue() == app_slide_num_test_cal:
    #         button_exit_app.draw()
    #         button_exit_app.listen(events)

    # for i in range(20,30):
    #     if app_slider.getValue() == i:
    #         button_open_terminal.draw()
    #         button_open_terminal.listen(events)

            
            

    
    # create pin apps variable one you use the slider
    button_open_example.draw()
    button_open_example.listen(events)
    
    button_open_terminal.draw()
    button_open_terminal.listen(events)

    button_close_example.draw()
    button_close_example.listen(events)

    
    button_exit_app.draw()
    button_exit_app.listen(events)

#TODO bookmark: test bookmark
    # create_app_icon(x=42,y=197,height=60,width=60,text='T',font_size=50,inactive_color=(247,207,69),on_click=BuiltinApps.open_terminal)
    pg.display.update()
