from tkinter import *
import tkinter as tk
import tkinter.font as tkFont
from tkinter.messagebox import showinfo
from typing import Tuple

#-- Constants --#
EMPLOYEES = ['Dan', 'Harish', 'Jagan', 'Manjula', 'Nikhil', 'Prathap', \
            'Shubham', 'Siva', 'Sneha', 'Srikanth', 'Timothy', 'Vimal', 'Viplav']

ATTENDING = 'Attending'
TO_PRESENT = 'To present'
PRESENTED = 'Done'
BTN_HEIGHT = 1
BTN_WIDTH = 12
FONT = 'Helvetica 10 bold'
BTN_PAD_X = (25,25)
BOX_PAD_X = (15,15)
LBL_PAD_X = (10,10)
LBL_PAD_Y = (10,5)
WINDOW_SIZE = '560x410'
ON = 1
OFF = 0
DISABLED = 'disabled'
ENABLED = 'normal'
HOST = ' - HOST'


#-- Global Variables --#
top = tk.Tk()
employeeList = []
row = 0
col = 0
hostAssigned = False

#-- Create main view to allow changing the title on the frame --#
class Main(Frame):
    def __init__(self,parent=None):
        Frame.__init__(self,parent)
        self.parent = parent

#-- Employee class that holds employee name information and the buttons/label for them --#
class Employee:
    def __init__(self, name, view):

        #-- Component variables --#
        self.attendingBtnVal = IntVar()
        self.presentedBtnVal = IntVar()
        self.lblText = StringVar()

        #-- Class Variables--#
        self.name = name
        self.label = Label(view, textvariable=self.lblText, relief=FLAT, font=FONT, state=DISABLED)
        
        self.label.bind('<Button-1>', self.checkLabel)
        
        self.checkBtnAttending = tk.Checkbutton(view, text= ATTENDING, \
                                            command=self.checkAttending, \
                                            variable= self.attendingBtnVal, onvalue= ON, \
                                            offvalue= OFF, height= BTN_HEIGHT, width= BTN_WIDTH)

        self.checkBtnPresented = tk.Checkbutton(view, text= TO_PRESENT, \
                                            command=self.checkPresented, state= DISABLED,\
                                            variable= self.presentedBtnVal, onvalue= ON, \
                                            offvalue= OFF, height= BTN_HEIGHT, width= BTN_WIDTH)

        #-- Set employee name as label text --#        
        self.lblText.set(self.name)

    def checkLabel(self, event):

        global hostAssigned

        if (self.label['state'] == ENABLED and not hostAssigned):
            self.lblText.set(self.name + HOST)
            hostAssigned = True
        elif (self.label['state'] == ENABLED and hostAssigned):
            if HOST in self.lblText.get():
                self.lblText.set(self.name)
                hostAssigned = False
    
    #-- Function is fired on checking the attendance checkbutton and updates GUI based on value --#
    def checkAttending(self):

        global hostAssigned

        # Box goes from unchecked -> checked
        if (self.attendingBtnVal.get() == ON):         
            
            # Enable presented checkbox
            self.checkBtnPresented['state'] = ENABLED   
            
            # Enable label and set color to red
            self.label['state'] = ENABLED               
            self.label.config(fg= 'red')

            # Change cursor to indicate its clickable
            self.label['cursor'] = 'hand2'              
        else: # Box goes from checked -> unchecked
            # Reset attending checkbutton
            self.checkBtnAttending['text'] = ATTENDING  

            # Reset presented checkbutton
            self.presentedBtnVal.set(OFF)
            self.checkBtnPresented['text'] = TO_PRESENT
            self.checkBtnPresented['state'] = DISABLED

            # Disable employee label
            self.label['state'] = DISABLED
            self.label['cursor'] = 'arrow'
            if HOST in self.lblText.get():
                self.lblText.set(self.name)
                hostAssigned = False

    #-- Function is fired on checking the presented checkbutton and updates GUI based on value --#
    def checkPresented(self):
        if (self.checkBtnPresented['text'] == TO_PRESENT):
            self.checkBtnPresented['text'] = PRESENTED
            self.label.config(fg= 'limegreen')
        else:
            self.checkBtnPresented['text'] = TO_PRESENT
            self.label.config(fg= 'red')

#-- Used to display the Employee class components --#
def showEmployee(Employee, start, col):

    # Set starting row and add label
    row = start
    Employee.label.grid(row=row, column=col, padx=LBL_PAD_X, pady=LBL_PAD_Y)
    
    # Underline font in label
    f = tkFont.Font(Employee.label, Employee.label.cget('font'))
    f.configure(underline = True)
    f.configure()
    Employee.label.configure(font=f)

    # Move down rows and add checkbuttons
    row += 1
    Employee.checkBtnAttending.grid(row=row, column=col, padx=BOX_PAD_X)
    row += 1
    Employee.checkBtnPresented.grid(row=row, column=col, padx=BOX_PAD_X)

    # Move row back to start for next employee
    row = start        

### These methods are for using a button instead of a checkbox ###

# class Employee:
#     def __init__(self, name, view):

#         #-- Component variables --#
#         attendingBtnVal = IntVar()
#         presentedBtnVal = IntVar()
#         lblText = StringVar()

#         #-- Class Variables--#
#         self.name = name
#         self.label = Label(view, textvariable=lblText, relief=FLAT, font=FONT)
#         self.checkBtnAttending = tk.Button(view, text= ATTENDING, command= self.checkAttending, \
#                                            height= BTN_HEIGHT, width= BTN_WIDTH)

#         self.checkBtnPresented = tk.Button(view, text= PRESENTED, command= self.checkPresented, \
#                                            height= BTN_HEIGHT, width= BTN_WIDTH, state='disabled')

#         #-- Set label name --#        
#         lblText.set(self.name)
    
#     def checkAttending(self):
#     # label.config(text='TED')
#     # tk.messagebox.showinfo(title=checkboxVar.get(), message=checkboxVar.get())
#     # if (checkboxVar == 'ON'):
#     #     tk.messagebox.showinfo(title=checkboxVar.get(), message=checkboxVar.get())
#         if (self.checkBtnAttending['text'] == ATTENDING):
#             self.checkBtnAttending['text'] = 'Not Attending'
#             self.checkBtnPresented['state'] = 'normal'
#         else:
#             self.checkBtnAttending['text'] = ATTENDING
#             self.checkBtnPresented['state'] = 'disabled'
        
        

#     def checkPresented(self):
#         if (self.checkBtnPresented['text'] == PRESENTED):
#             self.checkBtnPresented['text'] = 'Done'
#         else:
#             self.checkBtnPresented['text'] = PRESENTED


# #-- Used to display the Employee class components --#
# def showEmployee(Employee, start, col):
#     row = start
#     Employee.label.grid(row=row, column=col, padx=LBL_PAD_X, pady=LBL_PAD_Y)
#     f = tkFont.Font(Employee.label, Employee.label.cget('font'))
#     f.configure(underline = True)
#     f.configure()
#     Employee.label.configure(font=f)
#     row += 1
#     Employee.checkBtnAttending.grid(row=row, column=col, padx=BTN_PAD_X)
#     row += 1
#     Employee.checkBtnPresented.grid(row=row, column=col, padx=BTN_PAD_X)
#     row = start

def makeWidgets(view, row, col):

    # Set title for main window
    view.winfo_toplevel().title('Standup Tracker')

    #-- Create Employee list --#
    for name in EMPLOYEES:
        employeeList.append(Employee(name, top))

    #-- Add components to top view --#
    for employee in employeeList:
        showEmployee(employee, row, col)

        # Adjust location for grid layout
        col += 1
        if (col == 4):
            col = 0
            row += 4

main = Main(top)

# Add widgets to main view
makeWidgets(main, row, col)


# Set window size and disable resizing
# top.geometry(WINDOW_SIZE)
top.resizable(False, False)

# Set no host
hostAssigned = False

top.mainloop()