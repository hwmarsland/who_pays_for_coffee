import tkinter as tk
from tkinter import ttk
from person import *
import pandas as pd
import os

drinks = drinkList
people = peopleList


def addSomeone(gui_instance):
    frames = subWindowStaticTemplate('Add Someone', 'Who do you want to add?')

    tk.Label(frames[0], text='Name').grid(row=0)
    name = tk.Entry(frames[0])
    name.grid(row=0, column=1)

    confirmButton = tk.Button(frames[1], text='Confirm', font=('helvetica', 18), fg='green', highlightbackground='green', highlightthickness=1, command= lambda: addSomeoneData(name, gui_instance))
    confirmButton.pack(side='right', padx=10)


def addDrink(gui_instance):
    frames = subWindowStaticTemplate('Add Drink', 'What drink do you want to add?')

    # New drink entry blocks
    tk.Label(frames[0], text='Drink').grid(row=0) 
    tk.Label(frames[0], text='Price ($)').grid(row=1)
    drink = tk.Entry(frames[0])
    price = tk.Entry(frames[0])
    drink.grid(row=0, column=1)
    price.grid(row=1, column=1)

    confirmButton = tk.Button(frames[1], text='Confirm', font=('helvetica', 18), fg='green', highlightbackground='green', highlightthickness=1, command= lambda: addDrinkData(drink, price, gui_instance))
    confirmButton.pack(side='right', padx=10)


# Template for several sub windows to conform to DRY principles
def subWindowStaticTemplate(title, header): 
    subWindow = tk.Tk()
    subWindow.title(title)

    # Title within the window
    titleFrame = tk.Frame(subWindow) 
    titleFrame.pack(padx=100, pady=20)
    title = tk.Label(titleFrame, text=header, font=('helvetica', 24, 'bold'), fg='#563517') 
    title.pack(fill=tk.BOTH, expand=1)

    # Middle window where data can be entered
    middleFrame = tk.Frame(subWindow) 
    middleFrame.pack(padx=100, pady=(0, 20))

    # Confirm or cancel buttons
    confirmFrame = tk.Frame(subWindow) 
    confirmFrame.pack(padx=100, pady=(0, 20))
    cancelButton = tk.Button(confirmFrame, text='Cancel', font=('helvetica', 18), fg='red', highlightbackground='red', highlightthickness=1, command=subWindow.destroy)
    cancelButton.pack(side='left', padx=10)

    return [middleFrame, confirmFrame]

def popupWindow(title, header, color):
    subWindow = tk.Tk()
    subWindow.title(title)

    # Title within the window
    titleFrame = tk.Frame(subWindow) 
    titleFrame.pack(padx=100, pady=20)
    title = tk.Label(titleFrame, text=header, font=('helvetica', 18, 'bold'), fg=color) 
    title.pack(fill=tk.BOTH, expand=1)

def addSomeoneData(name, gui_instance):
    global people_df
    personName = name.get()
    flag = 1
    try: # Check if input is correct
        if personName == '':
            popupWindow('Error', 'Input Error', 'red')
            flag = 0
    except:
        popupWindow('Error', 'Input Error', 'red')
        flag = 0
    else:
        for i in people.personList: # Check if person is already in list
            if i.name == personName:
                popupWindow('Error', 'Person Already Exists', 'red')
                flag = 0
    if flag == 1:
        people.personList.append(person(personName)) # Add the new person to the list of people
        '''
        # Add function to save to file, add in later when I have more time
        newRow = {'Name': name, 'Balance': 0, 'LastPurchased': '', 'TotalBalance': 0}
        people_df = people_df.append(newRow, ignore_index=True)
        '''
        # for i in people.personList: # Used for testing purposes
        #     print(i.name)
        gui_instance.updatePeopleDisplay()
    

def addDrinkData(drinkName, drinkPrice, gui_instance):
    global drinks_df
    name = drinkName.get()
    price = drinkPrice.get()
    flag = 1
    try: # Check if input is correct
        if name == '' or price == '' or int(price) <= 0 or int(price) > 1000:
            popupWindow('Error', 'Input Error', 'red')
            flag = 0
    except:
        popupWindow('Error', 'Input Error', 'red')
        flag = 0
    else:
        for i in drinks.dict.keys(): # Check if drink is already in dict
            if i == name:
                popupWindow('Error', 'Drink Already Exists', 'red')
                flag = 0
    if flag == 1:
        drinks.dict[name] = int(price) # Add drink to drink list
        '''
        # Add function to save to file, add in later when I have time
        # newRow = {'DrinkName': name, 'Price': int(price)}
        # drinks_df = drinks_df.append(newRow, ignore_index=True)
        '''
        # print(drinks.dict) # Line for testing purposes
        newDrink = 'New Drink: ' + name + ', $' + price
        popupWindow('Drink Added', newDrink, '#563517')
        gui_instance.updatePeopleDisplay()