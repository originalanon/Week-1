from tkinter import *
from shapely.geometry import Polygon
import json

f = open('plant_info.json')

plant_data = json.load(f)

root = Tk()

root.geometry("400x600")


drawing_window_frame = Frame(root)
drawing_window = Canvas(root, width = 400, height = 400)


drawing_window_frame.pack()
drawing_window.pack()
##this is the list of all coordinates -- needed to calculate the area
point_coordinates = []

##this window will always be the last coordinate drawn, and the user's next one
point_coordinates_window = []

##list of coordinates for each individual shape
areas = []

def add_point(event):

    x, y = event.x, event.y

    label = Label(drawing_window_frame, text=f"{x} : {y}")
    ##label.pack()

    point_coordinates.append((x, y))
    point_coordinates_window.append((x, y))
    if(len(point_coordinates_window) > 1):
        label.destroy()
        draw_connected_line()




##draw the line, then pop the first coordinate so that the last coordinate is the first one now for the next line
def draw_connected_line():
    drawing_window.create_line(point_coordinates_window, fill='black', width=5)
    point_coordinates_window.pop(0)


##stop drawing, connect to first coordinate
def stop(event):
    drawing_window.create_line((point_coordinates[0], point_coordinates_window[0]), fill='black', width=5)
    
    point_coordinates_window.pop()

    ##create polygon from the points and get it's area -- add it to the areas list
    areas.append(Polygon(point_coordinates).area)

    point_coordinates.clear()

##updates mouse label with distance between two points
def update_mouse_label():
    drawing_window.after(500, update_mouse_label)

def create_plant(plant_name):
    width = plant_data['plants'][plant_name]['minimum_space_inches']
    drawing_window.create_rectangle(0, 0, width, width, outline = "black", fill = "green", width = 2)



root.bind('<Button-1>', add_point)
root.bind('z', stop)
root.mainloop()

print(areas)

