#!/usr/bin/env python
"""
A simple GUI program used to display and track who is attending stand up 
meetings as well as who has presented already. 
"""
from tkinter import *
import tkinter as tk
import tkinter.font as tkFont
from tkinter.messagebox import showinfo
from typing import Tuple
import constants as const

__author__ = "Dan Gerstl"
__copyright__ = "Copyright 2021, Dan Gerstl, All rights reserved"
__credits__ = ["Dan Gerstl",]
__version__ = "1.1"
__maintainer__ = "Dan Gerstl"
__email__ = "drgerstl@gmail.com"

# Global Variables
top = tk.Tk()
employeeList = []
row = 0
col = 0
hostAssigned = False

class Main(Frame):
    def __init__(self, parent=None):
        """ Create main view to allow changing the title on the frame """
        Frame.__init__(self, parent)
        self.parent = parent

class Employee:
    def __init__(self, name, view):
        """ 
        Class that contains the employee name and associated buttons and label.
        """
        # Component variables
        self.attendingBtnVal = IntVar()
        self.presentedBtnVal = IntVar()
        self.lblText = StringVar()

        # Class Variables
        self.name = name
        self.label = Label(view, textvariable=self.lblText, relief=FLAT, 
                           font=const.FONT, state=DISABLED)
        
        self.label.bind('<Button-1>', self.toggleLabel)
        
        self.checkBtnAttending = tk.Checkbutton(
            view, text=const.ATTENDING, command=self.toggleAttending,
            variable=self.attendingBtnVal, onvalue=ON, offvalue=OFF, 
            height=const.BTN_HEIGHT, width=const.BTN_WIDTH)

        self.checkBtnPresented = tk.Checkbutton(
            view, text=const.TO_PRESENT, command=self.togglePresented, 
            state=DISABLED, variable=self.presentedBtnVal, onvalue=ON, 
            offvalue= OFF, height= const.BTN_HEIGHT, width= const.BTN_WIDTH)

        # Set employee name as label text    
        self.lblText.set(self.name)

    def toggleLabel(self, event):
        """
        Toggles whether or not the HOST label is displayed on an Employee's 
        label.
        """
        # Global Variables
        global hostAssigned

        if (self.label['state'] == const.ENABLED and not hostAssigned):
            self.lblText.set(self.name + const.HOST)
            hostAssigned = True
        elif (self.label['state'] == const.ENABLED and hostAssigned):
            if const.HOST in self.lblText.get():
                self.lblText.set(self.name)
                hostAssigned = False  

    def toggleAttending(self):
        """ 
        Function is fired on checking the attendance checkbutton and updates GUI 
        based on value.
        """
        # Global Variables
        global hostAssigned

        # Box goes from unchecked -> checked
        if (self.attendingBtnVal.get() == ON):         
            
            # Enable presented checkbox
            self.checkBtnPresented['state'] = const.ENABLED   
            
            # Enable label and set color for attending
            self.label['state'] = const.ENABLED               
            self.label.config(fg= const.ATTENDING_COLOR)

            # Change cursor to indicate its clickable
            self.label['cursor'] = 'hand2'              
        else: # Box goes from checked -> unchecked
            clearEmployee(self)

    def togglePresented(self):
        """
        Function is fired on checking the presented checkbutton and updates GUI 
        based on value.
        """
        if (self.checkBtnPresented['text'] == const.TO_PRESENT):
            self.checkBtnPresented['text'] = const.PRESENTED
            self.label.config(fg= const.PRESENTED_COLOR)
        else:
            self.checkBtnPresented['text'] = const.TO_PRESENT
            self.label.config(fg= const.ATTENDING_COLOR)

def showEmployee(Employee, start, col):
    """ Used to display the Employee class components on GUI """
    # Set starting row and add label
    row = start
    Employee.label.grid(row=row, column=col, padx=const.LBL_PAD_X, 
                        pady=const.LBL_PAD_Y)
    
    # Underline font in label
    f = tkFont.Font(Employee.label, Employee.label.cget('font'))
    f.configure(underline = True)
    f.configure()
    Employee.label.configure(font=f)

    # Move down rows and add checkbuttons
    row += 1
    Employee.checkBtnAttending.grid(row=row, column=col, padx=const.BOX_PAD_X)
    row += 1
    Employee.checkBtnPresented.grid(row=row, column=col, padx=const.BOX_PAD_X)

    # Move row back to start for next employee
    row = start


def clearEmployee(Employee):
    """ Clears the GUI components associated with an employee """
    # Global Variables
    global hostAssigned

    # Reset attending checkbutton
    Employee.attendingBtnVal.set(OFF)
    Employee.checkBtnAttending['text'] = const.ATTENDING  

    # Reset presented checkbutton
    Employee.presentedBtnVal.set(OFF)
    Employee.checkBtnPresented['text'] = const.TO_PRESENT
    Employee.checkBtnPresented['state'] = DISABLED

    # Disable employee label
    Employee.label['state'] = DISABLED
    Employee.label['cursor'] = 'arrow'
    if const.HOST in Employee.lblText.get():
        Employee.lblText.set(Employee.name)
        hostAssigned = False

def clearAll(employeeList):
    """ Clears the GUI components associated with all employees """
    for employee in employeeList:
        clearEmployee(employee)


""" These methods are for using a button instead of a checkbox """
#region
# class Employee:
#     def __init__(self, name, view):

#         #-- Component variables --#
#         attendingBtnVal = IntVar()
#         presentedBtnVal = IntVar()
#         lblText = StringVar()

#         #-- Class Variables--#
#         self.name = name
#         self.label = Label(view, textvariable=lblText, relief=FLAT, font=FONT)
#         self.checkBtnAttending = tk.Button(view, text= ATTENDING, command= self.toggleAttending, \
#                                            height= BTN_HEIGHT, width= BTN_WIDTH)

#         self.checkBtnPresented = tk.Button(view, text= PRESENTED, command= self.togglePresented, \
#                                            height= BTN_HEIGHT, width= BTN_WIDTH, state='disabled')

#         #-- Set label name --#        
#         lblText.set(self.name)
    
#     def toggleAttending(self):
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
        
        

#     def togglePresented(self):
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

#endregion

def makeWidgets(view, row, col):
    """ Draws the GUI """
    # Set title for main window
    view.winfo_toplevel().title(const.TITLE)

    # Create Employee list
    sortedEmployees = const.EMPLOYEES
    sortedEmployees.sort()
    for name in const.EMPLOYEES:
        employeeList.append(Employee(name, top))

    # Add Employees to top view 
    for employee in employeeList:
        showEmployee(employee, row, col)

        # Adjust location for grid layout
        col += 1
        if (col == 4):
            col = 0
            row += 4

def addUtilityButtons(row, col):
    # Add Clear button  
    btnClear = tk.Button(
        top,height=const.BTN_HEIGHT, width=const.BTN_WIDTH, 
        text="Clear", command=lambda:clearAll(employeeList))

    btnClear.grid(row=row, column=col, padx=const.BTN_PAD_X, pady=(10,0))

main = Main(top)

# Add utility buttons to top 
addUtilityButtons(row, col)

# Move the starting position to add widgets
row += 1

# Add widgets to main view
makeWidgets(main, row, col)

# Set window size and disable resizing
top.geometry(const.WINDOW_SIZE)
top.resizable(False, False)

# Set no host
hostAssigned = False

# Start
top.mainloop()