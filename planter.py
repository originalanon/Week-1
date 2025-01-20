from tkinter import *
root = Tk()

root.geometry("400x400")


drawing_window_frame = Frame(root)
drawing_window = Canvas(root, width = 400, height = 400)


drawing_window_frame.pack()
drawing_window.pack()
##this is the list of all coordinates -- needed to calculate the area
point_coordinates = []

##this window will always be the last coordinate drawn, and the user's next one
point_coordinates_window = []

def add_point(event):

    x, y = event.x, event.y

    label = Label(drawing_window_frame, text=f"{x} : {y}")
    label.pack(pady=40)

    point_coordinates.append((x, y))
    point_coordinates_window.append((x, y))
    if(len(point_coordinates_window) > 1):
        draw_connected_line()
        label.destroy()




##draw the line, then pop the first coordinate so that the last coordinate is the first one now for the next line
def draw_connected_line():
    drawing_window.create_line(point_coordinates_window, fill='black', width=5)
    point_coordinates_window.pop(0)


##stop drawing, connect to first coordinate
def stop(event):

    print(point_coordinates_window)
    point_coordinates_window.pop()
    drawing_window.create_line((point_coordinates[0], (0, 0)), fill='black', width=5)

##updates mouse label with distance between two points
def update_mouse_label():
    drawing_window.after(500, update_mouse_label)




root.bind('<Button-1>', add_point)
root.bind('z', stop)
root.mainloop()

