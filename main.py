from tkinter import *
def display_coordinates(event):
    my_label['text']=f'x={event.x} y={event.y}'
my_window = Tk()
my_canvas = Canvas(my_window,width=400,height=400,background='white')
my_label=Label(bd=4,relief="solid",font="Times 22 bold",bg="white",fg="black")
my_canvas.bind('<Button-1>',display_coordinates)
my_canvas.grid(row=0,column=0)
my_label.grid(row=1,column=0)
my_window.mainloop()
