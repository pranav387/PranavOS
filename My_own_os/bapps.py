# you need to manually add your app to this list
reg_apps = ['Example App','Task Manager']


class Example:
    def __init__(self,win):
        import pygame as pg
        import pygame_widgets as pw
        # global register_apps

        # steps to write app code here
        # 1. Create rect
        # 2. Create Close button
        # 3. Make code that should fit in rect
        # 4. Modify the main.pyw file to make the code running
        self.rect_color = (50,125,100)
        self.rect_coords = pg.Rect(30,30,200,200)
        # self.rect = pg.draw.rect(win, self.rect_color, self.rect_coords, 2) 
        self.rect = pg.draw.rect(win, self.rect_color, self.rect_coords) 

        self.font = pg.font.Font('freesansbold.ttf', 25)
 

        self.text = self.font.render('Example App', (0,0,0), True)
        

        self.button_close = pw.Button(win=win,x=42,y=100,height=60,width=60,text='terminal',fontSize=20,margin=20,hoverColour=(68,172,249),
                inactiveColour=(247,207,69),pressedColour=(68,172,249),radius=20,onClick=None) 
        return None


class Terminal:
    def __init__(self):
        pass


class TaskMgr:
    def __init__(self,win,tskmgr_open):
        import pygame as pg
        import pygame_widgets as pw
        self.rect_color = (50,125,100)

        # self.taskmgr_open = True

        self.rect_coords = pg.Rect(30,30,200,350)

        self.rect = pg.draw.rect(win, self.rect_color, self.rect_coords) 

        self.font = pg.font.Font('freesansbold.ttf', 25)

        self.text = self.font.render('Example App', (0,0,0), True)


        self.button_close = pw.Button(win=win,x=350,y=35,height=20,width=20,text='X',fontSize=20,margin=20,hoverColour=(68,172,249),
        inactiveColour=(247,207,69),pressedColour=(68,172,249),radius=20,onClick=tskmgr_open)

        return None
