from buttonScripts import *


class StaticGUI:

    def __init__(self, root):
        self.root = root
        self.setWindowBasics()
        self.updatePeopleDisplay()

    def setWindowBasics(self):
        self.root.title('Who Pays For Coffee?') # Window header
        self.root.minsize(width=500, height=300) # Window minimum size

        # Title within the window
        titleFrame = tk.Frame(self.root)
        titleFrame.pack(padx=100, pady=20)
        self.title = tk.Label(titleFrame, text='Who Pays?', font=('helvetica', 36, 'bold'), fg='#563517') 
        self.title.pack(fill=tk.BOTH, expand=1)

        # Frame that will hold all of the users
        self.peopleFrame = tk.Frame(self.root, bd=2, relief='groove') 
        self.peopleFrame.pack(padx=20, fill=tk.BOTH, expand=1)

        addPersonFrame = tk.Frame(self.root)
        addPersonFrame.pack(padx=20, pady=5, fill='x')
        # Button to add a person
        self.addPerson = tk.Button(addPersonFrame, text='+ Add Someone', font=('helvetica', 18), fg='#9c6f44', command=lambda: addSomeone(self)) 
        self.addPerson.pack(side='left')
        # Button to add a drink
        self.addDrink = tk.Button(addPersonFrame, text='+ Add Drink', font=('helvetica', 18), fg='#9c6f44', command=lambda: addDrink(self)) 
        self.addDrink.pack(side='right')

        # Button to start the who pays program
        goButtonFrame = tk.Frame(self.root)
        goButtonFrame.pack(pady=(0,20), side='bottom')
        self.goButton = tk.Button(goButtonFrame, text='GO', font=('helvetica', 24, 'bold'), fg='green', 
                                  highlightbackground='green', highlightthickness=1, command=self.updateBalandSelectMax) 
        self.goButton.pack()

    def updatePeopleDisplay(self):
        # Clear existing content in peopleFrame
        for widget in self.peopleFrame.winfo_children():
            widget.destroy()
        
        # Display each person's details
        for person in people.personList:
            # Add frame for each person
            personFrame = tk.Frame(self.peopleFrame, borderwidth=1, relief="solid")
            personFrame.pack(padx=10, pady=5, fill=tk.X, expand=True)
            personFrame.person = person

            # Add a label with the person's name
            nameLabel = tk.Label(personFrame, text=person.name)
            nameLabel.pack(side='left', padx=10)

            # Add a dropdown for selecting the drink
            if person.lastPurchased == '':
                drink = tk.StringVar(value='Select Drink')
            else:
                drink = tk.StringVar(value=person.lastPurchased)
            drinkDropdown = ttk.Combobox(personFrame, textvariable=drink, values=list(drinkList.dict.keys()))
            drinkDropdown.pack(side='right', padx=10)
            personFrame.drinkVar = drink
    
    def updateBalandSelectMax(self):
        totalDrinkPrice = 0

        # Pointers
        for personFrame in self.peopleFrame.winfo_children():
            person = personFrame.person 
            drinkVar = personFrame.drinkVar
            drinkName = drinkVar.get()

            # Update person's balance and totalBal based on selected drink's price
            if drinkName in drinkList.dict:
                drinkPrice = drinkList.dict[drinkName]
                person.bal += drinkPrice
                person.totalBal += drinkPrice
                person.lastPurchased = drinkName
                totalDrinkPrice += drinkPrice
        
        # Find the person with the max balance
        maxBal = -1000000000000
        maxBalPerson = None
        for person in people.personList:
            if person.bal > maxBal:
                maxBal = person.bal
                maxBalPerson = person


        # Adjust their balance by subtracting the total price of everyone's drinks
        if maxBalPerson:
            maxBalPerson.bal -= totalDrinkPrice
            self.showWhoPays(maxBalPerson)
    
    def showWhoPays(self, person):
        # Create new window to display who pays
        payeeWindow = tk.Toplevel(self.root)
        payeeWindow.title('Who Pays?')
        tk.Label(payeeWindow, text=f"It's {person.name}'s turn to pay", font=("Helvetica", 36), fg='#563517').pack(pady=20)
        for i in people.personList:
            print(i.name, i.bal)
        print('\n')

    '''
    FUTURE ADDITIONS WHEN I HAVE MORE TIME
    def bootFromFile(self):
        global people_df
        global drinks_df
        if not os.path.exists('WhoPaysData.xlsx'):
            # Create a DataFrame for people with the appropriate columns
            peopleColumns = ['Name', 'Balance', 'LastPurchased', 'TotalBalance']
            people_df = pd.DataFrame(columns=peopleColumns)
    
            # Create a DataFrame for drinks with the appropriate columns
            drinksColumns = ['DrinkName', 'Price']
            drinks_df = pd.DataFrame(columns=drinksColumns)
    
            # Use ExcelWriter to create an Excel file with two sheets
            with pd.ExcelWriter('WhoPaysData.xlsx', engine='xlsxwriter') as writer:
                people_df.to_excel(writer, sheet_name='People', index=False)
                drinks_df.to_excel(writer, sheet_name='Drinks', index=False)
            
        xls = pd.ExcelFile('WhoPaysData.xlsx')
        people_df = pd.read_excel(xls, 'People')
        drinks_df = pd.read_excel(xls, 'Drinks')

        # Clear existing data
        people.personList.clear()
        drinks.dict.clear()  # Assuming you will replace this dict with a list

        # Update to use a list for drinks
        drinks.dict = drinks_df.to_dict('records')

        # Populate the peopleList from the DataFrame
        for _, row in people_df.iterrows():
            newPerson = person(row['Name'])
            newPerson.bal = row['Balance']
            newPerson.lastPurchased = row.get('LastPurchased', '')
            newPerson.totalBal = row['TotalBalance']
            peopleList.personList.append(newPerson)
    '''






root = tk.Tk()
gui = StaticGUI(root)
# gui.bootFromFile()
root.mainloop()