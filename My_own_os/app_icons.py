class CreateAppIcon:
    def __init__(self, screen, events, x,y,height,width,text, font_size,inactive_color,on_click):
        import pygame_widgets as pw
        self.button_open_terminal = pw.Button(win=screen,x=x,y=y,height=height,width=width,text=str(text),fontSize=font_size,margin=20,hoverColour=(68,172,249),
                    inactiveColour=inactive_color,radius=20,onClick=on_click)
        self.draw = self.button_open_terminal.draw()
        self.listen = self.button_open_terminal.listen(events)
        return None

print(0)
        